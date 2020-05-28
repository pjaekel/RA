import pandas_datareader as data
import numpy as np
import scipy.optimize as sco
from pylab import plt
import pandas as pd

# data = data.DataReader(['AAPL', 'PG', 'V'], 'yahoo', start='2019/01/25', end='2020/01/26')['Adj Close']
# print(data.head())

import csv
with open("/Users/Pit/Documents/Uni/Master/Pro Seminar/Mappe2.csv") as csvdatei:
    csv_reader_object = csv.DictReader(csvdatei)
    for row in csv_reader_object:
        print(row)
