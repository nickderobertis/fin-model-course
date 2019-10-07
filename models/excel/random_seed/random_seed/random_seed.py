import xlwings as xw
import numpy as np
import pandas as pd


@xw.func
@xw.ret(expand='table')
@xw.arg('mean', doc='The mean of the normal distribution')
@xw.arg('stdev', doc='The standard deviation of the normal distribution')
@xw.arg('rows', numbers=int, doc='The number of rows of random numbers to generate')
@xw.arg('columns', numbers=int, doc='The number of columns of random numbers to generate')
@xw.arg('seed', numbers=int, doc='The number to use to seed the random number generator. Pass a number to get consistent values')
def random_normal_array(mean, stdev, rows=1, columns=1, seed=None):
    """
    Draw random values from a normal distribution
    """
    if seed is not None:
        np.random.seed(seed)
    return np.random.normal(mean, stdev, (rows, columns))


@xw.func(volatile=True)
@xw.arg('data', pd.DataFrame, index=False, header=False, expand='table', doc='The top left cell of your data, not including headers')
@xw.arg('headers', np.array, expand='right', doc='Optional left-most cell of headers row')
@xw.ret(expand='table')
def summary_stats(data, headers=None):
    """
    Write summary statistics about a table by referencing it's top-left most cell
    """
    if headers is not None:
        data.columns = headers
    else:
        data.columns = ['' for _ in range(len(data.columns))]
    return data.describe()




if __name__ == '__main__':
    xw.serve()
