# MACD Zero-Cross Strategy Backtest Report (2018-2025)

## ⚠️ Disclaimer
**Past performance does not guarantee future results.** This report is based on historical data and simulated trading. Market conditions can change, and results may vary.

---

## 📊 Backtesting Summary
# Strategy Summary for MACDZeroCrossStrategy.py

## Introduction
This document provides a summary of the performance of the MACDZeroCrossStrategy.py across different time frames.

## Pairing List
- [Pairing List KuCoin](https://github.com/ingpawat/Freqtrade-strategy-MACDZeroCrossStrategy/blob/main/exchange-and-pair_whitelist.json)

## Strategy Performance Across Different Time Frames with initial capital 1,000 USDT

### 6H Summary
| Strategy          | Trades | Avg Profit % | Tot Profit USDT | Tot Profit % | Avg Duration       | Loss | Win % | Drawdown USDT | Drawdown % |
|-------------------|--------|--------------|-----------------|--------------|--------------------|-------|-------|---------------|------------|
| MACDZeroCross     | 2611   | 4.09         | 1625.506        | 162.55       | 6 days, 23:31:00   | 730   | 28.0  | 218.771       | 7.73       |

### 8H Summary
| Strategy          | Trades | Avg Profit % | Tot Profit USDT | Tot Profit % | Avg Duration       | Loss | Win % | Drawdown USDT | Drawdown % |
|-------------------|--------|--------------|-----------------|--------------|--------------------|-------|-------|---------------|------------|
| MACDZeroCross     | 1904   | 5.62         | 1630.066        | 163.01       | 9 days, 10:12:00   | 542   | 28.5  | 185.794       | 9.68       |

### 12H Summary
| Strategy          | Trades | Avg Profit % | Tot Profit USDT | Tot Profit % | Avg Duration       | Loss | Win % | Drawdown USDT | Drawdown % |
|-------------------|--------|--------------|-----------------|--------------|--------------------|-------|-------|---------------|------------|
| MACDZeroCross     | 1221   | 10.20        | 1961.400        | 196.14       | 14 days, 8:38:00  | 366   | 30.0  | 210.123       | 9.94       |

### 1D Summary
| Strategy          | Trades | Avg Profit % | Tot Profit USDT | Tot Profit % | Avg Duration       | Loss | Win % | Drawdown USDT | Drawdown % |
|-------------------|--------|--------------|-----------------|--------------|--------------------|-------|-------|---------------|------------|
| MACDZeroCross     | 551    | 25.80        | 2187.793        | 218.78       | 30 days, 13:17:00 | 196   | 35.6  | 267.184       | 8.37       |

### 1W Summary
| Strategy          | Trades | Avg Profit % | Tot Profit USDT | Tot Profit % | Avg Duration       | Loss | Win % | Drawdown USDT | Drawdown % |
|-------------------|--------|--------------|-----------------|--------------|--------------------|-------|-------|---------------|------------|
| MACDZeroCross     | 75     | 67.98        | 528.294         | 52.83        | 161 days, 6:43:00 | 26    | 34.7  | 78.611        | 5.34       |

## Conclusion
The MACDZeroCrossStrategy.py demonstrates varying performance across different time frames, with the 1D time frame yielding the highest total profit in USDT. The strategy's effectiveness is evident in its ability to maintain a positive profit margin across all time frames, though the drawdown percentages indicate potential risks associated with each time frame.

## Future Improvements
- **Risk Management**: Implement more sophisticated risk management techniques to reduce drawdowns.
- **Strategy Optimization**: Consider optimizing the strategy parameters for each time frame to enhance performance.
- **Diversification**: Explore diversifying the strategy across multiple assets to mitigate risk and increase potential returns.


---


