from gradetools.excel.io import set_inputs_from_input_range_dict, get_output_dict_from_output_range_dict
from gradetools.excel.check import check_output_dict
from models.project_1 import PhoneManufacturingModel
from gradetools.project_1.cases import INPUT_CASES
from gradetools.project_1.excel.config import INPUT_RANGE_DICT, OUTPUT_RANGE_DICT


def check_workbook(wb):
    for i, case in enumerate(INPUT_CASES):
        print(f'Checking case {i + 1}')
        _check_workbook_for_inputs(wb, case)


def _check_workbook_for_inputs(wb, input_dict: dict):
    model = PhoneManufacturingModel(**input_dict)
    correct_values = dict(
        pv=model.pv,
        cash_flows=model.cash_flows
    )
    set_inputs_from_input_range_dict(wb, INPUT_RANGE_DICT, input_dict)
    output_dict = get_output_dict_from_output_range_dict(wb, OUTPUT_RANGE_DICT)
    check_output_dict(output_dict, correct_values)
