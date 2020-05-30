import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas_datareader as data
import numpy as np
import scipy.optimize as sco
from pylab import plt
from pandas.util.testing import assert_frame_equal

data = data.DataReader(['ADS.DE', 'ALV.DE', 'BAS.DE', 'BEI.DE', 'BAYN.DE', 'BMW.DE',
                        'CON.DE', '1COV.DE', 'DAI.DE', 'DBK.DE', 'DB1.DE', 'LHA.DE',
                        'DPW.DE', 'DTE.DE', 'EOAN.DE', 'FRE.DE', 'FME.DE', 'HEI.DE',
                        'HEN3.DE', 'IFX.DE', 'LIN.DE', 'MRK.DE', 'MTX.DE', 'MUV2.DE',
                        'RWE.DE', 'SAP.DE', 'SIE.DE', 'VOW3.DE', 'VNA.DE', 'WDI.DE'],
                       'yahoo', start='2019/01/01', end='2019/12/31')['Adj Close']


rets = np.log(data / data.shift(1))

symbols = ['ADS.DE', 'ALV.DE', 'BAS.DE', 'BEI.DE', 'BAYN.DE', 'BMW.DE',
           'CON.DE', '1COV.DE', 'DAI.DE', 'DBK.DE', 'DB1.DE', 'LHA.DE',
           'DPW.DE', 'DTE.DE', 'EOAN.DE', 'FRE.DE', 'FME.DE', 'HEI.DE',
           'HEN3.DE', 'IFX.DE', 'LIN.DE', 'MRK.DE', 'MTX.DE', 'MUV2.DE',
           'RWE.DE', 'SAP.DE', 'SIE.DE', 'VOW3.DE', 'VNA.DE', 'WDI.DE']

noa = len(symbols)

weights = np.random.random(1)
weights /= np.sum(weights)

def port_ret(weights):
    return np.sum(rets.mean() * weights) * 251

def port_vol(weights):
    return np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 251, weights)))

prets = []
pvols = []
for p in range(3):
    weights = np.random.random(noa)
    weights /= np.sum(weights)
    prets.append(port_ret(weights))
    pvols.append(port_vol(weights))
prets = np.array(prets)
pvols = np.array(pvols)

print(prets)