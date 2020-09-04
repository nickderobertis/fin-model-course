import random

import xlwings as xw
import pandas as pd


@xw.func
@xw.arg('data', pd.DataFrame, expand='table')
@xw.ret(expand='table')
def average_all(data):
    return data.mean()


@xw.func
@xw.arg('returns', expand='vertical')
@xw.arg('weights', expand='vertical')
def portfolio_return(returns, weights):
    er = 0
    for i, ret in enumerate(returns):
        er = er + ret * weights[i]
    return er


@xw.arg('num_rets', numbers=int)
@xw.ret(expand='table')
def random_normal_returns(mean, stdev, num_rets):
    all_rets = []
    for i in range(num_rets):
        ret = random.normalvariate(mean, stdev)
        all_rets.append(ret)
    vertical_returns = [[ret] for ret in all_rets]
    return vertical_returns