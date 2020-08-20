import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

data1 = pd.read_excel('Daten_SIX_V4.xlsx', sheet_name = 'Gesamt', index_col ='Datum')
data1.columns = ['EXHA', 'EL49',	'EXW1', 'EXS1', 'EXXT', 'EXX7', 'ELFC', 'EXI5', 'EXV6', 'GOLD']


data1.plot()
plt.legend()
plt.title('Stock Prices over Time')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.show()

'''data2 = pd.read_excel('Daten_SIX_V4.xlsx', sheet_name = 'Gesamt', index_col ='Datum')
data2.columns = ['EL49']

data3 = pd.read_excel('Daten_SIX_V4.xlsx', sheet_name = 'Gesamt', index_col ='Datum')
data3.columns = ['EXW1']

data4 = pd.read_excel('Daten_SIX_V4.xlsx', sheet_name = 'Gesamt', index_col ='Datum')
data4.columns = ['EXS1']

data5 = pd.read_excel('Daten_SIX_V4.xlsx', sheet_name = 'Gesamt', index_col ='Datum')
data5.columns = ['EXXT']

data6 = pd.read_excel('Daten_SIX_V4.xlsx', sheet_name = 'Gesamt', index_col ='Datum')
data6.columns = ['EXX7']

data7 = pd.read_excel('Daten_SIX_V4.xlsx', sheet_name = 'Gesamt', index_col ='Datum')
data7.columns = ['ELFC']

data8 = pd.read_excel('Daten_SIX_V4.xlsx', sheet_name = 'Gesamt', index_col ='Datum')
data8.columns = ['EXI5']

data9 = pd.read_excel('Daten_SIX_V4.xlsx', sheet_name = 'Gesamt', index_col ='Datum')
data9.columns = ['EXV6']

data10 = pd.read_excel('Daten_SIX_V4.xlsx', sheet_name = 'Gesamt', index_col ='Datum')
data10.columns = ['GOLD']



rets1 = np.log(data1 / data1.shift(1))
rets2 = np.log(data2 / data2.shift(1))
rets3 = np.log(data3 / data3.shift(1))
rets4 = np.log(data4 / data4.shift(1))
rets5 = np.log(data5 / data5.shift(1))
rets6 = np.log(data6 / data6.shift(1))
rets7 = np.log(data7 / data7.shift(1))
rets8 = np.log(data8 / data8.shift(1))
rets9 = np.log(data9 / data9.shift(1))
rets10 = np.log(data10 / data10.shift(1))




last_price1 = data1["EXHA"].iloc[-1]
last_price2 = data2["EL49"].iloc[-1]
last_price3 = data3["EXW1"].iloc[-1]
last_price4 = data4["EXS1"].iloc[-1]
last_price5 = data5["EXXT"].iloc[-1]
last_price6 = data6["EXX7"].iloc[-1]
last_price7 = data7["ELFC"].iloc[-1]
last_price8 = data8["EXI5"].iloc[-1]
last_price9 = data9["EXV6"].iloc[-1]
last_price10 = data10["GOLD"].iloc[-1]


num_simulations = 3
num_days = 30

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
fig.suptitle('Monte Carlo Simulation: AAPL')
plt.plot(simulation_df)
plt.axhline(y=last_price1, color='r', linestyle='-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()'''
