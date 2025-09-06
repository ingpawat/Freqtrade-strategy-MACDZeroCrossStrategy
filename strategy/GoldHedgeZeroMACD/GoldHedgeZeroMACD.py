# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional

import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
import pandas as pd
import logging
from pandas import DataFrame
from freqtrade.strategy import IStrategy
from freqtrade.strategy import IntParameter, DecimalParameter

logger = logging.getLogger(__name__)


class GoldHedgeZeroMACD(IStrategy):
    """
    MACD Zero Cross Strategy with Dynamic Leverage
    
    Logic:
      - Enter long when MACD crosses above 0
      - Exit long when MACD crosses below 0
      - Dynamic leverage based on correlation with PAXG (gold proxy)
      - Fixed stake amount per order with risk management
    """

    # Required interface version for modern Freqtrade
    INTERFACE_VERSION = 3

    # Correlation window length for PAXG correlation calculation
    # Larger = smoother & slower; smaller = more reactive & noisier
    CC_LEN: int = 7
    
    # Reference asset for correlation (gold proxy)
    REF_GOLD_SPOT: str = "PAXG/USDT:USDT"

    TRADE_PREFIXES: tuple[str, ...] = (
    "BTC/USDT:USDT",
    "ETH/USDT:USDT",
    "SOL/USDT:USDT",
    "PAXG/USDT:USDT",
    "XRP/USDT:USDT",
    "BNB/USDT:USDT",
    "DOGE/USDT:USDT",
    "TRX/USDT:USDT",
    "ADA/USDT:USDT",
    "HYPE/USDT:USDT",
)

    timeframe = '1d'
    minimal_roi = {"0": 1000}
    stoploss = -0.99
    can_short = False
    position_adjustment_enable = False
    startup_candle_count = 60  # Buffer for MACD calculation

    # Hyperopt-tunable leverage parameters (discovered via space='protection')
    lev_max: IntParameter = IntParameter(10, 30, default=20, space='protection', optimize=True)
    lev_gamma: DecimalParameter = DecimalParameter(0.5, 3.0, decimals=2, default=1.0, space='protection', optimize=True)

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        macd = ta.MACD(dataframe)
        dataframe['macd'] = macd['macd']
        dataframe['macdsignal'] = macd['macdsignal']
        dataframe['macdhist'] = macd['macdhist']
        return dataframe

    def informative_pairs(self):
        """Keep PAXG as reference for correlation"""
        pairs = []
        # Keep PAXG as reference for correlation
        pairs.append(("PAXG/USDT:USDT", self.timeframe))
        # optional fallback if you sometimes use spot for CC
        pairs.append(("PAXG/USDT", self.timeframe))
        return pairs

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """Generate long entry when MACD crosses above 0."""
        dataframe['enter_long'] = 0
        long_cond = (qtpylib.crossed_above(dataframe['macd'], 0)) & (dataframe['volume'] > 0)
        dataframe.loc[long_cond, ['enter_long', 'enter_tag']] = (1, 'macd_zero_up')
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """Exit long when MACD crosses below 0."""
        dataframe['exit_long'] = 0
        dataframe.loc[
            qtpylib.crossed_below(dataframe['macd'], 0),
            ['exit_long', 'exit_tag']
        ] = (1, 'macd_zero_down')
        return dataframe

    def custom_stake_amount(
        self,
        pair: str,
        current_time: datetime,
        current_rate: float,
        proposed_stake: float,
        min_stake: Optional[float],
        max_stake: float,
        leverage: float,
        entry_tag: Optional[str],
        side: str,
        **kwargs
    ) -> float:
        """
        Fixed stake amount per order with risk management
        """
        available = self.wallets.get_available_stake_amount()
        stake_amount = 20

        if min_stake is not None and stake_amount < min_stake:
            stake_amount = float(min_stake)
        if max_stake is not None:
            stake_amount = min(stake_amount, float(max_stake))
        stake_amount = min(stake_amount, available)

        return float(max(0.0, stake_amount))

    def _corrN(self, pair: str, ref_pair: str, n: int) -> float | None:
        """Helper to compute N-day correlation between a pair and reference pair."""
        df_a, _ = self.dp.get_analyzed_dataframe(pair=pair, timeframe=self.timeframe)
        df_b = self.dp.get_pair_dataframe(ref_pair, timeframe=self.timeframe)
        if df_a is None or df_b is None:
            return None
        a = df_a[['date', 'close']].copy()
        a['ret'] = a['close'].pct_change()
        b = df_b[['date', 'close']].copy()
        b['ret_ref'] = b['close'].pct_change()
        m = pd.merge(a[['date','ret']], b[['date','ret_ref']], on='date', how='inner').dropna()
        if len(m) < n:
            return None
        cc = m['ret'].tail(n).corr(m['ret_ref'].tail(n))
        return None if pd.isna(cc) else float(cc)

    def leverage(
            self,
            pair: str,
            current_time: datetime,
            current_rate: float,
            proposed_leverage: float,
            max_leverage: float,
            entry_tag: Optional[str],
            side: str,
            **kwargs,
    ) -> float:
        """Dynamic futures leverage based on correlation with PAXG.

        Logic:
        - For tradeable pairs: correlate with PAXG and scale leverage when correlation < 0
        - Negative correlation indicates diversification benefit, higher leverage allowed
        - PAXG itself: return 1.0x (no leverage)
        - Other pairs: return 1.0x
        """
        try:
            if not hasattr(self, 'dp') or self.dp is None:
                return 1.0

            # Skip PAXG from leverage calculation (used as reference only)
            if pair.startswith("PAXG/USDT"):
                logger.debug(f"[LEVERAGE] {pair} - PAXG is reference asset, using 1.0x leverage")
                return 1.0
                
            # Apply correlation-based leverage for tradeable pairs
            if pair.startswith(self.TRADE_PREFIXES):
                refs = ["PAXG/USDT:USDT", "PAXG/USDT"]
                cc = None
                used_ref = None
                
                # Try PAXG futures first, then spot as fallback
                for r in refs:
                    cc = self._corrN(pair, r, self.CC_LEN)
                    if cc is not None:
                        used_ref = r
                        break
                
                # Log correlation result
                if cc is None:
                    logger.warning(f"[LEVERAGE] {pair} - No correlation data available, using 1.0x leverage")
                    return 1.0
                    
                if cc >= 0:
                    logger.debug(
                        f"[LEVERAGE] {pair} - Positive correlation ({cc:.3f}) with {used_ref}, using 1.0x leverage"
                    )
                    return 1.0
                    
                # Negative correlation - calculate dynamic leverage
                if hasattr(self, "lev_max") and hasattr(self, "lev_gamma"):
                    n = min(1.0, max(0.0, -cc))  # Normalize negative correlation to [0,1]
                    lev_max_val = float(self.lev_max.value)
                    gamma = float(self.lev_gamma.value)
                    lev = 3.0 + (lev_max_val - 3.0) * (n ** gamma)
                else:
                    lev = 10.0
                    
                # Cap by exchange maximum
                if max_leverage is not None:
                    lev = min(lev, float(max_leverage))
                    
                # Log leverage decision
                logger.info(
                    f"[LEVERAGE] {pair} at {current_time.strftime('%Y-%m-%d %H:%M:%S')} | "
                    f"Negative correlation: {cc:.3f} vs {used_ref} | "
                    f"Applied leverage: {lev:.2f}x (max: {max_leverage}x) | "
                    f"Parameters: max={lev_max_val}, gamma={gamma}, window={self.CC_LEN}"
                )
                
                return float(lev)

            # Default case for non-configured pairs
            logger.debug(f"[LEVERAGE] {pair} - Not in configured pairs, using 1.0x leverage")
            return 1.0
        except Exception:
            return 1.0
