import pandas as pd
from collections import defaultdict

BASE_URL = "https://vistia-ai.github.io/backtest"  # change it to "." if preview local

def generate_backtest_report():
    # Read the CSV file
    df = pd.read_csv('backtest_summary.csv')
    
    # Group strategies by base strategy name
    strategies = defaultdict(list)
    
    for _, row in df.iterrows():
        strategy_full = row['_strategy']
        # Split by underscore and get the base strategy name
        base_strategy = strategy_full.split('_')[0]
        
        # Get variant (everything after first underscore)
        variant_parts = strategy_full.split('_')[1:]
        variant = '_'.join(variant_parts) if variant_parts else 'default'
        
        strategies[base_strategy].append({
            'variant': variant,
            'data': row
        })
    
    # Generate markdown content
    md_content = ("# Backtest Summary\n\n"
                  "## Data:\n\n"
                  "- Symbol:\n"
                  "  - BTCUSDT (1h, 4h, 1d)\n"
                  "  - ETHUSDT (1h, 4h, 1d)\n"
                  "  - XRPUSDT (1h, 4h, 1d)\n"
                  "  - BNBUSDT (1h, 4h, 1d)\n"
                  "  - SOLUSDT (1h, 4h, 1d)\n"
                  "\n"
                  "- Broker setting:\n"
                  "  - commission (trade fee): 0.2%\n"
    )   
    strat_info = {
        "TriplePatternStrategy": (
            "- Pattern: Triple top/bottom Pattern (Bullish & Bearish)\n"
            "- Entry: At close price when price get over resistance / support line"
            "  - Position Size 100% of capital\n"
            "- Exit Strategy:  \n"
            "  - Hold for 9 periods (9p)\n"
            "  - Hold for 26 periods (26p)\n"
            "- Order setting:\n"
            "  - Stop lost: -2%\n"
            "  - Take profit: 5%\n"
            "- Pattern detect setting:\n"
            "  - tol: 0.01 (chênh lệch tối đa giữa 2 đỉnh)\n"
            "  - min_prominence: 0.01 (khoảng lệch tối thiểu từ đỉnh đến đáy, giúp giảm nhiễu)\n"
            "  - min_distance: 5 (khoảng cách nến tối thiểu giữa 2 đỉnh, giảm nhiễu)\n"),
        "ButterflyStrategy": (
            "- Pattern: Butterfly Pattern (Bullish & Bearish)\n"
            "- Entry: At close price when the pattern is detected\n"
            "  - Position Size 100% of capital\n"
            "- Exit Strategy:  \n"
            "  - Hold for 9 periods (9p)\n"
            "  - Hold for 26 periods (26p)\n"
            "- Order setting:\n"
            "  - Stop lost: -2%\n"
            "  - Take profit: 5%\n"
        ) 
    }
    for strategy_name, variants in strategies.items():
        md_content += f"# {strategy_name}\n\n"
        md_content += strat_info.get(strategy_name, "")

        # Group all data by symbol first
        symbol_groups = defaultdict(lambda: defaultdict(list))
        for item in variants:
            symbol = item['data']['tag'].split('_')[0] if pd.notna(item['data']['tag']) else 'Unknown'
            variant = item['variant']
            symbol_groups[symbol][variant].append(item['data'])
        
        for symbol in sorted(symbol_groups.keys()):
            md_content += f"## {symbol}\n\n"
            
            # Get all variants for this symbol
            variant_data = symbol_groups[symbol]
            all_variants = sorted(variant_data.keys())
            
            # Create table header with all variants
            header = "| Timeframe |"
            separator = "|-----------|"
            
            for variant in all_variants:
                header += f" {variant} Return [%] | {variant} Win Rate [%] | {variant} # Trades | {variant} Details |"
                separator += "---------------|----------------|-------------|---------|"
            
            md_content += header + "\n"
            md_content += separator + "\n"
            
            # Get all unique timeframes for this symbol
            all_timeframes = set()
            for variant in all_variants:
                for data in variant_data[variant]:
                    timeframe = data['tag'].split('_')[1] if pd.notna(data['tag']) and len(data['tag'].split('_')) > 1 else 'N/A'
                    all_timeframes.add(timeframe)
            
            # Create rows for each timeframe
            for timeframe in sorted(all_timeframes):
                row = f"| {timeframe} |"
                
                for variant in all_variants:
                    # Find data for this timeframe and variant
                    found_data = None
                    for data in variant_data[variant]:
                        data_timeframe = data['tag'].split('_')[1] if pd.notna(data['tag']) and len(data['tag'].split('_')) > 1 else 'N/A'
                        if data_timeframe == timeframe:
                            found_data = data
                            break
                    
                    if found_data is not None:
                        return_pct = f"{found_data['Return [%]']:.2f}" if pd.notna(found_data['Return [%]']) else 'N/A'
                        win_rate = f"{found_data['Win Rate [%]']:.1f}" if pd.notna(found_data['Win Rate [%]']) else 'N/A'
                        num_trades = f"{int(found_data['# Trades'])}" if pd.notna(found_data['# Trades']) else '0'
                        
                        # Generate links to detail files
                        trades_link = f"./{symbol}/{timeframe}/{strategy_name}_{variant}_trades.md"
                        plot_link = f"{BASE_URL}/{symbol}/{timeframe}/{strategy_name}_{variant}_equity_curve.html"
                        details = f"[trades]({trades_link}) [plot]({plot_link})"
                    else:
                        return_pct = '-'
                        win_rate = '-'
                        num_trades = '-'
                        details = '-'
                    
                    row += f" {return_pct} | {win_rate} | {num_trades} | {details} |"
                
                md_content += row + "\n"
            
            md_content += "\n"
    
    # Write to markdown file
    with open('backtest_report.md', 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print("Backtest report generated successfully as 'backtest_report.md'")
    print(f"Found {len(strategies)} base strategies:")
    for strategy_name, variants in strategies.items():
        variant_names = set(item['variant'] for item in variants)
        print(f"  - {strategy_name}: {len(variant_names)} variants ({', '.join(sorted(variant_names))})")

if __name__ == "__main__":
    generate_backtest_report()
    # df = pd.read_csv('backtest_summary.csv')
    # print(df)

