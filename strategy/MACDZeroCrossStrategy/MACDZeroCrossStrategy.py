from freqtrade.strategy import IStrategy
from pandas import DataFrame
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib

class MACDZeroCrossStrategy(IStrategy):

    # Use a 1-day timeframe
    timeframe = '1d'

    # Minimal ROI and Stoploss (adjustable as needed)
    minimal_roi = {}
    stoploss = -0.50

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Calculate MACD
        macd = ta.MACD(dataframe)
        dataframe['macd'] = macd['macd']
        dataframe['macdsignal'] = macd['macdsignal']
        dataframe['macdhist'] = macd['macdhist']
        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Buy when MACD crosses above 0 and there is volume
        dataframe.loc[
            (
                qtpylib.crossed_above(dataframe['macd'], 0) &
                (dataframe['volume'] > 0)
            ),
            'buy'] = 1
        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Sell when MACD crosses below 0
        dataframe.loc[
            (
                qtpylib.crossed_below(dataframe['macd'], 0)
            ),
            'sell'] = 1
        return dataframe
