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

data = pd.read_excel('Daten_SIX_V2.xlsx', sheet_name = 'Gesamt', index_col ='Datum')
data.columns = ['EXHA',	'EXVM',	'EL49',	'EXSA',	'EXW1', 'EXS1', 'EXXT', 'EXX7', 'EXV1', 'ELFC', 'EXI5', 'EXV6']



print(data)
symbols = ['EXHA',	'EXVM',	'EL49',	'EXSA',	'EXW1', 'EXS1', 'EXXT', 'EXX7', 'EXV1', 'ELFC', 'EXI5', 'EXV6']

''' SA-D, SA-D, UA, A-EU(600), A-EU(50), A-EU-DAX, A-USA, A-Japan, Financial(600), Financial(50), IMMO-EU	RS '''

noa = len(symbols)
#weights = np.random.random(noa)
weights = [0.1,	0.1,	0.1,	0.0505,	0.05,	0.05,	0.15,	0.05,	0.1,	0.1495,	0.05,	0.05]
weights /= np.sum(weights)

initial_investment = 100
rets = np.log(data / data.shift(1))
print("rets", rets)


'''sorted = rets.sort_values(by=['^GSPC'], ascending=True)

rets.plot.hist(bins=10, alpha=1, grid=True, density=True)
plt.axvline(color='r', )
plt.show()'''


"ANNUAL PORTFOLIO RETURN"
port_ret_annual = np.sum(rets.mean() * weights) * 252
print("annual return", port_ret_annual)

"COVARIANCE MATRIX"
cov_matrix = rets.cov()
print(cov_matrix)


avg_rets = rets.mean()
print("Average rest", avg_rets)

port_mean = avg_rets.dot(weights)
print("port mean", port_mean)


"PORTFOLIO VOLATILITY"
port_stdev = np.sqrt(weights.T.dot(cov_matrix).dot(weights))
print("stdev",port_stdev)

port_vol = np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))
print("Portfolio Volatility", port_vol)

mean_investment = (1 + port_mean) * initial_investment
print("mean investment", mean_investment)
stdev_investment = initial_investment * port_stdev

conf_level1 = 0.05

from scipy.stats import norm

cutoff1 = norm.ppf(conf_level1, mean_investment, stdev_investment)
print("cut off", cutoff1)

var_1d1 = initial_investment - cutoff1

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

#plt.show()