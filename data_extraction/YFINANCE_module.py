# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# YFINANCE MODULE
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Requirements setup 
# We import from config_API the API key for the call to the provider's server
import pandas as pd
import yfinance as yf

# Fetching function definition (fetch_YFINANCE)
# symbol: Ticker symbol (type=str, ex. "AAPL" or even "EURUSD" for exchange rate)
# start: start date (format YYYY-MM-DD, type=str, ex. "1947-01-01")
# end: end date (format YYYY-MM-DD, type=str, ex. "2025-04-01")
# (!!!) filter for frequency (3 options: daily (1d), weekly (1wk), monthly (1mo))
def fetch_YFINANCE(symbol: str, start: str, end: str, frequency: str):
# Frequency settings (1d/1wk/1mo) and progress=False to not dipslay the progress bar
    data = yf.download(symbol, start=start, end=end, interval=frequency, progress=False)
    data = data.reset_index()

# (!!!) For better readibility we drop second level index, in this case the ticker (panel data for single stocks will be handle differently)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.droplevel(1)

    data = data[["Date", "Open", "Close", "High", "Low", "Volume"]]
    return data