import warnings

import numpy.random as npr
import scipy.stats as scs

warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas_datareader as data
import numpy as np
import scipy.optimize as sco
import matplotlib.pyplot as plt
from pandas.util.testing import assert_frame_equal
import warnings
from statistics import mean
import numpy.random as npr
import scipy.stats as scs

data = data.DataReader(['ADS.DE', 'ALV.DE', 'BAS.DE', 'BEI.DE', 'BAYN.DE', 'BMW.DE'],
                       'yahoo', start='2017/12/29', end='2020/01/01')['Adj Close']
data1 = data.std()
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


S0 = 10000
r = 0.0464
sigma = 0.0439
T = 1.0
I = 900000

ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T +
                 sigma * np.sqrt(T) * npr.standard_normal(I))

R_gbm = np.sort(ST - S0)

percs = [0.01, 0.1, 1., 2.5, 5.0, 10.0]
var = scs.scoreatpercentile(R_gbm, percs)
print('%16.2s %16.3s' % ('CL', 'VaR'))
print(33 * '-')
for pair in zip(percs, var):
    print('%16.2f %16.3f' % (100 - pair[0], -pair[1]))


sorted_ST = np.sort(ST)

plt.plot(sorted_ST)
plt.show()

splitted_array = np.split(sorted_ST, 5)
print(splitted_array)

sehr_gute_entwicklung = []
sehr_gute_entwicklung.append(splitted_array[4])
gute_entwicklung = []
gute_entwicklung.append(splitted_array[3])
mittlere_entschicklung = []
mittlere_entschicklung.append(splitted_array[2])
schlecht_entwicklung = []
schlecht_entwicklung.append(splitted_array[1])
sehr_schlecht_entwicklung = []
sehr_schlecht_entwicklung.append(splitted_array[0])


print(np.mean(sehr_gute_entwicklung))
print(np.mean(gute_entwicklung))
print(np.mean(mittlere_entschicklung))
print(np.mean(schlecht_entwicklung))
print(np.mean(sehr_schlecht_entwicklung))


