
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas_datareader as data
import pandas as pd
import numpy as np
from itertools import combinations
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy
import seaborn as sns


data = pd.read_excel('Daten_SIX_V5.xlsx', sheet_name = 'GesamtEXXT', index_col ='Datum')
data.columns = ['EXXT']

symbols = ['EXXT']


initial_investment = 100
rets = np.log(data / data.shift(1))
print("rets", rets)



def port_ret(weights):
    return np.sum(rets.mean() * weights) * 252
# - defining annualized portfolio return given the portfolio weights

def port_vol(weights):
    return np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))
# - defining annualized portfolio volatility given the portfolio weights

prets = []
pvols = []
for p in range(1):
    #weights = np.random.random(noa)
    weights = [1]
    weights /= np.sum(weights)
    prets.append(port_ret(weights))
    pvols.append(port_vol(weights))
prets = np.array(prets)
pvols = np.array(pvols)

'''
print(prets)
clean_rets = rets.dropna()
print(clean_rets)

list_of_rets = clean_rets.values.tolist()

flattened = []
for sublist in list_of_rets:
    for val in sublist:
        flattened.append(val)

sorted_returns = np.sort(flattened)

plt.hist(flattened, bins=100, density=True, alpha=0.5)
plt.axvline(color='r', x= np.percentile(flattened,5))
plt.show()
'''

#weights = 1


sorted_0 = rets.sort_values(by=['EXXT'], ascending=True)
sorted_1 = sorted_0.dropna()
sorted_list = sorted_1.values.tolist()

flattened = []
for sublist in sorted_list:
    for val in sublist:
        flattened.append(val)

print(flattened)
print(len(flattened))
print(np.percentile(flattened, 5))

plt.hist(flattened, bins=18, density=True, histtype='bar', alpha=0.5)
plt.axvline(color='r', x=np.percentile(flattened, 5))
plt.show()

print(np.sum(rets.mean() * weights) * 252)
# - defining annualized portfolio return given the portfolio weights


#print(np.sqrt(np.dot(weights, np.dot(rets.cov(), weights))))
print(np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights))))
# - defining annualized portfolio volatility given the portfolio weights



#x=np.random.uniform(10,size=(1000))-5.0
#print(np.sort(x))
#print(np.percentile(x,100)) # 70th percentile


rets.plot.hist(bins=10, alpha=1, grid=True, density=True)
plt.axvline(color='r', )
#plt.show()

'''
"ANNUAL PORTFOLIO RETURN"
port_ret_annual = np.sum(rets.mean() * weights) * 252
#print("annual return", port_ret_annual)

"COVARIANCE MATRIX"
cov_matrix = rets.cov()
#print(cov_matrix)


avg_rets = rets.mean()
#print("Average rest", avg_rets)

port_mean = avg_rets.dot(weights)
#rint("port mean", port_mean)


"PORTFOLIO VOLATILITY"
port_stdev = np.sqrt(weights.T.dot(cov_matrix).dot(weights))
#print("stdev",port_stdev)

port_vol = np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))
#print("Portfolio Volatility", port_vol)

mean_investment = (1 + port_mean) * initial_investment
#print("mean investment", mean_investment)
stdev_investment = initial_investment * port_stdev

#conf_level1 = 0.05
conf_level1 = 0.95

from scipy.stats import norm

#cutoff1 = norm.ppf(conf_level1, mean_investment, stdev_investment)
cutoff1 = norm.ppf(conf_level1, mean_investment, stdev_investment)
#print("cut off", cutoff1)

print(cutoff1)

var_1d1 = initial_investment - cutoff1

print(var_1d1)

var_array = []

num_days = 252

#for x in range(1, num_days + 1):
var_array.append(np.round(var_1d1 * np.sqrt(252), 2))

print(str(252) + " day VaR @ 95% confidence: " + str(np.round(var_1d1 * np.sqrt(252), 5)))

plt.xlabel("Day #")

plt.ylabel("Max portfolio loss (USD)")

plt.title("Max portfolio loss (VaR) over 20 day period")

plt.plot(var_array, "r")


rets.hist(bins=100, density=True, histtype='stepfilled', alpha=0.5)

x = np.linspace(port_mean - 3 * port_stdev, port_mean + 3 * port_stdev, 100)

plt.plot(x, scipy.stats.norm.pdf(x, port_mean, port_stdev), "r")

plt.title("VaR")

plt.show()

'''