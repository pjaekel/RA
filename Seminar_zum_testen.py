import pandas_datareader as data
import numpy as np
import scipy.optimize as sco
from pylab import plt
from pandas.util.testing import assert_frame_equal

data = data.DataReader(['ADS.DE', 'ALV.DE', 'BAS.DE', 'BEI.DE', 'BAYN.DE', 'BMW.DE',
                        'CON.DE', '1COV.DE', 'DAI.DE', 'DBK.DE', 'DB1.DE', 'LHA.DE',
                        'DPW.DE', 'DTE.DE', 'EOAN.DE', 'FRE.DE', 'FME.DE', 'HEI.DE',
                        'HEN3.DE', 'IFX.DE', 'LIN.DE', 'MRK.DE', 'MTX.DE', 'MUV2.DE',
                        'RWE.DE', 'SAP.DE', 'SIE.DE', 'VOW3.DE', 'VNA.DE', 'WDI.DE'],
                       'yahoo', start='2019/01/01', end='2019/12/31')['Adj Close']

print(data)
data.plot()
plt.legend()
plt.title('Stock Prices over Time')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.show()

data.pct_change().mean().plot(kind='bar', figsize=(20, 12), color=['silver', 'green', 'blue'])
plt.xlabel('Stocks', size=20)
plt.ylabel('Mean of Returns', size=20)
plt.title('Figure 2', size=25)

rets = np.log(data / data.shift(1))

rets.plot(figsize=(40, 16))
plt.legend(prop={"size": 20})
plt.xlabel('Date', size=20)
plt.ylabel('Log Returns', size=20)
plt.title('Figure 3', size=25)
plt.show()

rets.corr()

print(rets.corr())

# - Correlation between asset returns of portolio

rets.cumsum().apply(np.exp).resample('1w', label='right').last().plot(figsize=(20, 12))
plt.legend(prop={"size": 20})
plt.xlabel('Date', size=20)
plt.ylabel('Cumulative Log Returns', size=20)
plt.title('Figure 4', size=25)

# - Shows the cumulative log returns over time in 1 month intervals.

# - cumsum() function is used when we want to compute the cumulative sum of array elements over a given axis

# #  Monte Carlo Simulation


symbols = ['ADS.DE', 'ALV.DE', 'BAS.DE', 'BEI.DE', 'BAYN.DE', 'BMW.DE',
           'CON.DE', '1COV.DE', 'DAI.DE', 'DBK.DE', 'DB1.DE', 'LHA.DE',
           'DPW.DE', 'DTE.DE', 'EOAN.DE', 'FRE.DE', 'FME.DE', 'HEI.DE',
           'HEN3.DE', 'IFX.DE', 'LIN.DE', 'MRK.DE', 'MTX.DE', 'MUV2.DE',
           'RWE.DE', 'SAP.DE', 'SIE.DE', 'VOW3.DE', 'VNA.DE', 'WDI.DE']

# - using 30 financial instruments for portfolio composition.

noa = len(symbols)

# - Defining the number of financial instruments
# - len() function returns the number of items in an object, here 3


weights = np.random.random(noa)
weights /= np.sum(weights)

print(weights)


# - generates three uniformly distributed random numbers betweeen 0 and 1
# - the sum of all values add up to 1

def port_ret(weights):
    return np.sum(rets.mean() * weights) * 252
# - defining annualized portfolio return given the portfolio weights

def port_vol(weights):
    return np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))
# - defining annualized portfolio volatility given the portfolio weights

prets = []
pvols = []
for p in range(500):
    weights = np.random.random(noa)
    weights /= np.sum(weights)
    prets.append(port_ret(weights))
    pvols.append(port_vol(weights))
prets = np.array(prets)
pvols = np.array(pvols)

print(prets)
# Monte Carlo simulation of portfolio weights:
# With the for loop a given number of portfolios (50000) with different weights is created. We then store the
# portfolio returns and the portfolio volatilities into the following arrays:
# - prets consists of an array of the returns of all the portfolio created.
# - pvols consists of an array of the corresponding voloatility of all the portfolio created.


plt.figure(figsize=(20, 12))
plt.scatter(pvols, prets, c=prets / pvols, marker='.', cmap='Spectral', )
plt.xlabel('Expected Volatility', size=20)
plt.ylabel('Expected Return', size=20)
plt.colorbar(label='Sharpe Ratio')
plt.title('Figure 1', size=25)
plt.show()

