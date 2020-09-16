import pandas as pd
import numpy as np
import numpy.random as npr
npr.seed(123)
from scipy.optimize import minimize

# Create a DataFrame of hypothetical returns for 5 stocks across 3 industries,
# at daily frequency over a year.  Note that these will be in decimal
# rather than numeral form. (i.e. 0.01 denotes a 1% return)


data = pd.read_excel('Daten_SIX_V5.xlsx', sheet_name = 'Gesamt', index_col ='Datum')
data.columns = ['EXHA',	'EL49',	'Gold', 'ELFC', 'EXI5', 'EXW1', 'EXX7',	'EXS1', 'EXXT', 'EXV6']
returns = np.log(data / data.shift(1))

symbols = ['EXHA',	'EL49',	'Gold', 'ELFC', 'EXI5', 'EXW1', 'EXX7',	'EXS1', 'EXXT', 'EXV6']
industry = ['EXHA'] + ['EL49'] + ['Gold'] + ['ELFC'] + ['EXI5'] + ['EXW1'] + ['EXX7'] + ['EXS1'] + ['EXXT']  + ['EXV6']

annulized_return = (1 + returns.mean()) ** 252 - 1

def logrels(returns):
    """Log of return"""
    return np.log(returns + 1)

def statistics(weights, returns):
    """
    returns : DataFrame
    pret : expected portfolio return
    pvol : expected portfolio variance
    pstd : expected portfolio standard deviation
    """

    if isinstance(weights, (tuple, list)):
        weights = np.array(weights)
    pret = np.sum(logrels(returns).mean() * weights)
    pvol = np.dot(weights.T, np.dot(logrels(returns).cov(), weights))
    pstd = np.sqrt(pvol)
    return [pret, pvol, pstd]

# The below are a few convenience functions around statistics() above, needed

def port_ret(weights, returns):
    return -1 * statistics(weights=weights, returns=returns)[0]

def port_variance(weights, returns):
    return statistics(weights=weights, returns=returns)[1]

statistics([0.1] * 10, returns)[2] * np.sqrt(252)

def mapto_constraints(returns, model):
    tactical = model['tactical'].to_dict() # values are tuple bounds
    industries = returns.columns.get_level_values(0)
    group_cons = list()
    for key in tactical:
        if isinstance(industries.get_loc('EXV6'), int):
            pos = [industries.get_loc(key)]
        else:
            pos = np.where(industries.get_loc(key))[0].tolist()
        lb = tactical[key][0]
        ub = tactical[key][1] # upper and lower bounds

        lbdict = {'type': 'ineq',
                  'fun': lambda x: np.sum(x[pos[0]:(pos[-1] + 1)]) - lb}
        ubdict = {'type': 'ineq',
                  'fun': lambda x: ub - np.sum(x[pos[0]:(pos[-1] + 1)])}
        group_cons.append(lbdict); group_cons.append(ubdict)
        
    return group_cons

def opt(returns, risk_tol, model, bounds, round=3):
    noa = len(returns.columns)
    guess = noa * [1. / noa,] # equal-weight; needed for initial guess
    bnds = bounds
    cons = [{'type': 'eq', 'fun': lambda x: np.sum(x) - 1.},
            {'type': 'ineq', 'fun': lambda x: risk_tol - port_variance(x, returns=returns)}
           ] + mapto_constraints(returns=returns, model=model)
    opt = minimize(port_ret, guess, args=(returns,), method='SLSQP', bounds=bnds,
                   constraints=cons, tol=1e-10)
    return opt.x.round(round)

model = pd.DataFrame(np.array([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]),
                     index= set(industry), columns = ['strategic'])
model['tactical'] = [(0.03, 0.25), (0.03, 0.3), (0.1, 0.2), (0.1, 0.25), (0.1, 0.2), (0.03, 0.3), (0.03, 0.3), (0.03, 0.3), (0.03, 0.2), (0.03, 0.25)]


weights_final = []

weights_final.append(opt(returns, risk_tol=port_variance([0.085] * 10, returns), model=model, bounds=list(model['tactical'])))
print(weights_final)
