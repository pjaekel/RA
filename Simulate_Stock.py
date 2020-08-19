import numpy as np
from pylab import plt

starting_price = 100


def simulate_stock(mean, sigma):
    prices_over_time = [starting_price]
    for _ in range(50):
        previous_price = prices_over_time[-1]
        growth_factor = np.random.lognormal(mean=mean, sigma=sigma)
        prices_over_time.append(previous_price * growth_factor)
    plt.plot(prices_over_time)
    print(prices_over_time)


plt.figure(figsize=(10, 10))
for _ in range(100):
    simulate_stock(mean=0.0005, sigma=0.15)
    #simulate_stock(mean=-0.005, sigma=0.01)

plt.show()

