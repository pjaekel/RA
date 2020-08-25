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



initial_value = 20000
log_return = 0.06367934
t = 31
sigma = 0.010540465
c_company = 0.0030
c_etf = 0.0019
log_return_net = log_return - c_company - c_etf
alpha_95 = 1.64
alpha_50 = 0.00
alpha_05 = -1.64


final_value_95 = np.exp(np.log(initial_value) + t * log_return_net + (np.sqrt(t) * sigma * alpha_95))
print('Gute Entwicklung =', final_value_95)

final_value_50 = np.exp(np.log(initial_value) + t * log_return_net + (np.sqrt(t) * sigma * alpha_50))
print('Mittlere Entwicklung =', final_value_50)

final_value_05 = np.exp(np.log(initial_value) + t * log_return_net + (np.sqrt(t) * sigma * alpha_05))
print('Schlechte Entwicklung =', final_value_05)

gute = []
for t in range(31):
    gute.append(np.exp(np.log(initial_value) + t * log_return_net + (np.sqrt(t) * sigma * alpha_95)))
# plt.plot(gute)
# plt.show()

mittlere = []
for t in range(31):
    mittlere.append(np.exp(np.log(initial_value) + t * log_return_net + (np.sqrt(t) * sigma * alpha_50)))
# plt.plot(mittlere)
# plt.show()

schlechte = []
for t in range(31):
    schlechte.append(np.exp(np.log(initial_value) + t * log_return_net + (np.sqrt(t) * sigma * alpha_05)))


# plt.plot(schlechte)
# plt.show()


class dashboard(object):

    def __init__(self, initial_value, log_return, sigma, t, alpha_95, c_company, c_etf):
        self.initial_value = initial_value
        self.log_return = log_return
        self.sigma = sigma
        self.alpha_95 = alpha_95
        self.alpha_50 = alpha_50
        self.alpha_05 = alpha_05
        self.t = t
        self.c_company = c_company
        self.c_etf = c_etf

    def net_return(self):
        self.log_return = log_return
        self.c_company = c_company
        self.c_etf = c_etf

        return self.log_return - (self.c_company + c_etf)

    def good_development(self):
        net_return = self.net_return()
        self.initial_value = initial_value
        self.sigma = sigma
        self.alpha_95 = alpha_95
        good = []
        for t in range(31):
            good.append(np.exp(np.log(initial_value) + t * net_return + (np.sqrt(t) * sigma * alpha_95)))

        return good

    def middle_development(self):
        net_return = self.net_return()
        self.initial_value = initial_value
        self.sigma = sigma
        self.alpha_50 = alpha_50
        middle = []
        for t in range(31):
            middle.append(np.exp(np.log(initial_value) + t * net_return + (np.sqrt(t) * sigma * alpha_50)))

        return middle

    def bad_development(self):
        net_return = self.net_return()
        self.initial_value = initial_value
        self.sigma = sigma
        self.alpha_05 = alpha_05
        bad = []
        for t in range(31):
            bad.append(np.exp(np.log(initial_value) + t * net_return + (np.sqrt(t) * sigma * alpha_05)))

        return bad


good = dashboard(20000, 0.06367934, 0.010540465, 31, 1.64, 0.003, 0.0019)
middle = dashboard(20000, 0.06367934, 0.010540465, 31, 0.00, 0.003, 0.0019)
bad = dashboard(20000, 0.06367934, 0.010540465, 31, -1.64, 0.003, 0.0019)


good_plot = good.good_development()
middle_plot = middle.middle_development()
bad_plot = bad.bad_development()
print(bad_plot)
print(middle_plot)
print(good_plot)


fig, ax = plt.subplots()
ax.set_xlabel('Years')
ax.plot(good_plot, color='blue')
ax.plot(middle_plot, color='red')
ax.plot(bad_plot, color='black')
ax.grid(True)
plt.ylabel('Portfolio Value')
plt.show()

