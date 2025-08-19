# Backtest Summary

## Data:

- Symbol:
  - BTCUSDT (1h, 4h, 1d)
  - ETHUSDT (1h, 4h, 1d)
  - XRPUSDT (1h, 4h, 1d)
  - BNBUSDT (1h, 4h, 1d)
  - SOLUSDT (1h, 4h, 1d)

- Broker setting:
  - commission (trade fee): 0.2%
# TriplePatternStrategy

- Pattern: Triple top/bottom Pattern (Bullish & Bearish)
- Entry: At close price when price get over resistance / support line  - Position Size 100% of capital
- Exit Strategy:  
  - Hold for 9 periods (9p)
  - Hold for 26 periods (26p)
- Order setting:
  - Stop lost: -2%
  - Take profit: 5%
- Pattern detect setting:
  - tol: 0.01 (chênh lệch tối đa giữa 2 đỉnh)
  - min_prominence: 0.01 (khoảng lệch tối thiểu từ đỉnh đến đáy, giúp giảm nhiễu)
  - min_distance: 5 (khoảng cách nến tối thiểu giữa 2 đỉnh, giảm nhiễu)
## BNBUSDT

| Timeframe | 26p Return [%] | 26p Win Rate [%] | 26p # Trades | 26p Details | 9p Return [%] | 9p Win Rate [%] | 9p # Trades | 9p Details |
|-----------|---------------|----------------|-------------|---------|---------------|----------------|-------------|---------|
| 1d | 0.00 | N/A | 0 | [trades](./BNBUSDT/1d/TriplePatternStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/BNBUSDT/1d/TriplePatternStrategy_26p_equity_curve.html) | 0.00 | N/A | 0 | [trades](./BNBUSDT/1d/TriplePatternStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/BNBUSDT/1d/TriplePatternStrategy_9p_equity_curve.html) |
| 1h | -5.84 | 38.8 | 67 | [trades](./BNBUSDT/1h/TriplePatternStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/BNBUSDT/1h/TriplePatternStrategy_26p_equity_curve.html) | -24.60 | 33.0 | 88 | [trades](./BNBUSDT/1h/TriplePatternStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/BNBUSDT/1h/TriplePatternStrategy_9p_equity_curve.html) |
| 4h | 4.17 | 55.6 | 9 | [trades](./BNBUSDT/4h/TriplePatternStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/BNBUSDT/4h/TriplePatternStrategy_26p_equity_curve.html) | 0.42 | 54.5 | 11 | [trades](./BNBUSDT/4h/TriplePatternStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/BNBUSDT/4h/TriplePatternStrategy_9p_equity_curve.html) |

## BTCUSDT

| Timeframe | 26p Return [%] | 26p Win Rate [%] | 26p # Trades | 26p Details | 9p Return [%] | 9p Win Rate [%] | 9p # Trades | 9p Details |
|-----------|---------------|----------------|-------------|---------|---------------|----------------|-------------|---------|
| 1d | 0.00 | N/A | 0 | [trades](./BTCUSDT/1d/TriplePatternStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/BTCUSDT/1d/TriplePatternStrategy_26p_equity_curve.html) | 0.00 | N/A | 0 | [trades](./BTCUSDT/1d/TriplePatternStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/BTCUSDT/1d/TriplePatternStrategy_9p_equity_curve.html) |
| 1h | -39.92 | 23.8 | 80 | [trades](./BTCUSDT/1h/TriplePatternStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/BTCUSDT/1h/TriplePatternStrategy_26p_equity_curve.html) | -45.93 | 20.2 | 99 | [trades](./BTCUSDT/1h/TriplePatternStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/BTCUSDT/1h/TriplePatternStrategy_9p_equity_curve.html) |
| 4h | -12.44 | 18.2 | 11 | [trades](./BTCUSDT/4h/TriplePatternStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/BTCUSDT/4h/TriplePatternStrategy_26p_equity_curve.html) | -7.60 | 18.2 | 11 | [trades](./BTCUSDT/4h/TriplePatternStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/BTCUSDT/4h/TriplePatternStrategy_9p_equity_curve.html) |

