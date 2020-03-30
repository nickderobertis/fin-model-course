from typing import Dict, List

import pandas as pd

from gradetools.excel.io import get_inputs_outputs_sheet_from_file_path
from gradetools.model_type import ModelType, get_excel_file_from_model_files
from gradetools.project_2.calculate import run_model_extract_irr_df
from gradetools.project_2.config import EXCEL_INPUT_LOCATIONS
from gradetools.inputs import set_inputs


def run_model_assemble_results_in_df(input_dicts: List[Dict[str, float]], model_type: ModelType,
                                     model_files: List[str],
                                     cell_location_dict: Dict[str, str] = EXCEL_INPUT_LOCATIONS) -> pd.DataFrame:
    all_dfs = []
    for input_dict in input_dicts:

        set_inputs(model_type, model_files, input_dict, cell_location_dict)
        df = run_model_extract_irr_df(model_files[0], model_type, input_dict)
        for inp_name, inp_value in input_dict.items():
            df[inp_name] = inp_value
        all_dfs.append(df)

    if model_type != ModelType.PYTHON:
        # Excel involved, close it down
        excel_file = get_excel_file_from_model_files(model_files, model_type)
        sheet = get_inputs_outputs_sheet_from_file_path(excel_file)
        sheet.book.close()

    df = pd.concat(all_dfs, axis=0)
    df = _standardize_df(df)
    return df


def _standardize_df(df: pd.DataFrame) -> pd.DataFrame:
    col_order = [
        'Interest Rate',
        'Loan Life',
        'Initial Default Probability',
        'price_machine',
        'default_decay',
        'final_default',
        'recovery_rate',
        'num_iterations'
    ]

    return df.sort_values(col_order)[col_order + ['IRR']].reset_index(drop=True)
