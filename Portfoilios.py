import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas_datareader as data
import pandas as pd

data = data.DataReader(['ADS.DE', 'ALV.DE', 'BAS.DE', 'BEI.DE', 'BAYN.DE', 'BMW.DE',
                        'CON.DE', '1COV.DE', 'DAI.DE', 'DBK.DE', 'DB1.DE', 'LHA.DE',
                        'DPW.DE', 'DTE.DE', 'EOAN.DE', 'FRE.DE', 'FME.DE', 'HEI.DE',
                        'HEN3.DE', 'IFX.DE', 'LIN.DE', 'MRK.DE', 'MTX.DE', 'MUV2.DE',
                        'RWE.DE', 'SAP.DE', 'SIE.DE', 'VOW3.DE', 'VNA.DE', 'WDI.DE'],
                       'yahoo', start='2019/01/01', end='2019/12/31')['Adj Close']

df = pd.DataFrame(data)

df.style


#for key, value in df.iteritems():
    #print(key, value)


# print(df.columns)


class Portfolio:

    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third


portfolio1 = Portfolio(df[['ADS.DE']], df[['ALV.DE']], df[['BAS.DE']])
portfolio2 = Portfolio(df[['BMW.DE']], df[['LHA.DE']], df[['BEI.DE']])

# print(portfolio1)
# print(portfolio2)

# portfolio1.first = df[['ADS.DE']]
# portfolio1.second = df[['ALV.DE']]
# portfolio1.third = df[['BAS.DE']]

# portfolio2.first = df[['BMW.DE']]
# portfolio2.second = df[['LHA.DE']]
# portfolio2.third = df[['BEI.DE']]

# print(portfolio1.first)
# print(portfolio2.first)

# print('{} {}'.format(portfolio1.first, portfolio1.second))
