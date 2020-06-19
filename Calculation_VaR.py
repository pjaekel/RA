import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas_datareader as data
import numpy as np

from pylab import plt


data = data.DataReader(['EXV6.DE','EXI5.DE', 'T3KE.DE', 'EXXT.DE','EL49.DE', 'EXHA.DE'],
                       'yahoo', start='2018/01/01', end='2020/06/15')['Adj Close']

print(data)
data.pct_change().mean()
plt.plot(data)

rets = np.log(data / data.shift(1))

rets.corr()

print(rets.corr())


rets.cumsum().apply(np.exp).resample('1w', label='right').last().plot(figsize=(20, 12))


symbols = ['EXV6.DE','EXI5.DE', 'EXXT.DE','EL49.DE', 'EXHA.DE']

noa = len(symbols)


weights = [0.3, 0.2, 0.3, 0.1, 0.1]
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
#for p in range(1):
weights = [0.3, 0.2, 0.3, 0.1, 0.1]
weights /= np.sum(weights)
prets.append(port_ret(weights))
pvols.append(port_vol(weights))
prets = np.array(prets)
pvols = np.array(pvols)


print("The Portfolio Return is =", prets)
print("The Portfolio Volatility is =", pvols)

portfolio_vol = pvols.item()

print(portfolio_vol)

t = 252
confidence_interval = 1.64
portfolio_value = 100

var_portfolio = portfolio_value*confidence_interval*portfolio_vol*np.sqrt(t/252)
print(var_portfolio)

var_percent = (var_portfolio/portfolio_value)*100

print("The Value at risk for this Portfolio =", var_percent, "%")
