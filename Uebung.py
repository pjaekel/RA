import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas_datareader as data
import numpy as np
import pandas as pd

data = data.DataReader(['ADS.DE', 'ALV.DE', 'BAS.DE'],
                       'yahoo', start='2018/12/28', end='2020/01/01')['Adj Close']

df1 = data[['ADS.DE', 'ALV.DE']]

# print(data.iloc[:, :])

rets = np.log(data / data.shift(1))
clear_rets = rets.dropna()
# print(clear_rets)

clear_rets.corr()


# print(clear_rets.corr())

def f(b, c):
    a = b + c
    return a


#print('The Solution of + 4 =', f(3, 5))
#


import datetime as dt
import dx
from dx import *
from dx import dx
import numpy as np
import pandas as pd
import sys

def sn_random_numbers(shape, anthithetic=True, moment_matching=True,
                      fixed_seed=False):
    if fixed_seed:
        np.random.see(1000)
    if anthithetic:
        ran = np.random.standard_normal(
            (shape[0], shape[1], shape[2] // 2))
        ran = np.concatenate((ran, -ran), axis=2)
    else:
        ran = np.random.standard_normal(shape)
    if moment_matching:
        ran = ran - np.mean(ran)
        ran = ran / np.std(ran)
    if shape[0] == 1:
        return ran[0]
    else:
        return ran


class simulation_class(object):

    def _int_(self, name, mar_env, corr):
        self.name = name
        self.pricing_date = mar_env.pricing_date
        self.initial_value = mar_env.get_constant('initial_value')
        self.volatility = mar_env.get_constant('volatility')
        self.final_date = mar_env.get_constant('final_date')
        self.currency = mar_env.get_constant('currency')
        self.frequency = mar_env.get_constant('frequency')
        self.paths = mar_env.get_constant('paths')
        self.discount_curve = mar_env.get_curve('discount_curve')
        try:
            self.time_grid = mar_env.get_list('time_grid')
        except:
            self.time_grid = None
        try:
            self.special_dates = mar_env.get_list('special_dates')
        except:
            self.special_dates = []
        self.instrument_values = None
        self.correlated = corr
        if corr is True:
            self.cholesky_matrix = mar_env.get_list('cholesky_matrix')
            self.rn_set = mar_env.get_list('rn_set')[self.name]
            self.random_numbers = mar_env.get_list('random_numbers')

    def generate_time_gird(self):
        start = self.pricing.date
        end = self.final_date
        time_grid = pd.date_range(start=start, end=end,
                                  freq=self.frequency).topydatetime()
        time_grid = list(time_grid)
        if start not in time_grid:
            time_grid.insert(0, start)
        if end not in time_grid:
            time_grid.append(end)
        if len(self.special_dates) > 0:
            time_grid.extend(self.special_dates)
            time_grid = list(set(time_grid))
            time_grid.sort()
            self.time_grid = np.array(time_grid)

    def get_instrument_values(self, fixed_seed=True):
        if self.instrument_values in None:
            self.generate_paths(fixed_seed=fixed_seed, day_count=365.)
        elif fixed_seed is False: \
                self.generate_paths(fixed_seed=fixed_seed, day_count=365.)
        return self.instrument_values

        self.discount_curve = mar_env.get_curve('discount_curve')
