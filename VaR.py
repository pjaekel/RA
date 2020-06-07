import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas_datareader as data
import pandas as pd
import numpy as np
from itertools import combinations
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy



data = data.DataReader(['DAX.DE'],
                        'yahoo', start='2019/01/01', end='2019/12/31')['Adj Close']

symbols = ['DAX.DE']
noa = len(symbols)
weights = np.random.random(noa)
weights /= np.sum(weights)

initial_investment = 1000000
returns = np.log(data / data.shift(1))

cov_matrix = returns.cov()

avg_rets = returns.mean()

port_mean = avg_rets.dot(weights)
port_stdev = np.sqrt(weights.T.dot(cov_matrix).dot(weights))

mean_investment = (1+port_mean) * initial_investment
stdev_investment = initial_investment * port_stdev


conf_level1 = 0.05

from scipy.stats import norm

cutoff1 = norm.ppf(conf_level1, mean_investment, stdev_investment)

var_1d1 = initial_investment - cutoff1


var_array = []

num_days = int(15)

for x in range(1, num_days+1):

    var_array.append(np.round(var_1d1 * np.sqrt(x),2))

    print(str(x) + " day VaR @ 95% confidence: " + str(np.round(var_1d1 * np.sqrt(x),2)))

plt.xlabel("Day #")

plt.ylabel("Max portfolio loss (USD)")

plt.title("Max portfolio loss (VaR) over 15-day period")

plt.plot(var_array, "r")

plt.show()

returns['ADS.DE'].hist(bins=40, normed=True,histtype="stepfilled",alpha=0.5)

x = np.linspace(port_mean - 3*port_stdev, port_mean+3*port_stdev,100)

plt.plot(x, scipy.stats.norm.pdf(x, port_mean, port_stdev), "r")

plt.title("ADS.DE returns (binned) vs. normal distribution")

plt.show()