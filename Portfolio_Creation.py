import warnings

import numpy.random as npr
import scipy.stats as scs

warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas_datareader as data
import numpy as np
import scipy.optimize as sco
from pylab import plt
from pandas.util.testing import assert_frame_equal

#data = data.DataReader(['CEMS.DE', 'ADS.DE', 'ALV.DE'],
                      # 'yahoo', start='2018/12/28', end='2020/01/02')['Adj Close']

a = 1
b = 2
c = 3

final_score = a + b + c


class Pro(object):

    def __init__(self, final_score, data_1):
        self.final_score = final_score
        self.data_1 = [1,1,2,3,4]

    def fuck(self, final_score):
        if final_score == 2:
            print(data)


sd = Pro()

print(sd.fuck(2))
