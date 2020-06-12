import numpy as np
import pandas as pd

marius = pd.DataFrame([1,2,4,5,6,7,8,4,2,4,5,6,7,9,7,6,4,2,4,5,6,9])
tim = [5,2,5,6,5,3,2,3,4,5,7,7,5,4,3,3,6,7,8,9,0,3]
pit = [3,1,2,4,5,6,7,8,9,7,6,4,5,6,7,6,4,3,4,5,6,6]


rets_marius = np.log(marius / marius.shift(1))
clean = rets_marius.dropna()
#rets_tim = np.log(tim / tim.shift(1))
#rets_pit = np.log(pit / pit.shift(1))

rets_marius_1 = clean.to_numpy()
print(rets_marius_1)

def port_ret():
    return np.sum(clean.mean() * 252)
# - defining annualized portfolio return given the portfolio weights

print(np.sum(rets_marius_1.mean()*21))

