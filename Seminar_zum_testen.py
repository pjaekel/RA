import pandas_datareader as data
import numpy as np
import scipy.optimize as sco
from pylab import plt
from pandas.util.testing import assert_frame_equal
import pandas as pd

data = pd.read_excel('Daten_SIX_V3.xlsx', sheet_name = 'Gesamt', index_col ='Datum')
data.columns = ['EXHA',	'EL49',	'EXW1', 'EXS1', 'EXXT', 'EXX7', 'ELFC', 'EXI5', 'EXV6']

print(data)
data.plot()
plt.legend()
plt.title('Stock Prices over Time')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.show()
'''
data.pct_change().mean().plot(kind='bar', figsize=(20, 12), color=['silver', 'green', 'blue'])
plt.xlabel('Stocks', size=20)
plt.ylabel('Mean of Returns', size=20)
plt.title('Figure 2', size=25)

rets = np.log(data / data.shift(1))

print(rets)

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


symbols = ['EXHA',	'EXVM',	'EL49',	'EXSA',	'EXW1', 'EXS1', 'EXXT', 'EXX7', 'EXV1', 'ELFC', 'EXI5', 'EXV6']

# - using 30 financial instruments for portfolio composition.

noa = len(symbols)

# - Defining the number of financial instruments
# - len() function returns the number of items in an object, here 3


#weights = np.random.random(noa)
#weights /= np.sum(weights)

#print(weights)


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
for p in range(1):
    weights = np.random.random(noa)
    weights /= np.sum(weights)
    prets.append(port_ret(weights))
    pvols.append(port_vol(weights))
    print("WWWWWWWWW", weights)
prets = np.array(prets)
pvols = np.array(pvols)

print("RRRRRRRRRRR", prets)
print("PPPPPPPPPPP", pvols)
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

# - Illustrates the result of the Monte Carlo Simulation
# - Scatter plot of 50000 portfolios created from the 3 underlying

# # Optimal Portfolios
def min_func_sharpe(weights):
    return -port_ret(weights) / port_vol(weights)


# - For the optimal portfolio we need to define the a function we want to minimize.
#
#
# - Since the benchmark for the optimal portfolio is the the Sharpe ratio, we define this as our function.

cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
# - equality constraints


bnds = tuple((0.0, 1) for x in range(noa))

print("BOUNDS", bnds)

# - bounds for the parameters of x


equal_weights = np.array(noa * [1. / noa, ])

# - This is the starting weight of a portfolio for the minimization process. We start our iteration from here.

opts = sco.minimize(min_func_sharpe, equal_weights, method='SLSQP', bounds=bnds, constraints=cons)
print("OOOOOOOOPTS", opts)

r_free = 0.002

weights = opts['x'].round(2)
ret_opt = port_ret(opts['x']).round(2)
vol_opt = port_vol(opts['x']).round(2)
Sharpe = port_ret(opts['x'] - r_free) / port_vol(opts['x'])

print(weights)
print(ret_opt)
print(vol_opt)
print(Sharpe)

# - Optimal Portfolio weights # - Return of the Optimal Portfolio # - Volatility of Optimal Portfolio # - Sharpe
# ratio of Optimal Portfolio (- A High Sharpe ratio is good when compared to similar portfolios or funds with lower
# returns)

optv = sco.minimize(port_vol, equal_weights, method='SLSQP', bounds=bnds, constraints=cons)

# - minimization of portfolio.
#
#
# - optv = MVP (Portfolio with the minimum variance)


weights_mvp = optv['x'].round(2)
ret_mvp = port_ret(optv['x']).round(2)
vol_mvp = port_vol(optv['x']).round(2)
sharpe_mvp = port_ret(optv['x'] - r_free) / port_vol(optv['x'])

print(weights_mvp)
print(ret_mvp)
print(vol_mvp)
print(sharpe_mvp)

# - Weights of MVP
# - Return of MVP
# - Volatility of MVP
# - Sharpe Ratio of MVP

# # EFFICIENT FRONTIER

cons = ({'type': 'eq', 'fun': lambda x: port_ret(x) - tret},
        {'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

# - Binding constraints for the efficient frontier.


bnds = tuple((0, 1) for x in weights)
bnds

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

plt.show()

# - Plotting the all the portfolios in a scatter plot by dividing the random portfolio returns by the assigned
# portfolio volatilities and plotting it with the matplot function.
#
#
# - The blue line along the scatter plot shows the efficient frontier. This line is made up of all optimal portfolios
# with a higher return than the minimum variance portfolio. All portfolios on this line show higher expected returns
# at a certain level of risk.
#
#
# - The red star indicates the minimum Variance Portfolio (MVP), which is the portfolio with the lowest volatility.
#
#
# - The yellow star indicates the optimal portfolio, which is made up of the three underlying and shows the
# portfolio on the efficient frontier with the highest Sharpe ratio (Return/Volatility), which was mentioned and
# calculated earlier in the code.

# # Sources:

# - Hilpisch, Y. (2018). Python for Finance. Sebastopol: O'Reilly Media Inc.
# - Yahoo Finance
'''