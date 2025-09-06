# GoldHedgeZeroMACD

**Free to use** (personal & commercial). No performance claims. Not financial advice.

## What it is

* **Trend-following futures strategy (isolated).**
* **Entries/Exits:** MACD **zero-cross** on **1D**.
* **Dynamic leverage:** Increases when the **Pearson correlation** of recent daily returns between the traded coin and **PAXG/USDT (Spot 1D)** is **negative** (gold underperforming vs crypto). Otherwise uses 1x.
* **PAXG is reference only** (not traded).
* Works well with a universe like: **BTC, ETH, SOL, XRP, BNB, DOGE, TRX, ADA**.

### Key knobs

`CC_LEN` (window, e.g. 20–30), `cc_thresh` (e.g. -0.10), `lev_max`, `lev_gamma`.
Recommended safety: `stoploss_on_exchange`, liquidation buffer, **ATR-based leverage cap**, reasonable `max_open_trades`.

---

## Also included: MACDZeroCrossStrategy

A **simpler baseline**: MACD zero-cross **without** correlation-based leverage.
Good when you want:

* a non-levered/spot-friendly reference,
* a clean benchmark to compare against GoldHedgeZeroMACD on the same pairs/timeframe.

---

## License

Free to use. If you want a formal license, add **MIT** or **Apache-2.0** to your repo.
