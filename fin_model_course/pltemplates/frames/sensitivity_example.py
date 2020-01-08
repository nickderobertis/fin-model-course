import itertools
import pandas as pd
import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll


def get_sensitivity_analysis_example_frames():
    possible_values = {
        'c': (60000, 100000),
        'E': (200, 500),
        'P': (50, 100)
    }
    possible_values_str = ', '.join([fr'{var_name} = {poss_vals}' for var_name, poss_vals in possible_values.items()])
    cart_prod = [i for i in itertools.product(*possible_values.values())]
    cart_prod_df = pd.DataFrame(cart_prod, columns=['$c$', '$E$', '$P$'])
    tab = lt.Tabular.from_df(cart_prod_df, align='ccc')
    cart_prod_result_df = cart_prod_df.copy()
    cart_prod_result_df['$D$'] = cart_prod_result_df.apply(lambda series: series['$c$'] - series['$E$'] * series['$P$'],
                                                           axis=1)
    tab_res = lt.Tabular.from_df(cart_prod_result_df, align='cccc')
    return [
        lp.Frame(
            [
                "Let's take a simple demand model as an example:",
                pl.Equation(str_eq='D = c - EP', inline=False),
                pl.Equation(str_eq='X = [c, E, P]', inline=False),
                pl.UnorderedList([
                    [pl.Equation(str_eq='D:'), 'Quantity demanded'],
                    [pl.Equation(str_eq='c:'), 'Demand constant'],
                    [pl.Equation(str_eq='E:'), 'Elasticity of demand'],
                    [pl.Equation(str_eq='P:'), 'Price'],
                    [pl.Equation(str_eq='X:'), 'Model input matrix'],
                ])
            ],
            title='Sensitivity Analysis Example Model'
        ),
        lp.Frame(
            [
                pl.Equation(str_eq='D = c - EP', inline=False),
                'Follow the following steps:',
                pl.OrderedList([
                    ['Choose', pl.Equation(str_eq=possible_values_str)],
                    ['Take the cartesian product of these values, yielding',
                     pl.Equation(str_eq='[X_1, X_2, ..., X_m]:')],
                ]),
                tab,
            ],
            title='Sensitivity Analysis Example'
        ),
        lp.Frame(
            [
                pl.Equation(str_eq='D = c - EP', inline=False),
                'Continue following the steps:',
                pl.OrderedList([
                    ['For each', pl.Equation(str_eq='X_i'), 'calculate', pl.Equation(str_eq='y_i = f(X_i)')],
                    ['Store the values of', pl.Equation(str_eq='X_i'), 'mapped to', pl.Equation(str_eq='y_i')],
                ], initial_number=3),
                tab_res,
            ],
            title='Sensitivity Analysis Example, Pt. 2'
        ),
    ]