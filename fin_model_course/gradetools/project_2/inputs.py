from typing import Dict

from gradetools.excel.io import set_inputs_from_input_range_dict
from gradetools.model_type import ModelType
from gradetools.project_2.config import EXCEL_INPUT_LOCATIONS


def set_inputs(model_type: ModelType, model_file: str, inputs_dict: Dict[str, float]):
    if model_type in (ModelType.EXCEL, ModelType.COMBO):
        _set_inputs_in_excel(model_file, inputs_dict)

    # NOTE: python inputs will be set in combination with running


def _set_inputs_in_excel(model_file: str, values_dict: Dict[str, float], cell_location_dict = EXCEL_INPUT_LOCATIONS):
    import xlwings as xw
    book = xw.Book(model_file)
    ws = book.sheets['Inputs and Outputs']
    set_inputs_from_input_range_dict(ws, cell_location_dict, values_dict)
