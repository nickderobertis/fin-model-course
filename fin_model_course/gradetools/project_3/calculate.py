from typing import Dict

import pandas as pd

from gradetools.config import PYTHON_ALWAYS_INSERT_CONFIGS
from gradetools.excel.io import get_inputs_outputs_sheet_from_file_path, get_output_dict_from_output_range_dict
from gradetools.model_type import ModelType
from gradetools.project_3.config import EXCEL_OUTPUT_LOCATIONS
from gradetools.py.execute2.main import ReplacementConfig, read_notebook_and_run_extracting_globals, InsertConfig
from gradetools.py.strip_style import get_df_from_df_or_styler


def run_model_extract_results_dict(model_file: str, model_type: ModelType,
                                   inputs_dict: Dict[str, Dict[str, float]]) -> Dict[str, float]:
    if model_type == ModelType.EXCEL:
        return _get_results_from_excel_model(model_file)

    # Python or combo, get from Python
    return _get_results_from_python_model(model_file, inputs_dict)


def _get_results_from_excel_model(model_file: str,
                                  output_locations: Dict[str, str] = EXCEL_OUTPUT_LOCATIONS) -> Dict[str, float]:
    ws = get_inputs_outputs_sheet_from_file_path(model_file)
    table_location = output_locations['mc_table']
    df = ws.range(table_location).expand().options(pd.DataFrame, index=False, header=False).value
    df.columns = ['Beta', 'Market Return', 'Bond Price', 'Tax Rate', 'WACC']

    # Get regular outputs
    single_inputs_dict = output_locations.copy()
    single_inputs_dict.pop('mc_table')
    outputs = get_output_dict_from_output_range_dict(ws, single_inputs_dict)

    _add_wacc_mc_outputs_to_dict(outputs, df)

    return outputs


def _get_results_from_python_model(model_file: str, inputs_dict: Dict[str, Dict[str, float]]) -> Dict[str, float]:
    model_rc = ReplacementConfig('model_data', 'ModelInputs', kwargs=inputs_dict['model'])
    sim_rc = ReplacementConfig('sim_data', 'SimulationInputs', kwargs=inputs_dict['sim'])
    globs = read_notebook_and_run_extracting_globals(
        model_file,
        [model_rc, sim_rc],
        inserts=PYTHON_ALWAYS_INSERT_CONFIGS,
        suppress_output=True
    )
    outputs = {}
    try:
        wacc_mc_df_or_styler = globs['wacc_mc_df']
        outputs['coe'] = globs['coe']
        outputs['mv_equity'] = globs['mv_equity']
        outputs['pretax_cost_of_debt'] = globs['pretax_cost_of_debt']
        outputs['aftertax_cost_of_debt'] = globs['aftertax_cost_of_debt']
        outputs['mv_debt'] = globs['mv_debt']
        outputs['wacc'] = globs['wacc']
    except KeyError as e:
        raise OutputNotFoundException(e)
    wacc_df = get_df_from_df_or_styler(wacc_mc_df_or_styler)
    _add_wacc_mc_outputs_to_dict(outputs, wacc_df)

    return outputs


def _add_wacc_mc_outputs_to_dict(outputs: Dict[str, float], df: pd.DataFrame):
    wacc_mean = df['WACC'].mean()
    wacc_std = df['WACC'].std()
    outputs['wacc_mean'] = wacc_mean
    outputs['wacc_std'] = wacc_std


class OutputNotFoundException(Exception):
    pass
