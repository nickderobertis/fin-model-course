from typing import List
from gradetools.excel.io import set_inputs_from_input_range_dict, get_output_dict_from_output_range_dict
from gradetools.excel.check import check_output_dict, IncorrectModelOutputException


def check_workbook(wb, input_dict_list: List[dict], output_dict_list: List[dict], input_range_dict: dict,
                   output_range_dict: dict, tolerance: float = 0.001):
    errors_dict = {}
    for i, (input_case, output_case) in enumerate(zip(input_dict_list, output_dict_list)):
        case_num = i + 1
        print(f'Checking case {case_num}')
        errors = _check_workbook_for_inputs(
            wb, input_case, output_case, input_range_dict, output_range_dict, tolerance=tolerance
        )
        if errors:
            errors_dict[case_num] = errors
    return errors_dict


def _check_workbook_for_inputs(wb, input_dict: dict, correct_values: dict, input_range_dict: dict,
                               output_range_dict: dict, tolerance: float = 0.001
                               ) -> List[IncorrectModelOutputException]:
    set_inputs_from_input_range_dict(wb, input_range_dict, input_dict)
    output_dict = get_output_dict_from_output_range_dict(wb, output_range_dict)
    errors = check_output_dict(output_dict, correct_values, tolerance=tolerance)
    return errors
