from typing import Dict, Any


def set_inputs_from_input_range_dict(wb, input_range_dict: Dict[str, str], values_dict: Dict[str, Any]):
    for input_name, cell_range in input_range_dict.items():
        wb.Range(cell_range).value = values_dict[input_name]


def get_output_dict_from_output_range_dict(wb, output_range_dict: Dict[str, str], trim_empty_values: bool = True):
    output_dict = {}
    for output_name, cell_range in output_range_dict.items():
        value = wb.Range(cell_range).value
        if trim_empty_values and isinstance(value, list):
            value = [val for val in value if val != '']
        output_dict[output_name] = value
    return output_dict

