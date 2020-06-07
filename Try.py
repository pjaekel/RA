import numpy as np
import matplotlib as plt
import pylab as plt
import numpy.random as npr


class VaR:
    def __init__(self, initial_value, var_value):
        self.initial_value = initial_value
        self.var_value = var_value

    def calculate_future_price(self):
        return self.initial_value * self.var_value


r = VaR(100, 1.01)
b = VaR(100, 101)
print(r.calculate_future_price())
print(b.calculate_future_price())

x = 1

plt.plot(x, x + 4, '-g')
plt.show()