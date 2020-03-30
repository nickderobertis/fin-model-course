from typing import Dict

import pandas as pd

from gradetools.config import PYTHON_ALWAYS_INSERT_CONFIGS
from gradetools.excel.io import get_inputs_outputs_sheet_from_file_path
from gradetools.model_type import ModelType
from gradetools.project_2.config import EXCEL_OUTPUT_TABLE_LOCATION
from gradetools.py.execute2.main import ReplacementConfig, read_notebook_and_run_extracting_globals
from gradetools.py.strip_style import get_df_from_df_or_styler


def run_model_extract_irr_df(model_file: str, model_type: ModelType, inputs_dict: Dict[str, float]) -> pd.DataFrame:
    if model_type == ModelType.EXCEL:
        return _get_results_from_excel_model(model_file)

    # Python or combo, get from Python
    return _get_results_from_python_model(model_file, inputs_dict)


def _get_results_from_excel_model(model_file: str, table_location: str = EXCEL_OUTPUT_TABLE_LOCATION) -> pd.DataFrame:
    ws = get_inputs_outputs_sheet_from_file_path(model_file)
    df = ws.range(table_location).expand().options(pd.DataFrame, index=False, header=False).value
    df.columns = [
        'Interest Rate',
        'Loan Life',
        'Initial Default Probability',
        'IRR'
    ]
    return df


def _get_results_from_python_model(model_file: str, inputs_dict: Dict[str, float]) -> pd.DataFrame:
    rc = ReplacementConfig('model_data', 'ModelInputs', kwargs=inputs_dict)
    globs = read_notebook_and_run_extracting_globals(
        model_file,
        [rc],
        inserts=PYTHON_ALWAYS_INSERT_CONFIGS,
        suppress_output=True
    )
    try:
        irr_df_or_styler = globs['irr_df']
    except KeyError:
        raise IRRDataFrameNotFoundException
    irr_df = get_df_from_df_or_styler(irr_df_or_styler)
    return irr_df


class IRRDataFrameNotFoundException(Exception):
    pass
