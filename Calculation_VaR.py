import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas_datareader as data
import numpy as np
import pandas as pd
from pylab import plt

data = pd.read_excel('Daten_SIX_V5.xlsx', sheet_name = 'Gesamt', index_col ='Datum')
data.columns = ['EXHA',	'EL49',	'Gold', 'ELFC', 'EXI5', 'EXW1', 'EXX7',	'EXS1', 'EXXT', 'EXV6']

data.pct_change().mean()
plt.plot(data)

rets = np.log(data / data.shift(1))
print(rets)
rets.corr()

rets.cumsum().apply(np.exp).resample('1w', label='right').last().plot(figsize=(20, 12))

symbols = ['EXHA',	'EL49',	'Gold', 'ELFC', 'EXI5', 'EXW1', 'EXX7',	'EXS1', 'EXXT', 'EXV6']
noa = len(symbols)

weights =[0.2, 0.2 , 0.105, 0.105  , 0.1  , 0.07 , 0.06 , 0.06 , 0.05, 0.05]
weights /= np.sum(weights)

print("SUMME DER WEIGHTS IST", np.sum(weights))

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
weights =[0.2, 0.2 , 0.105, 0.105  , 0.1  , 0.07 , 0.06 , 0.06 , 0.05, 0.05]
weights /= np.sum(weights)
prets.append(port_ret(weights))
pvols.append(port_vol(weights))
prets = np.array(prets)
pvols = np.array(pvols)


print(weights)
print("The Portfolio Return is =", prets)
print("The Portfolio Volatility is =", pvols)

portfolio_vol = pvols.item()
print(prets)
print(portfolio_vol)


#define variables for Value at risk
t = 252
confidence_interval = 1.64
portfolio_value = 100

#formular Value at Risk
var_portfolio = (portfolio_value*confidence_interval)*(portfolio_vol*np.sqrt(t/252))
print(var_portfolio)

var_percent = (var_portfolio/portfolio_value)*100

print("The Value at risk for this Portfolio =", var_percent, "%")
