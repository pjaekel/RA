import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
from scipy.stats import norm

style.use('ggplot')

data = pd.read_excel('Daten_SIX_V4.xlsx', sheet_name='Gesamt', index_col='Datum')
data.columns = ['EXHA', 'EL49', 'EXW1', 'EXS1', 'EXXT', 'EXX7', 'ELFC', 'EXI5', 'EXV6', 'GOLD']

plt.plot(data)


#the following lines of code create a dataframe containing the historical data of each ETF

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

num_simulations = 5000
num_days = 252
simulation_df_1 = pd.DataFrame()

#the following lines generate monte carlo simulations, which is the basis for the value and risk
#the returns of the paths are calculated and the value of risk for each is marked in an histogram

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
fig.suptitle('Monte Carlo Simulation')
plt.plot(simulation_df_1)
plt.axhline(y=last_price1, color='r', linestyle='-')
plt.xlabel('Day')
plt.ylabel('Price')


last_values_of_Simulation = simulation_df_1.iloc[-1]

one_year_return1 = (last_values_of_Simulation-last_price1)/last_price1

sorted_df1 = one_year_return1.sort_values()

list1 = sorted_df1.values.tolist()

x1 = np.percentile(list1, 5)

plt.figure(figsize=(10,6))
plt.hist(list1, label=['EXHA'], bins=42, align='mid', rwidth=1, color='#122235')
plt.axvline(ymin=0, ymax=0.5, color='r', x=np.percentile(list1, 5))
plt.xlabel('Returns')
plt.ylabel('Number of Returns')
plt.title('EXHA')
plt.show()

'''-------------------------------------------------------------------------------------------------------'''



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
print(list5)

x5 = np.percentile(list5, 5)


plt.figure(figsize=(10,6))
plt.hist(list5, label=['EXXT'], bins=42, align='mid', rwidth=1, color='#122235')
plt.axvline( ymin=0, ymax=0.5, color='r', x=np.percentile(list5, 5))
plt.xlabel('Returns')
plt.ylabel('Number of Returns')
plt.title('EXXT')
plt.show()



