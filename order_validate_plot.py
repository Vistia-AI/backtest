from datetime import datetime
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import seaborn as sns
from seaborn import lineplot
from typing import List, Union

from dotenv import load_dotenv
from sqlalchemy import create_engine
load_dotenv()

DB_URL = os.getenv('DB_URL')

engine = create_engine(
    DB_URL,
    pool_pre_ping=True,   # checks connection before using
    pool_recycle=1800,    # optional: avoids stale timeouts
    connect_args={"check_same_thread": False} if "sqlite" in DB_URL else {},
)
# engine
SCHEMA = 'proddb.'
tables = {
    'p5m': SCHEMA+'coin_prices_5m',
    'p1h': SCHEMA+'coin_prices_1h',
    'f5m': SCHEMA+'f_coin_signal_5m',
    'f10m': SCHEMA+'f_coin_signal_10m',
    'f15m': SCHEMA+'f_coin_signal_15m',
    'f30m': SCHEMA+'f_coin_signal_30m',
    'f1h': SCHEMA+'f_coin_signal_1h',
    'f4h': SCHEMA+'f_coin_signal_4h',
    'f1d': SCHEMA+'f_coin_signal_1d',
    'f1D': SCHEMA+'f_coin_signal_1d',
    'orders': SCHEMA+'trade_orders_sim',
    'tp_by_sess': SCHEMA+'trade_orders_tp_by_session',
    }


def get_data(start_time, end_time, symbols=['ETHUSDT'], lookback=14, lookforward=25):
    """
    Process order and price data to create normalized sequences around each order.
    
    Parameters:
    -----------
    df_orders : pd.DataFrame
        DataFrame with columns: symbol, open_time, 'order', price
    df_prices : pd.DataFrame  
        DataFrame with columns: open_time, symbol, high, low, close
    lookback : int, optional
        Number of prices before order (default: 14)
    lookforward : int, optional
        Number of prices after order (default: 25)
    
    Returns:
    --------
    tuple
        (buy_df, sell_df) - Two DataFrames with columns: x, y, time
    """
    # symbol = 'ETHUSDT'
    # from_time = int(datetime(2025, 4, 1, 0, 0, 0).timestamp())
    # from_time = 1757563200
    str_symbols = "'" + "', '".join(symbols) + "'"
    sql_orders = f"""
        select symbol, open_time, a.order, price
        from proddb.trade_orders_sim a
        where timeframe = '1h' 
            and symbol in ({str_symbols})
            and strategy = 'adx_ep_trend_reverse'
            and open_time >= {start_time}
            and open_time <= {end_time}
        order by symbol asc, open_time asc
    """

    sql_prices = f"""
        select open_time, symbol, high, low, close
        from  proddb.coin_prices_1h
        where open_time >= {start_time}
            and open_time <= {end_time}
            and symbol in ({str_symbols})
        order by symbol asc, open_time asc
    """

    df_orders = pd.read_sql(sql_orders, engine)
    print("Orders sample:\n", df_orders.head())
    if df_orders.empty:
        print("No orders found for given filters.")
        return pd.DataFrame(columns=['symbol','close','high','low','pos','time']), pd.DataFrame(columns=['symbol','close','high','low','pos','time'])
    print("Orders by symbol:\n", df_orders['symbol'].value_counts())
    print("Orders by type:\n", df_orders['order'].astype(str).str.lower().value_counts())
    df_prices = pd.read_sql(sql_prices, engine)


    # Sort prices by time
    df_prices = df_prices.sort_values('open_time').reset_index(drop=True)
    # Quick coverage overview per symbol
    if not df_prices.empty:
        coverage = (df_prices.groupby('symbol')['open_time']
                               .agg(['min', 'max', 'count'])
                               .reset_index())
        print("Price coverage (per symbol):\n", coverage.to_string(index=False))
    
    # Create lists to store per-order DataFrames for efficient concat
    print(f"Processing {len(df_orders)} orders...")
    buy_frames: List[pd.DataFrame] = []
    sell_frames: List[pd.DataFrame] = []

    collected_buy = collected_sell = 0
    skipped_edge = skipped_nomatch = 0
    
    for idx, order in df_orders.iterrows():
        order_time = order['open_time']
        order_price = order['price']
        order_type = order['order']  # This should be 'buy' or 'sell'
        order_symbol = order['symbol']  
        
        # Work only with prices of the same symbol
        symbol_prices = df_prices[df_prices['symbol'] == order_symbol].copy()
        if symbol_prices.empty:
            print(f"Warning: No price series for symbol {order_symbol}")
            continue
        symbol_prices = symbol_prices.sort_values('open_time').reset_index(drop=True)
        
        # Try exact time match first
        exact_idx = symbol_prices[symbol_prices['open_time'] == order_time].index
        if len(exact_idx) > 0:
            order_price_idx = int(exact_idx[0])
        else:
            # Fallback to nearest time within same symbol
            if not symbol_prices['open_time'].empty:
                nearest_idx = (symbol_prices['open_time'] - order_time).abs().idxmin()
                order_price_idx = int(nearest_idx)
            else:
                skipped_nomatch += 1
                continue
        
        # Calculate start and end indices for the sequence within this symbol's series
        start_idx = max(0, order_price_idx - lookback)
        end_idx = min(len(symbol_prices), order_price_idx + lookforward + 1)

        # Extract the price sequence for this symbol only (clamped window)
        price_sequence = symbol_prices.iloc[start_idx:end_idx].copy()
        
        if len(price_sequence) < (lookback + lookforward + 1):
            print(f"Warning: Insufficient price data for order at {order_time}, symbol {order_symbol}")
            continue
        
        # Normalize prices by dividing by order price
        price_sequence['nor_close'] = price_sequence['close'] / order_price
        price_sequence['nor_high'] = price_sequence['high'] / order_price
        price_sequence['nor_low'] = price_sequence['low'] / order_price
        
        # Create position array (candle position relative to order), adjusted to clamp window
        left_span = order_price_idx - start_idx
        right_span = end_idx - order_price_idx - 1
        positions = list(range(-left_span, right_span + 1))
        
        # Build a per-order DataFrame (vectorized) then append to list
        order_df = pd.DataFrame({
            'symbol': order['symbol'],
            'close': price_sequence['nor_close'].to_numpy(),
            'high': price_sequence['nor_high'].to_numpy(),
            'low': price_sequence['nor_low'].to_numpy(),
            'pos': np.array(positions, dtype=int),
            'time': order_time,
        })
        
        if str(order_type).lower() == 'buy':
            buy_frames.append(order_df)
            collected_buy += 1
        elif str(order_type).lower() == 'sell':
            sell_frames.append(order_df)
            collected_sell += 1
        else:
            print(f"Warning: Unknown order type '{order_type}' for order at {order_time}")
    
    # Concatenate once for performance
    buy_df = pd.concat(buy_frames, ignore_index=True) if buy_frames else pd.DataFrame(columns=['symbol','close','high','low','pos','time'])
    sell_df = pd.concat(sell_frames, ignore_index=True) if sell_frames else pd.DataFrame(columns=['symbol','close','high','low','pos','time'])

    print(f"Collected sequences - buy: {collected_buy}, sell: {collected_sell}; skipped (edge): {skipped_edge}, skipped (no match): {skipped_nomatch}")
    if not buy_df.empty:
        print("Buy rows by symbol:\n", buy_df['symbol'].value_counts())
    if not sell_df.empty:
        print("Sell rows by symbol:\n", sell_df['symbol'].value_counts())
    
    return buy_df, sell_df


