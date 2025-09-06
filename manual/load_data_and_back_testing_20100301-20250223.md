1. **Download historical data**  
   Run the following command to fetch the required market data:
   ```sh
   docker-compose run --rm freqtrade download-data --timeframes 1d --prepend --timerange 20100301-20250223 
   ```

2. **Run a backtest**  
   Execute the following command to test the strategy on historical data:
   ```sh
   docker-compose run --rm freqtrade backtesting --strategy MACDZeroCrossStrategy --dry-run-wallet 100 --fee 0.001 --config user_data/config.json
   