## ETHUSDT

| Timeframe | 26p Return [%] | 26p Win Rate [%] | 26p # Trades | 26p Details | 9p Return [%] | 9p Win Rate [%] | 9p # Trades | 9p Details |
|-----------|---------------|----------------|-------------|---------|---------------|----------------|-------------|---------|
| 1d | 0.00 | N/A | 0 | [trades](./ETHUSDT/1d/TriplePatternStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/ETHUSDT/1d/TriplePatternStrategy_26p_equity_curve.html) | 0.00 | N/A | 0 | [trades](./ETHUSDT/1d/TriplePatternStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/ETHUSDT/1d/TriplePatternStrategy_9p_equity_curve.html) |
| 1h | -1.56 | 34.2 | 38 | [trades](./ETHUSDT/1h/TriplePatternStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/ETHUSDT/1h/TriplePatternStrategy_26p_equity_curve.html) | 8.97 | 47.5 | 40 | [trades](./ETHUSDT/1h/TriplePatternStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/ETHUSDT/1h/TriplePatternStrategy_9p_equity_curve.html) |
| 4h | 2.16 | 50.0 | 2 | [trades](./ETHUSDT/4h/TriplePatternStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/ETHUSDT/4h/TriplePatternStrategy_26p_equity_curve.html) | 0.46 | 50.0 | 2 | [trades](./ETHUSDT/4h/TriplePatternStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/ETHUSDT/4h/TriplePatternStrategy_9p_equity_curve.html) |

## SOLUSDT

| Timeframe | 26p Return [%] | 26p Win Rate [%] | 26p # Trades | 26p Details | 9p Return [%] | 9p Win Rate [%] | 9p # Trades | 9p Details |
|-----------|---------------|----------------|-------------|---------|---------------|----------------|-------------|---------|
| 1d | 0.00 | N/A | 0 | [trades](./SOLUSDT/1d/TriplePatternStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/SOLUSDT/1d/TriplePatternStrategy_26p_equity_curve.html) | 0.00 | N/A | 0 | [trades](./SOLUSDT/1d/TriplePatternStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/SOLUSDT/1d/TriplePatternStrategy_9p_equity_curve.html) |
| 1h | -0.18 | 42.4 | 33 | [trades](./SOLUSDT/1h/TriplePatternStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/SOLUSDT/1h/TriplePatternStrategy_26p_equity_curve.html) | 9.46 | 55.9 | 34 | [trades](./SOLUSDT/1h/TriplePatternStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/SOLUSDT/1h/TriplePatternStrategy_9p_equity_curve.html) |
| 4h | -4.32 | 0.0 | 2 | [trades](./SOLUSDT/4h/TriplePatternStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/SOLUSDT/4h/TriplePatternStrategy_26p_equity_curve.html) | -4.32 | 0.0 | 2 | [trades](./SOLUSDT/4h/TriplePatternStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/SOLUSDT/4h/TriplePatternStrategy_9p_equity_curve.html) |

## XRPUSDT

| Timeframe | 26p Return [%] | 26p Win Rate [%] | 26p # Trades | 26p Details | 9p Return [%] | 9p Win Rate [%] | 9p # Trades | 9p Details |
|-----------|---------------|----------------|-------------|---------|---------------|----------------|-------------|---------|
| 1d | 0.00 | N/A | 0 | [trades](./XRPUSDT/1d/TriplePatternStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/XRPUSDT/1d/TriplePatternStrategy_26p_equity_curve.html) | 0.00 | N/A | 0 | [trades](./XRPUSDT/1d/TriplePatternStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/XRPUSDT/1d/TriplePatternStrategy_9p_equity_curve.html) |
| 1h | 3.19 | 42.9 | 49 | [trades](./XRPUSDT/1h/TriplePatternStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/XRPUSDT/1h/TriplePatternStrategy_26p_equity_curve.html) | -2.88 | 40.7 | 54 | [trades](./XRPUSDT/1h/TriplePatternStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/XRPUSDT/1h/TriplePatternStrategy_9p_equity_curve.html) |
| 4h | -0.55 | 33.3 | 3 | [trades](./XRPUSDT/4h/TriplePatternStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/XRPUSDT/4h/TriplePatternStrategy_26p_equity_curve.html) | -0.55 | 33.3 | 3 | [trades](./XRPUSDT/4h/TriplePatternStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/XRPUSDT/4h/TriplePatternStrategy_9p_equity_curve.html) |

