import xlwings as xw
import random
import pandas as pd
from pythoncom import com_error
import time


class CannotCollectOutputsException(Exception):
    pass


def run_workbook_collect_outputs():
    wb = xw.Book.caller()
    wb.sheets['Trials'].range('A:A').clear()
    n_iter = wb.sheets['Inputs and Outputs'].range('B11').value
    for i in range(int(n_iter)):
        output_row = i + 1
        finished = False
        retries = 0
        while not finished:
            try:
                result = wb.sheets['Inputs and Outputs'].range('B15').value
                wb.sheets['Trials'].range(f'A{output_row}').value = result
                wb.app.api.CalculateFull()
                finished = True
            except com_error:
                # Expected to hit these issues when running too fast for Excel to keep up
                time.sleep(.5)
                retries += 1
                if retries > 3:
                    # Something is really wrong, cannot calculate at all anymore, exit the loop
                    raise CannotCollectOutputsException('could not calculate workbook after trying 3 times over 1.5s')
                


@xw.func
@xw.arg('n_years', numbers=int, doc='The number of years')
@xw.ret(expand='table')
def default_probabilities(n_years, initial_prob, prob_decay, final_prob):
    all_probabilities = []
    default_prob = initial_prob
    for year in range(n_years + 1):
        if year == 0:
            all_probabilities.append(0)  # cannot default before taking loan
            continue
        elif year == 1:
            all_probabilities.append(initial_prob)
            continue
        elif year == n_years:
            all_probabilities.append(final_prob)
            continue
        default_prob *= prob_decay
        all_probabilities.append(default_prob)
    return [[prob] for prob in all_probabilities]


@xw.func
@xw.arg('n_years', numbers=int, doc='The number of years')
@xw.ret(expand='table')
def n_years_array(n_years):
    n_years += 2  # padding for bankruptcy in repayment
    return [[i] for i in range(n_years + 1)]


def has_default(prob):
    cases = [0, 1]
    probs = [(1 - prob), prob]
    return random.choices(cases, probs)[0]


@xw.func
@xw.arg('n_years', numbers=int, doc='The number of years')
@xw.ret(expand='table', index=False)
def has_default_and_repayment_years(n_years, probabilities):
    # pad all years by 2 for bankruptcy in repayment
    default_years = [0] * (n_years + 3)
    repayment_years = [0] * (n_years + 3)
    recovery_years = [0] * (n_years + 3)
    for year in range(n_years + 1):
        prob = probabilities[year]
        in_default = has_default(prob)
        default_years[year] = in_default
        if in_default:
            # Default year. Repayment should be two years later
            default_years[year] = 1
            recovery_years[year + 2] = 1
            break

    # Handle case where never defaults
    if sum(recovery_years) == 0:
        repayment_years[n_years] = 1

    df = pd.DataFrame()
    df['In Default Period'] = default_years
    df['Repayment Period'] = repayment_years
    df['Recovery Period'] = recovery_years
    return df


@xw.func
@xw.arg('data', pd.DataFrame, index=False, expand='table', doc='The top left cell of your data, including headers')
@xw.ret(expand='table', index=False)
def print_table(data):
    return data


def cash_flow_at_year(loan_amt, int_rate, recovery_rate, year, default, repayment, recovery):
    if year == 0:
        return -loan_amt

    if default:
        return 0

    interest = int_rate * loan_amt

    if repayment:
        return interest + loan_amt

    if recovery:
        return loan_amt * recovery_rate

    # Normal case
    return interest


@xw.func
@xw.arg('defaults', expand='vertical', doc='The top cell of defaults, excluding header')
@xw.arg('repayments', expand='vertical', doc='The top cell of repayments, excluding header')
@xw.arg('recoveries', expand='vertical', doc='The top cell of recoveries, excluding header')
@xw.ret(expand='table')
def cash_flows(loan_amt, int_rate, recovery_rate, n_years, defaults, repayments, recoveries):
    out_cash_flows = []
    no_cash_flow = False
    ever_in_default = False
    for year, (default, repayment, recovery) in enumerate(zip(defaults, repayments, recoveries)):
        if default:
            ever_in_default = True
        if ever_in_default:
            # After default, all future cash flows are zero, except for recovery
            no_cash_flow = True
        if recovery:
            # Handle the single year which should have a cash flow after default, the recovery year
            no_cash_flow = False

        if no_cash_flow:
            out_cash_flows.append(0)
        else:
            out_cash_flows.append(cash_flow_at_year(
                loan_amt,
                int_rate,
                recovery_rate,
                year,
                default,
                repayment,
                recovery
            ))

        if not ever_in_default and year == n_years:
            # Last year of cash flows in normal case. Stop loop. Extra years only needed for default cases
            break
    return [[cf] for cf in out_cash_flows]