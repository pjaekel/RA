import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import numpy.random as npr
import scipy.stats as scs
import pandas_datareader as data
import numpy as np
import scipy.optimize as sco
import matplotlib.pyplot as plt
from pandas.util.testing import assert_frame_equal
import warnings
from statistics import mean
import numpy.random as npr
import scipy.stats as scs

initial_value = 10000
log_return = 0.0215
t = 5
sigma = 0.0186
c_company = 0.0075
c_etf = 0.0019
log_return_net = log_return - c_company - c_etf
alpha_95 = 1.64
alpha_50 = 0.00
alpha_05 = -1.64



final_value_95 = np.exp(np.log(initial_value) + t*log_return_net + (np.sqrt(t) *sigma*alpha_95))
print('Gute Entwicklung =', final_value_95)

final_value_50 = np.exp(np.log(initial_value) + t*log_return_net + (np.sqrt(t) *sigma*alpha_50))
print('Mittlere Entwicklung =', final_value_50)

final_value_05 = np.exp(np.log(initial_value) + t*log_return_net + (np.sqrt(t) *sigma*alpha_05))
print('Schlechte Entwicklung =', final_value_05)

gute = []
for t in range(30):
    gute.append(np.exp(np.log(initial_value) + t*log_return_net + (np.sqrt(t) *sigma*alpha_95)))

plt.plot(gute)
plt.show()

mittlere = []
for t in range(30):
    mittlere.append(np.exp(np.log(initial_value) + t*log_return_net + (np.sqrt(t) *sigma*alpha_50)))

schlechte = []
for t in range(30):
    schlechte.append(np.exp(np.log(initial_value) + t*log_return_net + (np.sqrt(t) *sigma*alpha_05)))
