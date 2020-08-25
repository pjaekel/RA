import pandas as pd
import numpy as np
import scipy.optimize as sco

dates = pd.date_range('1/1/2000', periods=8)
industry = ['industry', 'industry', 'utility', 'utility', 'consumer']
symbols = ['A', 'B', 'C', 'D', 'E']
zipped = list(zip(industry, symbols))
index = pd.MultiIndex.from_tuples(zipped)

noa = len(symbols)

data = np.array([[10, 9, 10, 11, 12, 13, 14, 13],
                 [11, 11, 10, 11, 11, 12, 11, 10],
                 [10, 11, 10, 11, 12, 13, 14, 13],
                 [11, 11, 10, 11, 11, 12, 11, 11],
                 [10, 11, 10, 11, 12, 13, 14, 13]])

market_to_market_price = pd.DataFrame(data.T, index=dates, columns=index)

rets = market_to_market_price / market_to_market_price.shift(1) - 1.0
rets = rets.dropna(axis=0, how='all')

expo_factor = np.ones((5,5))
factor_covariance = market_to_market_price.cov()
delta = np.diagflat([0.088024, 0.082614, 0.084237, 0.074648,
                                 0.084237])
cov_matrix = np.dot(np.dot(expo_factor, factor_covariance),
                            expo_factor.T) + delta

def calculate_total_risk(weights, cov_matrix):
    port_var = np.dot(np.dot(weights.T, cov_matrix), weights)
    return port_var

def max_func_return(weights):
    return -np.sum(rets.mean() * weights)

# optimized return with given risk
tolerance_risk = 27
noa = market_to_market_price.shape[1]
cons = ({'type': 'eq', 'fun': lambda x:  np.sum(x) - 1},
         {'type': 'eq', 'fun': lambda x:  calculate_total_risk(x, cov_matrix) - tolerance_risk})
bnds = tuple((0, 1) for x in range(noa))
init_guess = noa * [1. / noa,]
opts_mean = sco.minimize(max_func_return, init_guess, method='SLSQP',
                       bounds=bnds, constraints=cons)


print(rets)


print(opts_mean['x'].round(3))

model = pd.DataFrame(np.array([.08,.12,.05]), index= set(industry), columns = ['strategic'])
model['tactical'] = [(.05,.41), (.2,.66), (0,.16)]

print(model)