# ButterflyStrategy

- Pattern: Butterfly Pattern (Bullish & Bearish)
- Entry: At close price when the pattern is detected
  - Position Size 100% of capital
- Exit Strategy:  
  - Hold for 9 periods (9p)
  - Hold for 26 periods (26p)
- Order setting:
  - Stop lost: -2%
  - Take profit: 5%
## BNBUSDT

| Timeframe | 26p Return [%] | 26p Win Rate [%] | 26p # Trades | 26p Details | 9p Return [%] | 9p Win Rate [%] | 9p # Trades | 9p Details |
|-----------|---------------|----------------|-------------|---------|---------------|----------------|-------------|---------|
| 1d | 0.00 | N/A | 0 | [trades](./BNBUSDT/1d/ButterflyStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/BNBUSDT/1d/ButterflyStrategy_26p_equity_curve.html) | 0.00 | N/A | 0 | [trades](./BNBUSDT/1d/ButterflyStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/BNBUSDT/1d/ButterflyStrategy_9p_equity_curve.html) |
| 1h | 0.04 | 50.0 | 2 | [trades](./BNBUSDT/1h/ButterflyStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/BNBUSDT/1h/ButterflyStrategy_26p_equity_curve.html) | 0.61 | 50.0 | 2 | [trades](./BNBUSDT/1h/ButterflyStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/BNBUSDT/1h/ButterflyStrategy_9p_equity_curve.html) |
| 4h | 4.36 | 100.0 | 1 | [trades](./BNBUSDT/4h/ButterflyStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/BNBUSDT/4h/ButterflyStrategy_26p_equity_curve.html) | 2.22 | 100.0 | 1 | [trades](./BNBUSDT/4h/ButterflyStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/BNBUSDT/4h/ButterflyStrategy_9p_equity_curve.html) |

## BTCUSDT

| Timeframe | 26p Return [%] | 26p Win Rate [%] | 26p # Trades | 26p Details | 9p Return [%] | 9p Win Rate [%] | 9p # Trades | 9p Details |
|-----------|---------------|----------------|-------------|---------|---------------|----------------|-------------|---------|
| 1d | 0.00 | N/A | 0 | [trades](./BTCUSDT/1d/ButterflyStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/BTCUSDT/1d/ButterflyStrategy_26p_equity_curve.html) | 0.00 | N/A | 0 | [trades](./BTCUSDT/1d/ButterflyStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/BTCUSDT/1d/ButterflyStrategy_9p_equity_curve.html) |
| 1h | 0.00 | N/A | 0 | [trades](./BTCUSDT/1h/ButterflyStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/BTCUSDT/1h/ButterflyStrategy_26p_equity_curve.html) | 0.00 | N/A | 0 | [trades](./BTCUSDT/1h/ButterflyStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/BTCUSDT/1h/ButterflyStrategy_9p_equity_curve.html) |
| 4h | 0.00 | N/A | 0 | [trades](./BTCUSDT/4h/ButterflyStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/BTCUSDT/4h/ButterflyStrategy_26p_equity_curve.html) | 0.00 | N/A | 0 | [trades](./BTCUSDT/4h/ButterflyStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/BTCUSDT/4h/ButterflyStrategy_9p_equity_curve.html) |

## ETHUSDT