def plot_line_df(df, x_col, y_col, title, xlabel, ylabel, output_path):
    plot = lineplot(data=df, x=x_col, y=y_col, hue='symbol', errorbar='sd')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print("Plot saved to: ", output_path)


def plot_six_panel(
    buy_df: pd.DataFrame,
    sell_df: pd.DataFrame,
    output_path: str,
    xlim: tuple = (-15, 25),
    ylim: tuple = (0.95, 1.05),
    figsize: tuple = (14, 14),
    aspect_ratio: float = 0.5
) -> None:
    """
    Plot 6 subplots (3x2):
      Col 1: Buy - close, high, low (top to bottom)
      Col 2: Sell - close, high, low (top to bottom)
    Uses seaborn lineplot with errorbar='sd'.
    """
    # Enforce per-axis aspect by deriving figure height from width
    rows, cols = 3, 2
    fig_width = figsize[0]
    fig_height = (fig_width / cols) * aspect_ratio * rows
    fig, axes = plt.subplots(rows, cols, figsize=(fig_width, fig_height), sharex=True, sharey=True)

    # Mapping for ease
    panels = [
        (buy_df,  'close', 'Buy - Normalized Close',  (0, 0)),
        (sell_df, 'close', 'Sell - Normalized Close', (0, 1)),
        (buy_df,  'high',  'Buy - Normalized High',   (1, 0)),
        (sell_df, 'high',  'Sell - Normalized High',  (1, 1)),
        (buy_df,  'low',   'Buy - Normalized Low',    (2, 0)),
        (sell_df, 'low',   'Sell - Normalized Low',   (2, 1)),
    ]

    # Fixed axis limits (configurable)
    x_min, x_max = xlim
    y_min, y_max = ylim

    for df, y_col, title, (r, c) in panels:
        ax = axes[r][c]
        if df is not None and not df.empty:
            lineplot(data=df, x='pos', y=y_col, hue='symbol', errorbar='sd', ax=ax)
        ax.set_title(title)
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.set_xlabel('Position')
        ax.set_ylabel('Normalized Price')
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("Plot saved to:", output_path)

if __name__ == "__main__":
    # Run examples
    # example_usage()
    
    # Get data from database
    start_time = 1757563200
    end_time = int(datetime.now().timestamp())
    buy_df, sell_df = get_data(start_time, end_time, symbols=['ETHUSDT', 'HBARUSDT', 'USDTUSDT'], lookback=14, lookforward=25)
    # print(buy_df[:50])
    
    # Single figure with 6 subplots (2x3)
    plot_six_panel(buy_df, sell_df, output_path='plots/ADX_EP_TREND_REVERSE_orders_2x3_panels.png')
