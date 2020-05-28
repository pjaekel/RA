import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas_datareader as data
import pandas as pd
import numpy as np
from itertools import combinations

data = data.DataReader(['ADS.DE', 'ALV.DE', 'BAS.DE', 'BEI.DE', 'BAYN.DE', 'BMW.DE',
                        'CON.DE', '1COV.DE', 'DAI.DE', 'DBK.DE', 'DB1.DE', 'LHA.DE',
                        'DPW.DE', 'DTE.DE', 'EOAN.DE', 'FRE.DE', 'FME.DE', 'HEI.DE',
                        'HEN3.DE', 'IFX.DE', 'LIN.DE', 'MRK.DE', 'MTX.DE', 'MUV2.DE',
                        'RWE.DE', 'SAP.DE', 'SIE.DE', 'VOW3.DE', 'VNA.DE', 'WDI.DE'],
                        'yahoo', start='2019/01/01', end='2019/12/31')['Adj Close']

df = pd.DataFrame(data)



print(df[['ADS.DE','ALV.DE']])

#df1 = df.sample(frac=0.1, replace=True, random_state=1)
#print(df1)

# Printing the firs 3 columns of the DataFrame
#print(df[df.columns[1:4]])

# Splitting a DataFrame
#dfs = np.split(df, [6], axis=1)
#print(dfs[0])

#rets = np.log(data / data.shift(1))
#rets.corr()

#symbols = ['ADS.DE', 'ALV.DE', 'BAS.DE']

# - using 3 financial instruments for portfolio composition.

#noa = len(symbols)
#print(noa)

# - Defining the number of financial instruments
# - len() function returns the number of items in an object, here 3

#weights = np.random.random(noa)
#weights /= np.sum(weights)

#print(weights)
