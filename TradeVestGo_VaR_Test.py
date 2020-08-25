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

'''df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10], axis=1)
print(df)

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
print(rets)

rets = np.log(df / df.shift(1))


weights =  [0.1, 0.1, 0.1, 0.1 ,0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
weights /= np.sum(weights)


def port_ret(weights):
    return np.sum(rets.mean() * weights) * 252
# - defining annualized portfolio return given the portfolio weights

def port_vol(weights):
    return np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))


prets = []
pvols = []
#for p in range(1):
weights = [0.1, 0.1, 0.1, 0.1 ,0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
weights /= np.sum(weights)
prets.append(port_ret(weights))
pvols.append(port_vol(weights))
prets = np.array(prets)
pvols = np.array(pvols)

print(prets)
print(pvols)



'''


rets = np.log(df1 / df1.shift(1))


last_price1 = df1.iloc[-1]
print(last_price1)

num_simulations = 1000
num_days = 252

simulation_df = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = rets.std()

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

one_year_return = (last_values_of_Simulation-last_price1)/last_price1

sorted_df = one_year_return.sort_values()

list = sorted_df.values.tolist()

plt.hist(list, bins=32, density=True, histtype='bar', alpha=0.5, color="skyblue")
plt.axvline(color='r', x=np.percentile(list, 5))
plt.show()

x = np.percentile(list, 5)

print(x)