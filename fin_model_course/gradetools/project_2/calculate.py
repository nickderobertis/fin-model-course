from typing import List, Tuple, Dict, Union

import pandas as pd
from pandas.io.formats.style import Styler

from gradetools.excel.io import get_inputs_outputs_sheet_from_file_path
from gradetools.excel.values import get_non_none_range_value
from gradetools.model_type import ModelType
from gradetools.project_2.config import EXCEL_OUTPUT_TABLE_LOCATION
from gradetools.py.execute2.main import ReplacementConfig, read_notebook_and_run_extracting_globals


def run_model_extract_irr_df(model_file: str, model_type: ModelType, inputs_dict: Dict[str, float]) -> pd.DataFrame:
    if model_type == ModelType.EXCEL:
        return _get_results_from_excel_model(model_file)

    # Python or combo, get from Python
    return _get_results_from_python_model(model_file, inputs_dict)


def _get_results_from_excel_model(model_file: str, table_location: str = EXCEL_OUTPUT_TABLE_LOCATION) -> pd.DataFrame:
    ws = get_inputs_outputs_sheet_from_file_path(model_file)
    df = ws.range(table_location).expand().options(pd.DataFrame, index=False)
    return df


def _get_results_from_python_model(model_file: str, inputs_dict: Dict[str, float]) -> pd.DataFrame:
    rc = ReplacementConfig('model_data', 'ModelInputs', kwargs=inputs_dict)
    globs = read_notebook_and_run_extracting_globals(model_file, [rc], suppress_output=True)
    try:
        irr_df_or_styler = globs['irr_df']
    except KeyError:
        raise IRRDataFrameNotFoundException
    irr_df = _get_irr_df_from_irr_df_or_styler(irr_df_or_styler)
    return irr_df


def _get_irr_df_from_irr_df_or_styler(df_or_sty: Union[pd.DataFrame, Styler]) -> pd.DataFrame:
    if isinstance(df_or_sty, Styler):
        return df_or_sty.data
    if isinstance(df_or_sty, pd.DataFrame):
        return df_or_sty

    raise ValueError(f'got inproper type, should be DataFrame or Styler, got {type(df_or_sty)}')


class IRRDataFrameNotFoundException(Exception):
    pass
