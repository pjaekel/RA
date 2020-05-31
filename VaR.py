import warnings

import numpy.random as npr
import scipy.stats as scs

warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas_datareader as data
import numpy as np
import scipy.optimize as sco
from pylab import plt
from pandas.util.testing import assert_frame_equal

data = data.DataReader(['CEMS.DE', 'ADS.DE', 'ALV.DE'],
                       'yahoo', start='2018/12/28', end='2020/01/02')['Adj Close']

print(data)

correlation = data.corr()
print('Correlation:', correlation)

standard_deviation = data.std()
print('Standardabweichnung:', standard_deviation)

rets = np.log(data / data.shift(1))
rets.dropna(inplace=True)

annual_return = np.sum(rets.mean() * 1) * 252
print(rets)

print('Annual Return =', annual_return)

print(data.std())