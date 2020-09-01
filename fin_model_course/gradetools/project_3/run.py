from typing import Dict, List

from gradetools.excel.io import get_inputs_outputs_sheet_from_file_path
from gradetools.model_type import ModelType, get_excel_file_from_model_files
from gradetools.project_3.calculate import run_model_extract_results_dict
from gradetools.inputs import set_inputs
from gradetools.project_3.config import EXCEL_INPUT_LOCATIONS

# TODO [#8]: some repeated logic versus project 2, could be restructured


def run_model_assemble_results(input_dicts: List[Dict[str, Dict[str, float]]], model_type: ModelType,
                               model_files: List[str],
                               cell_location_dict: Dict[str, str] = EXCEL_INPUT_LOCATIONS
                               ) -> List[Dict[str, float]]:
    all_outputs = []
    for input_dict in input_dicts:
        # Set inputs only operates on Excel, where it need not be a nested dict
        all_inputs_dict = input_dict['model'].copy()
        all_inputs_dict.update(input_dict['sim'])
        set_inputs(model_type, model_files, all_inputs_dict, cell_location_dict)

        outputs = run_model_extract_results_dict(model_files[0], model_type, input_dict)
        for inp_name, inp_value in all_inputs_dict.items():
            outputs[inp_name] = inp_value
        all_outputs.append(outputs)

    if model_type != ModelType.PYTHON:
        # Excel involved, close it down
        excel_file = get_excel_file_from_model_files(model_files, model_type)
        sheet = get_inputs_outputs_sheet_from_file_path(excel_file)
        sheet.book.close()

    return all_outputs
