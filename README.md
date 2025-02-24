# MACD Zero Cross Strategy

This is a simple trading strategy for Freqtrade based on the MACD (Moving Average Convergence Divergence) indicator crossing the zero line. It generates buy and sell signals as follows:

- **Buy Signal**: When the MACD line crosses above the zero line.
- **Sell Signal**: When the MACD line crosses below the zero line.

The strategy has been backtested on the KuCoin exchange using a 1-day timeframe. Below are the detailed results of the backtest.

## Backtest Summary

| Metric               | Value                   |
|----------------------|-------------------------|
| **Strategy**         | MACDZeroCrossStrategy   |
| **Total Trades**     | 551                     |
| **Avg Profit %**     | 25.80%                  |
| **Total Profit**     | 16,830.170 USDT         |
| **Total Profit %**   | 1,683.02%               |
| **Avg Duration**     | 30 days, 13:17:00       |
| **Win / Draw / Loss**| 196 / 0 / 355           |
| **Win Rate**         | 35.6%                   |
| **Max Drawdown**     | 4,707.004 USDT (25.57%) |

## Pairwise Backtest Results

| Pair       | Trades | Avg Profit % | Tot Profit USDT | Tot Profit % | Avg Duration         | Win / Draw / Loss | Win Rate |
|------------|--------|--------------|-----------------|--------------|----------------------|-------------------|----------|
| SUI/USDT   | 5      | 104.15%      | 1,932.020       | 193.2%       | 62 days, 0:00:00     | 2 / 0 / 3         | 40.0%    |
| ORDI/USDT  | 9      | 113.11%      | 1,729.280       | 172.93%      | 28 days, 8:00:00     | 1 / 0 / 8         | 11.1%    |
| ORAI/USDT  | 15     | 36.74%       | 1,357.888       | 135.79%      | 37 days, 9:36:00     | 7 / 0 / 8         | 46.7%    |
| KCS/USDT   | 37     | 62.79%       | 1,319.343       | 131.93%      | 30 days, 7:08:00     | 13 / 0 / 24       | 35.1%    |
| BNB/USDT   | 27     | 45.26%       | 1,002.134       | 100.21%      | 41 days, 11:33:00    | 16 / 0 / 11       | 59.3%    |
| KSM/USDT   | 20     | 76.90%       | 946.503         | 94.65%       | 39 days, 13:12:00    | 9 / 0 / 11        | 45.0%    |
| QNT/USDT   | 26     | 14.15%       | 883.987         | 88.4%        | 21 days, 0:55:00     | 9 / 0 / 17        | 34.6%    |
| HNT/USDT   | 12     | 25.07%       | 810.553         | 81.06%       | 32 days, 14:00:00    | 6 / 0 / 6         | 50.0%    |
| AVAX/USDT  | 21     | 19.77%       | 751.217         | 75.12%       | 27 days, 22:51:00    | 7 / 0 / 14        | 33.3%    |
| UNI/USDT   | 24     | 35.10%       | 723.746         | 72.37%       | 31 days, 11:00:00    | 8 / 0 / 16        | 33.3%    |
| BTC/USDT   | 36     | 17.77%       | 690.407         | 69.04%       | 36 days, 16:00:00    | 12 / 0 / 24       | 33.3%    |
| SOL/USDT   | 16     | 18.67%       | 682.214         | 68.22%       | 33 days, 6:00:00     | 5 / 0 / 11         | 31.2%    |
| TRB/USDT   | 18     | 20.49%       | 578.326         | 57.83%       | 26 days, 16:00:00    | 5 / 0 / 13         | 27.8%    |
| PENDLE/USDT| 8      | 22.89%       | 515.471         | 51.55%       | 42 days, 6:00:00     | 4 / 0 / 4          | 50.0%    |
| DOT/USDT   | 20     | 29.96%       | 502.535         | 50.25%       | 32 days, 13:12:00    | 8 / 0 / 12         | 40.0%    |
| PYR/USDT   | 22     | 15.03%       | 450.065         | 45.01%       | 26 days, 6:33:00     | 7 / 0 / 15         | 31.8%    |
| INJ/USDT   | 20     | 15.60%       | 344.329         | 34.43%       | 27 days, 1:12:00     | 6 / 0 / 14         | 30.0%    |
| FIL/USDT   | 19     | 25.76%       | 332.232         | 33.22%       | 26 days, 12:38:00    | 6 / 0 / 13         | 31.6%    |
| MKR/USDT   | 29     | 11.86%       | 322.366         | 32.24%       | 25 days, 1:39:00     | 10 / 0 / 19        | 34.5%    |
| COMP/USDT  | 24     | 13.07%       | 297.797         | 29.78%       | 29 days, 23:00:00    | 9 / 0 / 15         | 37.5%    |
| ICP/USDT   | 16     | 11.33%       | 187.423         | 18.74%       | 29 days, 1:30:00     | 4 / 0 / 12         | 25.0%    |
| ETH/USDT   | 38     | 11.14%       | 183.178         | 18.32%       | 33 days, 19:35:00    | 14 / 0 / 24        | 36.8%    |
| ETC/USDT   | 42     | 11.46%       | 126.012         | 12.6%        | 24 days, 8:00:00     | 13 / 0 / 29        | 31.0%    |
| AXS/USDT   | 16     | 5.03%        | 115.346         | 11.53%       | 26 days, 9:00:00     | 5 / 0 / 11         | 31.2%    |
| LINK/USDT  | 31     | 2.22%        | 45.797          | 4.58%        | 26 days, 5:25:00     | 10 / 0 / 21        | 32.3%    |

| **TOTAL**  | **551** | **25.80%**  | **16,830.170**  | **1,683.02%** | **30 days, 13:17:00** | **196 / 0 / 355** | **35.6%** |

## Key Notes:
- **Timeframe**: 1 day (1d).
- **Exchange**: KuCoin.
- **Strategy**: Free to use, share, and modify.

## Disclaimer:
This is not financial advice. Always conduct your own research before using any strategy.
