import pandas_datareader as data
import numpy as np
import scipy.optimize as sco
from pylab import plt
from pandas.util.testing import assert_frame_equal
import pandas as pd



data = data.DataReader(['^GSPC'],
                       'yahoo', start='1999/01/04', end='2014/09/26')['Adj Close']
print(data)
plt.plot(data)
plt.show()

rets = np.log(data / data.shift(1))



rets.plot(figsize=(40, 16))
plt.legend(prop={"size": 20})
plt.xlabel('Date', size=20)
plt.ylabel('Log Returns', size=20)
plt.title('Figure 3', size=25)
plt.show()

df1 = data['^GSPC']

rets1 = np.log(df1 / df1.shift(1))

last_price1 = df1.iloc[-1]

num_simulations = 10000
num_days = 252

simulation_df = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = rets1.std()

    price_series = []

    price = last_price1 * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(num_days):
        if count == 252:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1

    simulation_df[x] = price_series


fig = plt.figure()
fig.suptitle('Monte Carlo Simulation')
plt.plot(simulation_df)
plt.axhline(y=last_price1, color='r', linestyle='-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()


print(simulation_df.iloc[-1])

last_values_of_Simulation = simulation_df.iloc[-1]

one_year_return = (last_values_of_Simulation-1982.849976)/1982.849976

sorted_df = one_year_return.sort_values()

list = sorted_df.values.tolist()

my_rounded_list = [ round(elem, 2) for elem in list ]

print(my_rounded_list)

plt.hist(my_rounded_list, bins=32, density=True, histtype='bar', alpha=0.5)
plt.axvline(color='r', x=np.percentile(my_rounded_list, 5))
plt.show()

x = np.percentile(list, 5)

print(x)
