import datetime
import os
import random

import numpy as np
import pandas as pd
import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll
from finstmt import IncomeStatements, BalanceSheets, FinancialStatements

from build_tools.config import LAB_EXERCISES_PATH
from pltemplates.blocks import LabBlock
from pltemplates.exercises.lab_exercise import LabExercise
from pltemplates.hyperlink import Hyperlink


def get_dcf_fcf_calculation_exercise() -> LabExercise:

    lab_1_inputs = dict(
        adjustments=100,
        change_ar=1000,
        change_inventory=500,
        change_ap=800,
        change_ppe=2000,
        dep_amort=200,
        net_income=300
    )

    lab_1_nwc = lab_1_inputs['change_ar'] + lab_1_inputs['change_inventory'] - lab_1_inputs['change_ap']
    lab_1_capex = lab_1_inputs['change_ppe'] + lab_1_inputs['dep_amort']
    lab_1_fcf = lab_1_inputs['net_income'] + lab_1_inputs['adjustments'] - lab_1_nwc - lab_1_capex

    stmt_folder = LAB_EXERCISES_PATH / 'DCF' / 'FCF'
    bs_path = os.path.join(stmt_folder, 'WMT Balance Sheet.xlsx')
    inc_path = os.path.join(stmt_folder, 'WMT Income Statement.xlsx')

    bs_df = pd.read_excel(bs_path, index_col=0)
    inc_df = pd.read_excel(inc_path, index_col=0)

    bs_data = BalanceSheets.from_df(bs_df)
    inc_data = IncomeStatements.from_df(inc_df)
    stmts = FinancialStatements(inc_data, bs_data)
    lab_2_date_1 = '2019-04-30'
    lab_2_date_2 = '2019-07-31'

    bullet_contents = [
        [
            'Calculate free cash flow from the following information:',
            f"Net income is {lab_1_inputs['net_income']}, the total of non-cash expenditures is "
            f"{lab_1_inputs['adjustments']}, "
            f"the changes in accounts receivable, inventory, accounts payable, and PPE are {lab_1_inputs['change_ar']}, "
            f"{lab_1_inputs['change_inventory']}, {lab_1_inputs['change_ap']}, and {lab_1_inputs['change_ppe']}, "
            f"and depreciation & amortization is {lab_1_inputs['dep_amort']}."
        ],
        [
            'Load in the income statement and balance sheet data associated with Project 3, "WMT Balance Sheet.xlsx" '
            'and "WMT Income Statement.xlsx"',
            'Calculate the free cash flows from these data. Note that some items are missing in these data such as '
            'depreciation. You will just need to exclude any missing items from your calculation',
            f'Get the FCFs for {lab_2_date_1} and {lab_2_date_2}.'
        ]
    ]

    answer_contents = [
        [
            fr'The NWC is \${lab_1_nwc:,.0f}',
            fr'The CapEx is \${lab_1_capex:,.0f}',
            fr'The FCF is \${lab_1_fcf:,.0f}'
        ],
        [
            fr'The FCF for {lab_2_date_1} is \${stmts.fcf[lab_2_date_1]:,.0f}',
            fr'The FCF for {lab_2_date_2} is \${stmts.fcf[lab_2_date_2]:,.0f}',
        ]
    ]

    return LabExercise(
        bullet_contents,
        'Calculate FCFs',
        f"Free Cash Flow Calculation",
        label='lab:dcf-fcf-calc',
        answers_content=answer_contents
    )


def get_dcf_fcf_simple_forecast_exercise() -> LabExercise:

    # NOTE: to get answers, ran Forecast Sales COGS simple but loading in these data instead

    bullet_contents = [
        [
            'Go to Canvas and download "Debt Interest.xlsx" from Lab Exercises > Forecasting > Simple',
            'Forecast the next value of total debt using trend regression approach',
            'Forecast the next value of interest using the four approaches (average, recent, trend reg, trend CAGR)',
            'Forecast the next value of interest using the % of total debt method, with the percentages forecasted '
            'using the four approaches (average, recent, trend reg, trend CAGR)',
        ],
    ]

    answer_contents = [
        [
            r'The forecasted value of total debt should be \$6,867',
            r'The directly forecasted values of interest should be \$1,600, \$1,900, \$2,300, and \$2,391, '
            r'for average, recent, trend reg, trend CAGR, respectively',
            r'The % of debt forecasted values of interest should be \$2,072, \$2,139, \$2,379, and \$2,312, '
            r'for average, recent, trend reg, trend CAGR, respectively',
        ],
    ]

    return LabExercise(
        bullet_contents,
        'Simple Forecast',
        f"Forecasting Simple Time-Series",
        label='lab:dcf-fcf-forecast-simple',
        answers_content=answer_contents
    )


