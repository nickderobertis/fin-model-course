import xlwings as xw
import random
import pandas as pd

@xw.func
@xw.arg('num_periods', numbers=int)
@xw.ret(expand='table')
def n_random_normal(mean, stdev, num_periods, horizontal=False):
    random_values = []
    for i in range(num_periods):
        num = random.normalvariate(mean, stdev)
        if not horizontal:
            num = [num]
        random_values.append(num)
    return random_values


@xw.func
@xw.arg('nper', numbers=int)
@xw.ret(expand='horizontal')
def n_random_uniform(bot, top, nper):
    nums = []
    for i in range(nper):
        num = random.uniform(bot, top)
        nums.append(num)
    return nums


def capm(risk_free, beta, market_ret, epsilon):
    return risk_free + beta * (market_ret - risk_free) + epsilon


def capm_auto_epsilon(risk_free, beta, market_ret, epsilon_stdev):
    epsilon = random.normalvariate(0, epsilon_stdev)

    return capm(risk_free, beta, market_ret, epsilon)


@xw.func
@xw.arg('betas', expand='horizontal')
@xw.arg('epsilon_stdevs', expand='horizontal')
@xw.arg('market_rets', expand='vertical')
@xw.arg('num_assets', numbers=int)
@xw.ret(expand='table', index=False)
def multi_capm(risk_free, betas, market_rets, epsilon_stdevs, num_assets):
    df = pd.DataFrame()
    for i in range(num_assets):
        beta = betas[i]
        epsilon_stdev = epsilon_stdevs[i]
        returns = [capm_auto_epsilon(risk_free, beta, market_ret, epsilon_stdev) for market_ret in market_rets]
        df[f'Asset {i + 1}'] = returns
    return df


@xw.func
@xw.arg('data', pd.DataFrame, expand='table', index=False)
@xw.ret(expand='table')
def correlations(data):
    return data.corr()

