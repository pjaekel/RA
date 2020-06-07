import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas_datareader as data
import pandas as pd
import numpy as np
from itertools import combinations
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as scs

data = data.DataReader(['ADS.DE'],
                        'yahoo', start='2019/01/01', end='2019/12/31')['Adj Close']

data.plot()

inital_investment = 10000

rets = np.log(data / data.shift(1))
std = rets.std()
rets.plot()
#print(std)
#print(np.sqrt((variance)))
volatility = np.sqrt(rets.var()) * np.sqrt(252)
print(volatility)
print(np.sum(rets.mean()) * 252)

percs = np.array([0.01, 0.1, 1.0, 2.5, 5.0, 10.0])

VaR = scs.scoreatpercentile(inital_investment * rets, percs)

def print_var():
    print('%16s %16s' % ('Confidence Level', 'VaR'))
    print(33 * '-')
    for pair in zip(percs,VaR):
        print('%16.2f %16.3f' % (100 - pair[0], -pair[1]))

print_var()