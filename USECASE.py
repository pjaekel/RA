from dx_frame import *
import matplotlib as plt
import datetime as dt

import numpy as np
from pylab import mpl, plt
plt.style.use('seaborn')

mpl.rcParams['font.family'] = 'serif'

import sys

sys.path.append('../dx')
me_gbm = market_environment('me_gbm', dt.datetime(2020, 1, 1))

me_gbm.add_constant('initial_value', 36.)
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
gbm.generate_time_gird()

paths_1 = gbm.get_instrument_values()
print(paths_1)

paths_2 = gbm.get_instrument_values()

plt.figure(figsize=(10, 6))
p1 = plt.plot(gbm.time.grid, paths_1[:, :10], 'b')
p2 = plt.plot(gbm.time.grid, paths_2[:, :10], 'r-.')
l1 = plt.legend([p1[0], p2[0]],
                ['low volatility', 'high volatility'], loc=2)
plt.gca().add_artist(l1)
plt.xticks(rotation=30)
plt.show()