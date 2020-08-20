import datetime
import numpy as np
from scipy.stats import norm
import pandas_datareader as data




def var_cov_var(P, c, mu, sigma):
    """
    Variance-Covariance calculation of daily Value-at-Risk
    using confidence level c, with mean of returns mu
    and standard deviation of returns sigma, on a portfolio
    of value P.
    """
    alpha = norm.ppf(1-c, mu, sigma)
    return P - P*(alpha + 1)

if __name__ == "__main__":
    start = datetime.datetime(2006, 1, 1)
    end = datetime.datetime(2009, 1, 1)

    data = data.DataReader("VOW.DE", 'yahoo', start, end)
    data["rets"] = data["Adj Close"].pct_change()

    P = 1e6   # 1,000,000 USD
    c = 0.95  # 99% confidence interval
    mu = np.mean(data["rets"])
    sigma = np.std(data["rets"])

    var = var_cov_var(P, c, mu, sigma)
    print("Value-at-Risk: $%0.2f" % var)
    print("The fucking std is", sigma)