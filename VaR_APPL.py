import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas_datareader as data
import numpy as np


data = data.DataReader(['XDJP.DE', 'LCVB.DE', 'XQUE.DE', 'XAAG.DE'],
                       'yahoo', start='2017/08/01', end='2018/12/31')['Adj Close']

print(data)
data.pct_change().mean()


rets = np.log(data / data.shift(1))

rets.corr()

print(rets.corr())

# - Correlation between asset returns of portolio

rets.cumsum().apply(np.exp).resample('1w', label='right').last().plot(figsize=(20, 12))

# - Shows the cumulative log returns over time in 1 month intervals.

# - cumsum() function is used when we want to compute the cumulative sum of array elements over a given axis

# #  Monte Carlo Simulation


symbols = ['XDJP.DE', 'LCVB.DE', 'XQUE.DE', 'XAAG.DE']

# - using 30 financial instruments for portfolio composition.

noa = len(symbols)

# - Defining the number of financial instruments
# - len() function returns the number of items in an object, here 3


weights = [0.18, 0.025, 0.325, 0.47]
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
    weights = [0.18, 0.025, 0.325, 0.47]
    weights /= np.sum(weights)
    prets.append(port_ret(weights))
    pvols.append(port_vol(weights))
prets = np.array(prets)
pvols = np.array(pvols)

print(prets)
print(pvols)

portfolio_vol = pvols.item()
print(portfolio_vol)

t = 252
confidence_interval = 1.64
portfolio_value = 1000000

var_portfolio = portfolio_value*confidence_interval*portfolio_vol*np.sqrt(t/252)
print(var_portfolio)

var_percent = (var_portfolio/portfolio_value)*100

print("The Value at risk for this Portfolio =", var_percent, "%")



class Value_at_Risk(object):

    def __init__(self, portfolio_value, confidence_interval, portfolio_vol, t):
        self.portfolio_value = portfolio_value
        self.confidence_interval = confidence_interval
        self.portfolio_vol = portfolio_vol
        self.t = t

    def Var_Portfolio(self):
        self.portfolio_value = portfolio_value
        self.confidence_interval = confidence_interval
        self.portfolio_vol = portfolio_vol
        self.t = t

        return self.portfolio_value*self.confidence_interval*self.portfolio_vol*np.sqrt(self.t/252)


portfolio_1 = Value_at_Risk(1000000, 1.64, 0.15383843827689053, 252)

print(portfolio_1.Var_Portfolio())

'''

data = data.DataReader(['AAPL', 'NKE', 'GLD', 'PYPL', 'TSLA'], 'yahoo', start='2000/01/01', end='2018/12/31')['Close']
rets = np.log(data / data.shift(1))
cov_matrix = data.pct_change().apply(lambda x: np.log(1+x)).cov()
print(cov_matrix)

w = {'AAPL': 0.2,'NKE': 0.2,'GLD': 0.2,'PYPL': 0.2,'TSLA': 0.2,}
p_var = cov_matrix.mul(w, axis=0).mul(w, axis=1).sum().sum()
print(p_var)
p_sd = np.sqrt(p_var)
print(p_sd)
annual_sd = p_sd*np.sqrt(252)
print(annual_sd)




print(rets)
print(data)
print(rets.std()*np.sqrt(252))
std_rets = rets.std()*np.sqrt(252)
var_rets = (std_rets**2)
print(var_rets)

portfolio_value = 1000000
exp_volatility = std_rets
t = 21
ci = 2.33
var_appl = 0.0935
std_appl = 0.305
var_gold = 0.0092
std_gold = 0.0959
weight_aapl = 0.5
weight_gold = 0.5

covariance = (rets['AAPL'].cov(rets['GLD']))*252
print(covariance)

var = portfolio_value*ci*exp_volatility*np.sqrt(t/252)

print("The Value at risk =", var)


portfolio_exp_volatility = np.sqrt(((weight_aapl**2)*var_appl)+((weight_gold**2)*var_gold)+2*covariance*weight_aapl*
                                   weight_gold)
print(portfolio_exp_volatility)

var_portfolio = portfolio_value*ci*portfolio_exp_volatility*np.sqrt(t/252)
print(var_portfolio)

'AAPL', 'NKE', 'GLD', 'PYPL', 'TSLA'
'''