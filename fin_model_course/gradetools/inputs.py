from typing import Dict, List

from gradetools.excel.io import set_inputs_from_input_range_dict
from gradetools.model_type import ModelType, get_excel_file_from_model_files


def set_inputs(model_type: ModelType, model_files: List[str], inputs_dict: Dict[str, float],
               cell_location_dict: Dict[str, str]):
    if model_type in (ModelType.EXCEL, ModelType.COMBO):
        model_file = get_excel_file_from_model_files(model_files, model_type)
        _set_inputs_in_excel(model_file, inputs_dict, cell_location_dict)

    # NOTE: python inputs will be set in combination with running


def _set_inputs_in_excel(model_file: str, values_dict: Dict[str, float], cell_location_dict: Dict[str, str]):
    import xlwings as xw
    book = xw.Book(model_file)
    ws = book.sheets['Inputs and Outputs']
    set_inputs_from_input_range_dict(ws, cell_location_dict, values_dict)
