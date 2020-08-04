import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas_datareader as data
import numpy as np

from pylab import plt

data = data.DataReader(['EXV6.DE', 'EXI5.DE', 'EXXT.DE', 'EL49.DE', 'EXHA.DE'],
                           'yahoo', start='2018/01/01', end='2020/06/15')['Adj Close']

rets = np.log(data / data.shift(1))

class Create_Portfolio(object):

    def __init__(self, data, weight_1, weight_2, weight_3, weight_4, weight_5):


    def port_ret(weights):
        return np.sum(rets.mean() * weights) * 252


