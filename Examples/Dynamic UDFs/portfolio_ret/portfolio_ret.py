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
