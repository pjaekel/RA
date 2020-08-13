import pandas_datareader as data
import numpy as np
import scipy.optimize as sco
from pylab import plt
from pandas.util.testing import assert_frame_equal
import pandas as pd
from scipy.stats import norm

data = data.DataReader(['AAPL'],
                       'yahoo', start='2006/01/01', end='2017/12/31')['Adj Close']


log_returns = np.log(1 + data.pct_change())

u = log_returns.mean()

var = log_returns.var()

stdev = log_returns.std()

drift = u - (0.5 * var)

t_intervals = 252

iterations = 10

Z = norm.ppf(np.random.rand(t_intervals, iterations))


daily_returns = np.exp(drift + stdev * norm.ppf(np.random.rand(t_intervals, iterations)))

S0 = data.iloc[-1]

price_list = np.zeros_like(daily_returns)

price_list[0] = S0

for t in range(1, t_intervals):

    price_list[t] = price_list[t - 1] * daily_returns[t]


plt.figure(figsize=(10,5))

plt.plot(price_list)

