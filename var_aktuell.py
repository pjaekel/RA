import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas_datareader as data
import pandas as pd
import numpy as np
from itertools import combinations
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as scs

data = data.DataReader(['AAPL'],
                        'yahoo', start='2020/01/01', end='2020/06/11')['Adj Close']


rets = np.log(data / data.shift(1))

inital_investment = 100
d = inital_investment * rets
#print(d)
std = rets.std()
#print(std)
#print(np.sqrt((variance)))
volatility = np.sqrt(rets.var()) * np.sqrt(251)
print(volatility)
print(np.sum(rets.mean()) * 251)

r = 0.05

percs = np.array([0.01, 0.1, 1.0, 2.5, 5.0, 10.0])

var = scs.scoreatpercentile(d, percs)

def print_var():
    print('%16s %16s' % ('Confidence Level', 'VaR'))
    print(33 * '-')
    for pair in zip(percs,var):
        print('%16.2f %16.7f' % (100 - pair[0], -pair[1]))

print_var()

'''
import pandas_datareader as data
import numpy as np
import scipy.optimize as sco
from pylab import plt
from pandas.util.testing import assert_frame_equal

data = data.DataReader(['AAPL', 'V', 'PG'],
                       'yahoo', start='2019/01/01', end='2019/12/31')['Adj Close']

data_percentage_change = data.pct_change().mean()

rets = np.log(data / data.shift(1))

rets.corr()

symbols = ['AAPL', 'V', 'PG']

noa = len(symbols)

weights = np.random.random(noa)
weights /= np.sum(weights)

print(weights)

def port_ret(weights):
    return np.sum(rets.mean() * weights) * 252
# - defining annualized portfolio return given the portfolio weights

def port_vol(weights):
    return np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))
# - defining annualized portfolio volatility given the portfolio weights

prets = []
pvols = []
for p in range(1):
    weights = np.random.random(noa)
    weights /= np.sum(weights)
    prets.append(port_ret(weights))
    pvols.append(port_vol(weights))
prets = np.array(prets)
pvols = np.array(pvols)


# # Optimal Portfolios
def min_func_sharpe(weights):
    return -port_ret(weights) / port_vol(weights)


cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
# - equality constraints

bnds = tuple((0, 1) for x in range(noa))
# - bounds for the parameters of x


equal_weights = np.array(noa * [1. / noa, ])
print(equal_weights)

# - This is the starting weight of a portfolio for the minimization process. We start our iteration from here.

opts = sco.minimize(min_func_sharpe, equal_weights,
                    method='SLSQP', bounds=bnds,
                    constraints=cons)
print(opts)

r_free = 0.002

weights = opts['x'].round(2)
ret_opt = port_ret(opts['x']).round(2)
vol_opt = port_vol(opts['x']).round(2)
Sharpe = port_ret(opts['x'] - r_free) / port_vol(opts['x'])

print(weights)
print(ret_opt)
print(vol_opt)
print(Sharpe)

optv = sco.minimize(port_vol, equal_weights, method='SLSQP', bounds=bnds, constraints=cons)


weights_mvp = optv['x'].round(2)
ret_mvp = port_ret(optv['x']).round(2)
vol_mvp = port_vol(optv['x']).round(2)
sharpe_mvp = port_ret(optv['x'] - r_free) / port_vol(optv['x'])

print(weights_mvp)
print(ret_mvp)
print(vol_mvp)
print(sharpe_mvp)


# # EFFICIENT FRONTIER

cons = ({'type': 'eq', 'fun': lambda x: port_ret(x) - tret},
        {'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

# - Binding constraints for the efficient frontier.

bnds = tuple((0, 1) for x in weights)

# - sets the bounds of the weights between 0 and 1

target_rets = np.linspace(0.35, 0.72, 50)
target_vols = []
for tret in target_rets:
    res = sco.minimize(port_vol, equal_weights, method='SLSQP',
                       bounds=bnds, constraints=cons)
    target_vols.append(res['fun'])
target_vols = np.array(target_vols)

# - Basic minimization process in which we find the portfolios and the corresponding returns and volatilities that
# lie on the edge of our scatter plot and are better than the MVP in terms of risk/return ratio.


plt.figure(figsize=(20, 12))
plt.scatter(pvols, prets, c=prets / pvols, marker='.', alpha=0.5, cmap='Spectral')
plt.plot(target_vols, target_rets, 'b', lw=4.0)
plt.plot(port_vol(opts['x']), port_ret(opts['x']), 'y*', markersize=30.0, label='Optimal Portfolio')
plt.plot(port_vol(optv['x']), port_ret(optv['x']), 'r*', markersize=30.0, label='Minimum Variance Portfolio')
plt.legend(loc=0)
plt.legend(prop={"size": 30})
plt.grid(True)
plt.xlabel('Expected Volatility', size=20)
plt.ylabel('Expected Return', size=20)
plt.colorbar(label='Sharpe Ratio')
plt.title('Figure 6', size=25)

'''