| Timeframe | 26p Return [%] | 26p Win Rate [%] | 26p # Trades | 26p Details | 9p Return [%] | 9p Win Rate [%] | 9p # Trades | 9p Details |
|-----------|---------------|----------------|-------------|---------|---------------|----------------|-------------|---------|
| 1d | 0.00 | N/A | 0 | [trades](./ETHUSDT/1d/ButterflyStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/ETHUSDT/1d/ButterflyStrategy_26p_equity_curve.html) | 0.00 | N/A | 0 | [trades](./ETHUSDT/1d/ButterflyStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/ETHUSDT/1d/ButterflyStrategy_9p_equity_curve.html) |
| 1h | 4.52 | 100.0 | 1 | [trades](./ETHUSDT/1h/ButterflyStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/ETHUSDT/1h/ButterflyStrategy_26p_equity_curve.html) | 2.45 | 100.0 | 1 | [trades](./ETHUSDT/1h/ButterflyStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/ETHUSDT/1h/ButterflyStrategy_9p_equity_curve.html) |
| 4h | -2.09 | 0.0 | 1 | [trades](./ETHUSDT/4h/ButterflyStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/ETHUSDT/4h/ButterflyStrategy_26p_equity_curve.html) | -2.09 | 0.0 | 1 | [trades](./ETHUSDT/4h/ButterflyStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/ETHUSDT/4h/ButterflyStrategy_9p_equity_curve.html) |

## SOLUSDT

| Timeframe | 26p Return [%] | 26p Win Rate [%] | 26p # Trades | 26p Details | 9p Return [%] | 9p Win Rate [%] | 9p # Trades | 9p Details |
|-----------|---------------|----------------|-------------|---------|---------------|----------------|-------------|---------|
| 1d | 0.00 | N/A | 0 | [trades](./SOLUSDT/1d/ButterflyStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/SOLUSDT/1d/ButterflyStrategy_26p_equity_curve.html) | 0.00 | N/A | 0 | [trades](./SOLUSDT/1d/ButterflyStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/SOLUSDT/1d/ButterflyStrategy_9p_equity_curve.html) |
| 1h | 4.52 | 100.0 | 1 | [trades](./SOLUSDT/1h/ButterflyStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/SOLUSDT/1h/ButterflyStrategy_26p_equity_curve.html) | 4.52 | 100.0 | 1 | [trades](./SOLUSDT/1h/ButterflyStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/SOLUSDT/1h/ButterflyStrategy_9p_equity_curve.html) |
| 4h | 0.00 | N/A | 0 | [trades](./SOLUSDT/4h/ButterflyStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/SOLUSDT/4h/ButterflyStrategy_26p_equity_curve.html) | 0.00 | N/A | 0 | [trades](./SOLUSDT/4h/ButterflyStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/SOLUSDT/4h/ButterflyStrategy_9p_equity_curve.html) |

## XRPUSDT

| Timeframe | 26p Return [%] | 26p Win Rate [%] | 26p # Trades | 26p Details | 9p Return [%] | 9p Win Rate [%] | 9p # Trades | 9p Details |
|-----------|---------------|----------------|-------------|---------|---------------|----------------|-------------|---------|
| 1d | 0.00 | N/A | 0 | [trades](./XRPUSDT/1d/ButterflyStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/XRPUSDT/1d/ButterflyStrategy_26p_equity_curve.html) | 0.00 | N/A | 0 | [trades](./XRPUSDT/1d/ButterflyStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/XRPUSDT/1d/ButterflyStrategy_9p_equity_curve.html) |
| 1h | 0.00 | N/A | 0 | [trades](./XRPUSDT/1h/ButterflyStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/XRPUSDT/1h/ButterflyStrategy_26p_equity_curve.html) | 0.00 | N/A | 0 | [trades](./XRPUSDT/1h/ButterflyStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/XRPUSDT/1h/ButterflyStrategy_9p_equity_curve.html) |
| 4h | 0.00 | N/A | 0 | [trades](./XRPUSDT/4h/ButterflyStrategy_26p_trades.md) [plot](https://vistia-ai.github.io/backtest/XRPUSDT/4h/ButterflyStrategy_26p_equity_curve.html) | 0.00 | N/A | 0 | [trades](./XRPUSDT/4h/ButterflyStrategy_9p_trades.md) [plot](https://vistia-ai.github.io/backtest/XRPUSDT/4h/ButterflyStrategy_9p_equity_curve.html) |

