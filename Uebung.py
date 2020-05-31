import warnings

import numpy.random as npr
import scipy.stats as scs

warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas_datareader as data
import numpy as np
import scipy.optimize as sco
from pylab import plt
from pandas.util.testing import assert_frame_equal

data = data.DataReader(['ADS.DE', 'ALV.DE', 'BAS.DE', 'BEI.DE', 'BAYN.DE', 'BMW.DE'],
                       'yahoo', start='2017/12/29', end='2020/01/01')['Adj Close']
data1 = data.std()
print(data1)
rets = np.log(data / data.shift(1))
rets.dropna(inplace=True)
print(rets)

symbols = ['ADS.DE', 'ALV.DE', 'BAS.DE', 'BEI.DE', 'BAYN.DE', 'BMW.DE']

noa = len(symbols)

weights = np.random.random(1)
weights /= np.sum(weights)


def port_ret(weights):
    return np.sum(rets.mean() * weights) * 252


def port_vol(weights):
    return np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))


prets = []
pvols = []
for p in range(3):
    weights = np.random.random(noa)
    weights /= np.sum(weights)
    prets.append(port_ret(weights))
    pvols.append(port_vol(weights))
prets = np.array(prets)
pvols = np.array(pvols)

print(prets)

S0 = 100
r = 0.05
sigma = 0.25
T = 30 / 365
I = 100000

ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T +
                 sigma * np.sqrt(T) * npr.standard_normal(I))

print(ST)
R_gbm = np.sort(ST - S0)

percs = [0.01, 0.1, 1., 2.5, 5.0, 10.0]
var = scs.scoreatpercentile(R_gbm, percs)
print('%16.2s %16.3s' % ('CL', 'VaR'))
print(33 * '-')
for pair in zip(percs, var):
    print('%16.2f %16.3f' % (100 - pair[0], -pair[1]))

L = 0.5

from sn_random_numbers import *

sn = sn_random_numbers((2, 2, 2), antithetic=False,
                         moment_matching=False, fixed_seed=True)

print(sn)