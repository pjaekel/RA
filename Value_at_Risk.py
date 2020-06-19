import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas_datareader as data
import numpy as np
from pylab import plt



class Value_at_Risk(object):

    def __init__(self, portfolio_value, confidence_interval, portfolio_vol, t):
        self.portfolio_value = portfolio_value
        self.confidence_interval = confidence_interval
        self.portfolio_vol = portfolio_vol
        self.t = t

    def Var_Portfolio(self):
        return self.portfolio_value*self.confidence_interval*self.portfolio_vol*np.sqrt(self.t/252)

portfolio_var_3 = Value_at_Risk(100, 1.64, 0.0186, 252)
portfolio_var_4 = Value_at_Risk(100, 1.64, 0.0222, 252)
portfolio_var_5 = Value_at_Risk(100, 1.64, 0.0258, 252)
portfolio_var_6 = Value_at_Risk(100, 1.64, 0.0295, 252)
portfolio_var_7 = Value_at_Risk(100, 1.64, 0.0331, 252)
portfolio_var_8 = Value_at_Risk(100, 1.64, 0.0367, 252)
portfolio_var_9 = Value_at_Risk(100, 1.64, 0.0403, 252)
portfolio_var_10 = Value_at_Risk(100, 1.64, 0.0439, 252)
portfolio_var_11 = Value_at_Risk(100, 1.64, 0.0475, 252)
portfolio_var_12 = Value_at_Risk(100, 1.64, 0.0512, 252)
portfolio_var_13 = Value_at_Risk(100, 1.64, 0.0548, 252)
portfolio_var_14 = Value_at_Risk(100, 1.64, 0.0584, 252)
portfolio_var_15 = Value_at_Risk(100, 1.64, 0.0620, 252)
portfolio_var_16 = Value_at_Risk(100, 1.64, 0.0656, 252)
portfolio_var_17 = Value_at_Risk(100, 1.64, 0.0693, 252)
portfolio_var_18 = Value_at_Risk(100, 1.64, 0.0729, 252)
portfolio_var_19 = Value_at_Risk(100, 1.64, 0.0765, 252)
portfolio_var_20 = Value_at_Risk(100, 1.64, 0.0801, 252)
portfolio_var_21 = Value_at_Risk(100, 1.64, 0.0837, 252)
portfolio_var_22 = Value_at_Risk(100, 1.64, 0.0874, 252)
portfolio_var_23 = Value_at_Risk(100, 1.64, 0.0910, 252)
portfolio_var_24 = Value_at_Risk(100, 1.64, 0.0947, 252)
portfolio_var_25 = Value_at_Risk(100, 1.64, 0.0983, 252)


a = portfolio_var_3.Var_Portfolio()
b = portfolio_var_4.Var_Portfolio()
c = portfolio_var_5.Var_Portfolio()
d = portfolio_var_6.Var_Portfolio()
e = portfolio_var_7.Var_Portfolio()
f = portfolio_var_8.Var_Portfolio()
g = portfolio_var_9.Var_Portfolio()
h = portfolio_var_10.Var_Portfolio()
i = portfolio_var_11.Var_Portfolio()
j = portfolio_var_12.Var_Portfolio()
k = portfolio_var_13.Var_Portfolio()
l = portfolio_var_14.Var_Portfolio()
m = portfolio_var_15.Var_Portfolio()
n = portfolio_var_16.Var_Portfolio()
o = portfolio_var_17.Var_Portfolio()
p = portfolio_var_18.Var_Portfolio()
q = portfolio_var_19.Var_Portfolio()
r = portfolio_var_20.Var_Portfolio()
s = portfolio_var_21.Var_Portfolio()
t = portfolio_var_22.Var_Portfolio()
u = portfolio_var_23.Var_Portfolio()
v = portfolio_var_24.Var_Portfolio()
w = portfolio_var_25.Var_Portfolio()

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)
print(n)
print(o)
print(p)
print(q)
print(r)
print(s)
print(t)
print(u)
print(v)
