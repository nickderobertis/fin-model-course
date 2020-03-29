import pandas as pd


def score_accuracy_of_result_df(df: pd.DataFrame, answers_df: pd.DataFrame, tolerance: float = 0.03):
    """
    Note: inplace
    """
    diff = abs(df.IRR - answers_df.IRR)
    invalid_indices = diff[diff > tolerance].index
    df['Valid'] = True
    df.loc[invalid_indices, 'Valid'] = False
