import numpy as np
import pandas as pd
import datetime as dt

from pylab import mpl, plt

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

import sys

sys.path.append('../dx')

dates = [dt.datetime(2020, 1, 1), dt.datetime(2020, 7, 1),
         dt.datetime(2021, 1, 1)]

(dates[1] - dates[0]).days / 365.

(dates[2] - dates[1]).days / 365.

fractions = [0.0, 0.5, 1.0]

from get_year_deltas import get_year_deltas

get_year_deltas(dates)

from constant_short_rate import constant_short_rate

csr = constant_short_rate('csr', 0.05)
csr.get_discount_factors(dates)
deltas = get_year_deltas(dates)
csr.get_discount_factors(deltas, dtobjects=False)


from market_environment import market_environment

me = market_environment('me_gbm', dt.datetime(2020, 1, 1))
me.add_constant('initial_value', 36.)
me.add_constant('volatility', 0.2)
me.add_constant('final_date', dt.datetime(2020, 12, 31))
me.add_constant('currency', 'EUR')
me.add_constant('frequency', 'M')
me.add_constant('paths', 10000)
me.add_curve('discount_curve', csr)
me.get_constant('volatility')
me.get_curve('discount_curve').short_rate


from sn_random_numbers import *

snrn = sn_random_numbers((2, 2, 2), antithetic=False,
                         moment_matching=False, fixed_seed=True)

round(snrn.mean(), 6)
round(snrn.std(), 6)

snrn = sn_random_numbers((2, 2, 2), antithetic=False,
                         moment_matching=True, fixed_seed=True)

round(snrn.mean(), 6)
round(snrn.std(), 6)


from dx_frame import *


me_gbm = market_environment('me_gbm', dt.datetime(2020, 1, 1))

me_gbm.add_constant('initial_value', 20000.)
me_gbm.add_constant('volatility', 0.2)
me_gbm.add_constant('final_date', dt.datetime(2020, 12, 31))
me_gbm.add_constant('currency', 'EUR')
me_gbm.add_constant('frequency', 'M')
me_gbm.add_constant('paths', 10000)

csr = constant_short_rate('csr', 0.06)

me_gbm.add_curve('discount_curve', csr)

from geometric_brownian_motion import geometric_brownian_motion

gbm = geometric_brownian_motion('gbm', me_gbm)
gbm.generate_time_gird()


paths_1 = gbm.get_instrument_values()

gbm.update(volatility=0.2)

paths_2 = gbm.get_instrument_values()

plt.figure(figsize=(10, 6))
p1 = plt.plot(gbm.time_grid, paths_1[:, :30], 'b')
p2 = plt.plot(gbm.time_grid, paths_2[:, :3], 'r-.')
l1 = plt.legend([p1[0], p2[0]],
                ['low volatility', 'high volatility'], loc=2)
plt.gca().add_artist(l1)
plt.xticks(rotation=0)
plt.show()
