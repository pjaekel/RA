import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

style.use('ggplot')


num_simulations = 2000
num_days = 252
simulation_df_1 = pd.DataFrame()
last_price = 10000
rets1 = 0.05816299

for x in range(num_simulations):
    count = 0
    daily_vol = rets1/15.87

    price_series = []

    price = last_price * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(num_days):
        if count == 252:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1

    simulation_df_1[x] = price_series

fig = plt.figure()
fig.suptitle('Monte Carlo Simulation 25.02.2020')
plt.plot(simulation_df_1)
#plt.axhline(y=last_price, color='r', linestyle='-')
plt.xlabel('Trading Days')
plt.ylabel('Portfolio Value')
plt.ylim(7500, 12500)
plt.show()

last_values_of_Simulation = simulation_df_1.iloc[-1]

one_year_return1 = (last_values_of_Simulation-last_price)/last_price

sorted_df1 = one_year_return1.sort_values()

list1 = sorted_df1.values.tolist()

plt.hist(list1, bins=32, density=True, histtype='bar', alpha=0.5)
plt.axvline(color='r', x=np.percentile(list1, 5))


x1 = np.percentile(list1, 5)

print(x1)