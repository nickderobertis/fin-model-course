from typing import Dict, List, Tuple
import pandas as pd
from gradetools.excel.check import IncorrectModelOutputException


def error_dict_to_df(error_dict: Dict[int, List[IncorrectModelOutputException]]) -> pd.DataFrame:
    df = pd.DataFrame()
    for case_num, error_list in error_dict.items():
        error_tups = _error_list_to_list_of_tuples(error_list)
        full_tups = [(case_num,) + error_tup for error_tup in error_tups]
        case_df = pd.DataFrame(full_tups, columns=['Case', 'Item', 'Incorrect Value', 'Correct Value'])
        df = df.append(case_df)
    return df


def _error_list_to_list_of_tuples(error_list: List[IncorrectModelOutputException]
                                  ) -> Tuple[List[Tuple[str, float, float]]]:
    return [(error.item, error.incorrect_value, error.correct_value) for error in error_list]


def single_workbook_report_df_from_full_workbook_df(full_df: pd.DataFrame) -> pd.DataFrame:
    series = full_df.groupby('Item')['Case'].apply(lambda x: ', '.join([str(val) for val in x]))
    return pd.DataFrame(series).T.reset_index(drop=True)
