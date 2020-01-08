import pandas as pd

from gradetools.project_2.config import IRR_RESULTS


def score_accuracy_of_result_df(df: pd.DataFrame, tolerance: float = 0.03):
    """
    Note: inplace
    """
    check_series = pd.Series(IRR_RESULTS)
    diff = abs(df.IRR - check_series)
    invalid_indices = diff[diff > tolerance].index
    df['Valid'] = True
    df.loc[invalid_indices, 'Valid'] = False
