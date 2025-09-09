# Create a properly formatted Markdown file from the provided backtest output

md = """# MacdZeroDual50 — Backtesting Report

_Backtested 2020-03-06 00:00:00 → 2025-09-05 00:00:00 • Max open trades: 10 • Trading Mode: Isolated Futures_

---

## Strategy Summary

| Strategy       | Trades | Avg Profit % | Total Profit (USDT) | Total Profit % | Avg Duration        | Wins | Draws | Losses | Win % | Drawdown (USDT / %) |
|----------------|--------|--------------|---------------------|----------------|---------------------|------|-------|--------|-------|---------------------|
| MacdZeroDual50 | 201    | 32.65        | 1400.664            | 700.33         | 33 days, 12:32:00   | 78   | 0     | 123    | 38.8  | 60.863 / 4.61%      |

---

## By Pair — Backtesting Report

| Pair            | Trades | Avg Profit % | Total Profit (USDT) | Total Profit % | Avg Duration        | Wins | Draws | Losses | Win % |
|-----------------|--------|--------------|---------------------|----------------|---------------------|------|-------|--------|-------|
| DOGE/USDT:USDT  | 26     | 76.74        | 399.028             | 199.51         | 29 days, 19:23:00   | 7    | 0     | 19     | 26.9  |
| BNB/USDT:USDT   | 27     | 45.41        | 241.258             | 120.63         | 43 days, 08:53:00   | 17   | 0     | 10     | 63.0  |
| ADA/USDT:USDT   | 27     | 33.81        | 182.255             | 91.13          | 32 days, 02:40:00   | 10   | 0     | 17     | 37.0  |
| BTC/USDT:USDT   | 14     | 22.75        | 156.724             | 78.36          | 44 days, 15:26:00   | 7    | 0     | 7      | 50.0  |
| ETH/USDT:USDT   | 16     | 42.32        | 135.496             | 67.75          | 30 days, 01:30:00   | 6    | 0     | 10     | 37.5  |
| TRX/USDT:USDT   | 36     | 17.04        | 122.625             | 61.31          | 35 days, 16:40:00   | 14   | 0     | 22     | 38.9  |
| XRP/USDT:USDT   | 37     | 11.75        | 86.854              | 43.43          | 26 days, 04:32:00   | 8    | 0     | 29     | 21.6  |
| SOL/USDT:USDT   | 14     | 27.26        | 75.817              | 37.91          | 36 days, 15:26:00   | 7    | 0     | 7      | 50.0  |
| PAXG/USDT:USDT  | 3      | 0.85         | 0.434               | 0.22           | 9 days, 16:00:00    | 1    | 0     | 2      | 33.3  |
| HYPE/USDT:USDT  | 1      | 0.89         | 0.174               | 0.09           | 23 days, 00:00:00   | 1    | 0     | 0      | 100   |
| **TOTAL**       | **201**| **32.65**    | **1400.664**        | **700.33**     | **33 days, 12:32:00**| **78**| **0** | **123**| **38.8** |

---

## Left Open Trades Report

| Pair            | Trades | Avg Profit % | Total Profit (USDT) | Total Profit % | Avg Duration        | Wins | Draws | Losses | Win % |
|-----------------|--------|--------------|---------------------|----------------|---------------------|------|-------|--------|-------|
| ETH/USDT:USDT   | 1      | 473.16       | 94.430              | 47.21          | 63 days, 00:00:00   | 1    | 0     | 0      | 100   |
| BNB/USDT:USDT   | 1      | 168.94       | 32.198              | 16.10          | 64 days, 00:00:00   | 1    | 0     | 0      | 100   |
| SOL/USDT:USDT   | 1      | 13.72        | 2.669               | 1.33           | 27 days, 00:00:00   | 1    | 0     | 0      | 100   |
| PAXG/USDT:USDT  | 1      | 5.19         | 0.877               | 0.44           | 9 days, 00:00:00    | 1    | 0     | 0      | 100   |
| HYPE/USDT:USDT  | 1      | 0.89         | 0.174               | 0.09           | 23 days, 00:00:00   | 1    | 0     | 0      | 100   |
| **TOTAL**       | **5**  | **132.38**   | **130.348**         | **65.17**      | **37 days, 04:48:00**| **5**| **0** | **0**  | **100**|

---

## Enter Tag Stats

| Enter Tag     | Entries | Avg Profit % | Total Profit (USDT) | Total Profit % | Avg Duration        | Wins | Draws | Losses | Win % |
|---------------|---------|--------------|---------------------|----------------|---------------------|------|-------|--------|-------|
| macd_zero_up  | 201     | 32.65        | 1400.664            | 700.33         | 33 days, 12:32:00   | 78   | 0     | 123    | 38.8  |
| **TOTAL**     | **201** | **32.65**    | **1400.664**        | **700.33**     | **33 days, 12:32:00**| **78**| **0** | **123**| **38.8** |

---

## Exit Reason Stats

| Exit Reason      | Exits | Avg Profit % | Total Profit (USDT) | Total Profit % | Avg Duration        | Wins | Draws | Losses | Win % |
|------------------|-------|--------------|---------------------|----------------|---------------------|------|-------|--------|-------|
| macd_zero_down   | 194   | 31.40        | 1308.523            | 654.26         | 33 days, 17:34:00   | 73   | 0     | 121    | 37.6  |
| force_exit       | 5     | 132.38       | 130.348             | 65.17          | 37 days, 04:48:00   | 5    | 0     | 0      | 100   |
| liquidation      | 1     | -89.97       | -17.966             | -8.98          | 3 days, 00:00:00    | 0    | 0     | 1      | 0     |
| stop_loss        | 1     | -101.16      | -20.240             | -10.12         | 5 days, 00:00:00    | 0    | 0     | 1      | 0     |
| **TOTAL**        | **201**| **32.65**   | **1400.664**        | **700.33**     | **33 days, 12:32:00**| **78**| **0** | **123**| **38.8** |

---

## Mixed Tag Stats (Enter × Exit)

| Enter Tag     | Exit Reason    | Trades | Avg Profit % | Total Profit (USDT) | Total Profit % | Avg Duration        | Wins | Draws | Losses | Win % |
|---------------|----------------|--------|--------------|---------------------|----------------|---------------------|------|-------|--------|-------|
| macd_zero_up  | macd_zero_down | 194    | 31.40        | 1308.523            | 654.26         | 33 days, 17:34:00   | 73   | 0     | 121    | 37.6  |
| macd_zero_up  | force_exit     | 5      | 132.38       | 130.348             | 65.17          | 37 days, 04:48:00   | 5    | 0     | 0      | 100   |
| macd_zero_up  | liquidation    | 1      | -89.97       | -17.966             | -8.98          | 3 days, 00:00:00    | 0    | 0     | 1      | 0     |
| macd_zero_up  | stop_loss      | 1      | -101.16      | -20.240             | -10.12         | 5 days, 00:00:00    | 0    | 0     | 1      | 0     |
| **TOTAL**     |                | **201**| **32.65**    | **1400.664**        | **700.33**     | **33 days, 12:32:00**| **78**| **0** | **123**| **38.8** |

---

## Summary Metrics

| Metric                         | Value                           |
|--------------------------------|---------------------------------|
| Backtesting from               | 2020-03-06 00:00:00             |
| Backtesting to                 | 2025-09-05 00:00:00             |
| Trading Mode                   | Isolated Futures                |
| Max open trades                | 10                              |
| Total/Daily Avg Trades         | 201 / 0.1                       |
| Starting balance               | 200 USDT                        |
| Final balance                  | 1600.664 USDT                   |
| Absolute profit                | 1400.664 USDT                   |
| Total profit %                 | 700.33%                         |
| CAGR %                         | 45.92%                          |
| Sortino                        | 5.16                            |
| Sharpe                         | 0.45                            |
| Calmar                         | 144.51                          |
| SQN                            | 3.32                            |
| Profit factor                  | 6.45                            |
| Expectancy (Ratio)             | 6.97 (3.33)                     |
| Avg. daily profit              | 0.697 USDT                      |
| Avg. stake amount              | 23.699 USDT                     |
| Total trade volume             | 15870.055 USDT                  |
| Best Pair                      | DOGE/USDT:USDT 199.51%          |
| Worst Pair                     | HYPE/USDT:USDT 0.09%            |
| Best trade                     | DOGE/USDT:USDT 1590.21%         |
| Worst trade                    | DOGE/USDT:USDT -101.16%         |
| Best day                       | 318.171 USDT                    |
| Worst day                      | -20.24 USDT                     |
| Days win/draw/lose             | 67 / 1758 / 108                 |
| Min/Max/Avg. Duration Winners  | 9d 00:00 / 166d 00:00 / 62d 14:09 |
| Min/Max/Avg. Duration Losers   | 1d 00:00 / 46d 00:00 / 15d 02:09  |
| Max Consecutive Wins / Losses  | 7 / 13                          |
| Rejected Entry signals         | 0                               |
| Entry/Exit Timeouts            | 0 / 0                           |
| Min balance                    | 198.972 USDT                    |
| Max balance                    | 1600.664 USDT                   |
| Max % of account underwater    | 5.22%                           |
| Absolute drawdown              | 60.863 USDT (4.61%)             |
| Drawdown duration              | 114 days 00:00:00               |
| Profit at drawdown start       | 1120.6 USDT                     |
| Profit at drawdown end         | 1059.736 USDT                   |
| Drawdown start                 | 2025-02-06 00:00:00             |
| Drawdown end                   | 2025-05-31 00:00:00             |
| Market change                  | 1689.39%                        |

---
"""

with open("/mnt/data/proper.md", "w", encoding="utf-8") as f:
    f.write(md)

"/mnt/data/proper.md"
