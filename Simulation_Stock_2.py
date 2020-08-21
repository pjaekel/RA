import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2017, 1, 3)
end = dt.datetime(2017, 11, 20)

prices = web.DataReader('AAPL', 'yahoo', start, end)['Close']


returns = prices.pct_change()

plt.plot(prices)
plt.show()




last_price = prices[-1]
print(last_price)

# Number of Simulations
num_simulations = 3
num_days = 252

simulation_df = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = returns.std()

    price_series = []

    price = last_price * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(num_days):
        if count == 252:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1

    simulation_df[x] = price_series
    print(simulation_df)
    print(simulation_df.iloc[-1])


fig = plt.figure()
fig.suptitle('Monte Carlo Simulation: AAPL')
plt.plot(simulation_df)
plt.axhline(y=last_price, color='r', linestyle='-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()


mean = simulation_df.mean(axis=1)

print(mean)

plt.plot(mean)
plt.show()