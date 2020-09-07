import datetime
import os
import random

import numpy as np
import pandas as pd
import statsmodels.api as sm
import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

from build_tools.config import LAB_EXERCISES_PATH
from pltemplates.blocks import LabBlock
from pltemplates.exercises.lab_exercise import LabExercise
from pltemplates.hyperlink import Hyperlink


def get_dcf_enterprise_equity_value_exercise() -> LabExercise:

    bullet_contents = [
        [
            pl.TextSize(-1),
            'You are the CFO for a startup developing artificial intelligence technologies. There will be an '
            'initial research phase before making any money. Google is watching your development and will purchase '
            'the company after it is profitable.',
            r'For the first two years (years 0 and 1), the company loses \$20 million. Then there is one breakeven year, after which '
            r'the profit is \$10 million for year 3. Finally in year 4, Google purchases the company for \$70 million.',
            'The WACC for the company is 15% and it has 1 million shares outstanding. The company has \$5 million '
            'in debt and \$1 million in cash.',
            'What is the enterprise value of the stock at year 5? What about the enterprise value today? '
            'What is the price of the stock today?'
        ],
        [
            pl.TextSize(-1),
            'A pharmaceutical company developed a new drug and has 4 years to sell it before the patent expires. '
            'It forms a new company to manufacture and sell the drug. After 4 years, the company will be sold to '
            'someone that wants to continue manufacturing at the lower price. The company is just about to pay a dividend.',
            r'The new company pays a dividend of \$1 per share each year for years 0 to 3, before selling it for \$30 million in '
            r'year 4.',
            r'There are 10 million shares outstanding, \$10 million of debt and \$1 million of cash throughout the '
            r'life of the company. The WACC is 10% today.',
            'What is the enterprise value at year 5 and today? What is the price of the stock today?'
        ]
    ]

    answer_contents = [
        [
            r'The enterprise value at year 5 is \$70 million',
            r'The enterprise value at year 0 is \$9.2 million',
            r'The equity value at year 0 is \$5.21 million so the share price is \$5.21'
        ],
        [
            r'The enterprise value at year 5 is \$30 million',
            r'The equity value at year 0 is \$49.2 million so the share price is \$4.92',
            r'The enterprise value at year 0 is \$58.2 million',
        ]
    ]

    return LabExercise(
        bullet_contents,
        'DCF Value of a Firm',
        f"Finding Enterprise and Equity Value Given FCF and WACC",
        label='lab:dcf-enterprise-equity',
        answers_content=answer_contents
    )


def get_dcf_cost_equity_exercise() -> LabExercise:
    risk_free = 0.02

    data_path = LAB_EXERCISES_PATH / 'DCF' / 'Cost of Equity' / 'prices.xlsx'
    df = pd.read_excel(data_path)
    returns = df.pct_change().dropna()
    returns['MRP'] = returns['Market'] - risk_free
    model = sm.OLS(returns['Asset'], sm.add_constant(returns['MRP']), hasconst=True)
    results = model.fit()
    beta = results.params['MRP']
    market_return = returns['Market'].mean()
    cost_of_equity = risk_free + beta * (market_return - risk_free)
    recession_cost_of_equity = risk_free + beta * ((market_return - 0.03) - risk_free)


    bullet_contents = [
        [
            'Go to Canvas and download "prices.xlsx" from Lab Exercises > DCF > Cost of Equity',
            f'Assume the risk free rate is {risk_free:.0%}',
            'What is the beta and the cost of equity for this company?',
            'If you thought there was going to be a recession, such that the average market return would be '
            '3% lower, then what would you expect the cost of equity to be?',
            'Complete this exercise with the tool of your choice.'
        ],
    ]

    answer_contents = [
        [
            rf'The $\beta$ is {beta:.3f}',
            rf'The cost of equity is {cost_of_equity:.2%}',
            rf'The cost of equity in the recession is {recession_cost_of_equity:.2%}'
        ],
    ]

    return LabExercise(
        bullet_contents,
        'DCF Cost of Equity',
        f"Finding Cost of Equity Given Historical Prices",
        label='lab:dcf-cost-equity',
        answers_content=answer_contents
    )


def get_dcf_cost_debt_exercise() -> LabExercise:

    today = datetime.datetime.today().date()
    bond_price = 1042.12
    coupon_rate = 0.07
    maturity_date = datetime.date(today.year + 3, today.month, today.day)
    par_value = 1000
    tax_rate = 0.35

    bullet_contents = [
        [
            rf'A chemical manufacturer has a {coupon_rate:.1%} coupon, annual pay {par_value} par value bond outstanding, priced '
            rf'at \${bond_price} on {today}.',
            f'If the bond matures on {maturity_date}, what is the '
            rf'cost of debt for this company? The tax rate is {tax_rate:.0%}.',
        ],
        [
            ['Go to', Hyperlink('https://stockrow.com'), "and search for WMT to get Walmart's financials. Calculate "
             "the cost of debt for 2019-07-31 using the financial statements approach. Note that you will also "
             "need to determine the effective tax rate using actual tax paid and EBT."]
        ],
    ]

    # Levels 1 exercise
    l1_pretax_cost_of_debt = np.irr([-bond_price] +  [coupon_rate * par_value for _ in range(3 - 1)] + [(1 + coupon_rate) * par_value])
    l1_aftertax_cost_of_debt = l1_pretax_cost_of_debt * (1 - tax_rate)

    # Level 2 exercise
    wmt_int_exp = 641
    wmt_total_debt = 74709
    wmt_ebt = 4843
    wmt_tax_paid = 1233

    wmt_tax_rate = wmt_tax_paid / wmt_ebt
    wmt_pre_tax_cd = wmt_int_exp / wmt_total_debt
    wmt_after_tax_cd = wmt_pre_tax_cd * (1 - wmt_tax_rate)

    answer_contents = [
        [
            f'The pre-tax cost of debt for the chemical manufacturer is {l1_pretax_cost_of_debt:.2%}',
            f'The after-tax cost of debt for the chemical manufacturer is {l1_aftertax_cost_of_debt:.2%}',
        ],
        [
            f'The pre-tax cost of debt for Walmart in 2019-07-31 is {wmt_pre_tax_cd:.2%}',
            f'The after-tax cost of debt for Walmart in 2019-07-31 is {wmt_after_tax_cd:.2%}',
        ],
    ]

    return LabExercise(
        bullet_contents,
        'DCF Cost of Debt',
        f"Finding Cost of Debt Given Financial and Market Info",
        label='lab:dcf-cost-debt',
        answers_content=answer_contents
    )


def mv_bond_annuity_approach(principal, coupon_rate, maturity, cost_of_debt):
    """
    Calculate the market value of bond with non-integer maturity
    """
    coupon_payment = coupon_rate * principal
    return coupon_payment * ((1 - (1 + cost_of_debt)**(-maturity))/cost_of_debt) + principal/(1 + cost_of_debt)**maturity


def years_between_dates(begin_date, end_date):
    """
    Calculate the number of years until a date, starting from today.
    """
    diff = end_date - begin_date
    seconds = diff.total_seconds()
    seconds_per_year = 60 * 60 * 24 * 365
    years_elapsed = seconds / seconds_per_year
    return years_elapsed