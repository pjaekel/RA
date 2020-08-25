from typing import Optional, Any


import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

style.use('ggplot')

data = pd.read_excel('Daten_SIX_V4.xlsx', sheet_name='Gesamt', index_col='Datum')
data.columns = ['EXHA', 'EL49', 'EXW1', 'EXS1', 'EXXT', 'EXX7', 'ELFC', 'EXI5', 'EXV6', 'GOLD']

plt.plot(data)
plt.show()

df1 = data['EXHA']
df2 = data['EL49']
df3 = data['EXW1']
df4 = data['EXS1']
df5 = data['EXXT']
df6 = data['EXX7']
df7 = data['ELFC']
df8 = data['EXI5']
df9 = data['EXV6']
df10 = data['GOLD']

df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10], axis=1)
#print(df)

rets1 = np.log(df1 / df1.shift(1))
rets2 = np.log(df2 / df2.shift(1))
rets3 = np.log(df3 / df3.shift(1))
rets4 = np.log(df4 / df4.shift(1))
rets5 = np.log(df5 / df5.shift(1))
rets6 = np.log(df6 / df6.shift(1))
rets7 = np.log(df7 / df7.shift(1))
rets8 = np.log(df8 / df8.shift(1))
rets9 = np.log(df9 / df9.shift(1))
rets10 = np.log(df10 / df10.shift(1))

rets = pd.concat([rets1, rets2, rets3, rets4, rets5, rets6, rets7, rets8, rets9, rets10], axis=1)
#print(rets)

last_price1 = df1.iloc[-1]
last_price2 = df2.iloc[-1]
last_price3 = df3.iloc[-1]
last_price4 = df4.iloc[-1]
last_price5 = df5.iloc[-1]
last_price6 = df6.iloc[-1]
last_price7 = df7.iloc[-1]
last_price8 = df8.iloc[-1]
last_price9 = df9.iloc[-1]
last_price10 = df10.iloc[-1]

num_simulations = 3000
num_days = 252
simulation_df_1 = pd.DataFrame()

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

    simulation_df_1[x] = price_series

fig = plt.figure()
fig.suptitle('German 10 year Government Bond: Monte Carlo Simulation')
plt.plot(simulation_df_1)
#plt.axhline(y=last_price1*0.95, color='r', linestyle='-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()

#print(simulation_df.iloc[-1])

last_values_of_Simulation = simulation_df_1.iloc[-1]

one_year_return1 = (last_values_of_Simulation-last_price1)/last_price1

sorted_df1 = one_year_return1.sort_values()

list1 = sorted_df1.values.tolist()

plt.hist(list1, bins=32, density=True, histtype='bar', alpha=0.5)
plt.axvline(color='r', x=np.percentile(list1, 5))
plt.show()

x1 = np.percentile(list1, 5)

'''---------------------------------------------------------------------------'''
#print(x)

simulation_df_2 = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = rets2.std()

    price_series_1 = []

    price = last_price2 * (1 + np.random.normal(0, daily_vol))
    price_series_1.append(price)

    for y in range(num_days):
        if count == 252:
            break
        price = price_series_1[count] * (1 + np.random.normal(0, daily_vol))
        price_series_1.append(price)
        count += 1

    simulation_df_2[x] = price_series_1

last_values_of_Simulation = simulation_df_2.iloc[-1]

one_year_return2 = (last_values_of_Simulation-last_price2)/last_price2

sorted_df2 = one_year_return2.sort_values()

list2 = sorted_df2.values.tolist()

x2 = np.percentile(list2, 5)



'''---------------------------------------------------------------------------'''


simulation_df_3 = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = rets3.std()

    price_series = []

    price = last_price3 * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(num_days):
        if count == 252:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1

    simulation_df_3[x] = price_series

last_values_of_Simulation = simulation_df_3.iloc[-1]

one_year_return3 = (last_values_of_Simulation-last_price3)/last_price3

sorted_df3 = one_year_return3.sort_values()

list3 = sorted_df3.values.tolist()

x3 = np.percentile(list3, 5)

simulation_df_4 = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = rets4.std()

    price_series = []

    price = last_price4 * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(num_days):
        if count == 252:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1

    simulation_df_4[x] = price_series

last_values_of_Simulation = simulation_df_4.iloc[-1]

one_year_return4 = (last_values_of_Simulation-last_price4)/last_price4

sorted_df4 = one_year_return4.sort_values()

list4 = sorted_df4.values.tolist()

x4 = np.percentile(list4, 5)

simulation_df_5 = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = rets5.std()

    price_series = []

    price = last_price5 * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(num_days):
        if count == 252:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1

    simulation_df_5[x] = price_series

last_values_of_Simulation = simulation_df_5.iloc[-1]

one_year_return5 = (last_values_of_Simulation-last_price5)/last_price5

sorted_df5 = one_year_return5.sort_values()

list5 = sorted_df5.values.tolist()

x5 = np.percentile(list5, 5)

simulation_df_6 = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = rets6.std()

    price_series = []

    price = last_price6 * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(num_days):
        if count == 252:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1

    simulation_df_6[x] = price_series

last_values_of_Simulation = simulation_df_6.iloc[-1]

one_year_return6 = (last_values_of_Simulation-last_price6)/last_price6

sorted_df6 = one_year_return6.sort_values()

list6 = sorted_df6.values.tolist()

x6 = np.percentile(list6, 5)

simulation_df_7 = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = rets7.std()

    price_series = []

    price = last_price7 * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(num_days):
        if count == 252:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1

    simulation_df_7[x] = price_series

last_values_of_Simulation = simulation_df_7.iloc[-1]

one_year_return7 = (last_values_of_Simulation-last_price7)/last_price7

sorted_df7 = one_year_return7.sort_values()

list7 = sorted_df7.values.tolist()

x7 = np.percentile(list7, 5)

simulation_df_8 = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = rets8.std()

    price_series = []

    price = last_price8 * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(num_days):
        if count == 252:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1

    simulation_df_8[x] = price_series

last_values_of_Simulation = simulation_df_8.iloc[-1]

one_year_return8 = (last_values_of_Simulation-last_price8)/last_price8

sorted_df8 = one_year_return8.sort_values()

list8 = sorted_df8.values.tolist()

x8 = np.percentile(list8, 5)

simulation_df_9 = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = rets9.std()

    price_series = []

    price = last_price9 * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(num_days):
        if count == 252:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1

    simulation_df_9[x] = price_series

last_values_of_Simulation = simulation_df_9.iloc[-1]

one_year_return9 = (last_values_of_Simulation-last_price9)/last_price9

sorted_df9 = one_year_return9.sort_values()

list9 = sorted_df9.values.tolist()
print(list9)


plt.hist(list9, bins=42, stacked=True, density=True, histtype='stepfilled', orientation='vertical', align='mid', alpha=0.5)
plt.ylim(0, 3)
plt.grid(True)
plt.axvline(color='r', x=np.percentile(list9, 5))
plt.show()



x9 = np.percentile(list9, 5)

simulation_df_10 = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = rets10.std()

    price_series = []

    price = last_price10 * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(num_days):
        if count == 252:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1

    simulation_df_10[x] = price_series

last_values_of_Simulation = simulation_df_10.iloc[-1]

one_year_return10 = (last_values_of_Simulation-last_price10)/last_price10

sorted_df10 = one_year_return10.sort_values()

list10 = sorted_df10.values.tolist()

x10 = np.percentile(list10, 5)

print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
print(x7)
print(x8)
print(x9)
print(x10)

print(last_price1*0.95)

#daily_returns_simulated = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10], axis=1)
#print(df)