def get_dcf_fcf_complex_forecast_exercise() -> LabExercise:

    # NOTE: to get answers, ran Forecast Quarterly Financial Statements.ipynb but loading in these data instead

    bullet_contents = [
        [
            'Go to Canvas and download "CAT Balance Sheet.xlsx" and "CAT Income Statement.xlsx" from '
            'Lab Exercises > Forecasting > Complex',
            'Forecast the next four periods (one year) of cash using both the Quarterly Seasonal Trend Model and '
            'the automated software approach.',
            'Plot both forecasts to see how they worked.'
        ],
    ]

    answer_contents = [
        [
            r'The forecasted values of cash using the Quarterly Seasonal Trend Model should be \$8,454,920,455, '
            r'\$8,833,593,182, \$8,869,693,182, and \$10,251,393,182',
            r'The forecasted values of cash using the automated approach should be \$8,071,641,657, \$8,185,822,286, '
            r'\$9,132,093,865, and \$9,502,395,879'
        ],
    ]

    return LabExercise(
        bullet_contents,
        'Complex Forecast',
        f"Forecasting Complex Time-Series",
        label='lab:dcf-fcf-forecast-complex',
        answers_content=answer_contents
    )


def get_dcf_fcf_tv_exercise() -> LabExercise:

    ev_ebitda = 18.58
    ev_sales = 1.92
    ev_fcf = 11.82
    pe = 39.30

    ebitda = 1500
    sales = 7898
    shrout = 561
    fcf = 2.36 * shrout
    earnings = 232
    debt = 11631
    cash = 4867
    wacc = 0.1
    growth = 0.03

    def p_from_ev(ev):
        current_ev = np.npv(wacc, [0] + [fcf] * 4 + [fcf + ev])
        equity_value = current_ev - debt + cash
        return equity_value/shrout

    ev_from_ebitda = ev_ebitda * ebitda
    p_from_ebitda = p_from_ev(ev_from_ebitda)
    ev_from_sales = ev_sales * sales
    p_from_sales = p_from_ev(ev_from_sales)
    ev_from_fcf = ev_fcf * fcf
    p_from_fcf = p_from_ev(ev_from_fcf)

    eps = earnings/shrout
    tv_p_from_pe = pe * eps
    ev_from_pe = tv_p_from_pe * shrout
    p_from_pe = p_from_ev(ev_from_pe)

    ev_from_perp = (fcf * (1 + growth))/(wacc - growth)
    p_from_perp = p_from_ev(ev_from_perp)

    bullet_contents = [
        [
            pl.TextSize(-1),
            'Calculate possible stock prices today for a hypothetical company. Use EV/EBITDA, EV/Sales, EV/FCF, and P/E '
            'and the perpetuity growth method to determine five different possible terminal values. '
            'You have already determined that the next 5 years '
            fr'FCFs will be \${fcf:,.0f}M. ',
            fr'EV/EBITDA is {ev_ebitda:.2f}, EV/Sales is {ev_sales:.2f}, EV/FCF is {ev_fcf:.2f}, and P/E is {pe:.2f}.',
            fr'Final period forecasted financial statement values are as follows: EBITDA is \${ebitda:,.0f}M, '
            fr'sales is \${sales:,.0f}M, and net income is \${earnings:,.0f}M',
            fr'Current period financial statement values are as follows: total debt is \${debt:,.0f}M, and '
            fr'cash is \${cash:,.0f}M',
            fr'Shares outstanding is \${shrout:,.0f}M and WACC is {wacc:.1%} for the entire time period',
            f'The terminal growth rate is {growth:.1%}',
            'You can assume the next free cash flow is one year away.'
        ],
    ]

    answer_contents = [
        [
            'The stock prices using the five methods are as follows:',
            fr'EV/EBITDA: \${p_from_ebitda:.2f}',
            fr'EV/Sales: \${p_from_sales:.2f}',
            fr'EV/FCF: \${p_from_fcf:.2f}',
            fr'P/E: \${p_from_pe:.2f}',
            fr'Perpetuity Growth: \${p_from_perp:.2f}',
        ],
    ]

    return LabExercise(
        bullet_contents,
        'Terminal Values',
        f"DCF Stock Price using Terminal Values",
        label='lab:dcf-fcf-tv',
        answers_content=answer_contents
    )