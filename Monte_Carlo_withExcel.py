import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

data = pd.read_excel('Daten_SIX_V4.xlsx', sheet_name='Gesamt', index_col='Datum')
data.columns = ['EXHA', 'EL49', 'EXW1', 'EXS1', 'EXXT', 'EXX7', 'ELFC', 'EXI5', 'EXV6', 'GOLD']

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

print(last_price1)

num_simulations = 100
num_days = 251

simulation_df = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = rets1.std()

    price_series = []

    price = last_price1 * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(num_days):
        if count == 251:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1

    simulation_df[x] = price_series
    print(simulation_df)

fig = plt.figure()
fig.suptitle('Monte Carlo Simulation')
plt.plot(simulation_df)
plt.axhline(y=last_price1, color='r', linestyle='-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()

mean = simulation_df.mean(axis=1)

print(mean)

plt.plot(mean)
plt.show()

print(simulation_df.iloc[-1])