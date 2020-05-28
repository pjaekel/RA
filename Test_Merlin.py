import pandas as pd
import pandas_datareader as web
import numpy as np

symbols = ['AAPL', 'DB', 'GOOG', 'NFLX']
data = pd.DataFrame()
for sym in symbols:
    data[sym] = web.DataReader(sym, data_source='yahoo', start='1-1-09', end='31-12-20')['Adj Close']
data.columns = symbols
rets = (data / data.shift(1)) - 1  # discrete returns
rets = rets.dropna()  # drop first NA entry
print(rets)
