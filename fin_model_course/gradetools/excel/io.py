from typing import Dict, Any
import types


def set_inputs_from_input_range_dict(wb, input_range_dict: Dict[str, str], values_dict: Dict[str, Any]):
    for input_name, cell_range in input_range_dict.items():
        _get_range(wb, cell_range).value = values_dict[input_name]


def get_output_dict_from_output_range_dict(wb, output_range_dict: Dict[str, str], trim_empty_values: bool = True):
    output_dict = {}
    for output_name, cell_range in output_range_dict.items():
        value = _get_range(wb, cell_range).value
        if trim_empty_values and isinstance(value, list):
            value = [val for val in value if val != '']
        output_dict[output_name] = value
    return output_dict


def get_inputs_outputs_sheet_from_file_path(file_path: str):
    import xlwings as xw
    book = xw.Book(file_path)
    ws = book.sheets['Inputs and Outputs']
    return ws


def _get_range(wb, cell_range: str):
    """
    Can be passed the xlwings module or a sheet object. Needs to use Range for xlwings module and range for sheet object
    """
    if isinstance(wb, types.ModuleType):
        attr = 'Range'
    else:
        attr = 'range'

    return getattr(wb, attr)(cell_range)


def close_excel_if_open():
    import xlwings as xw
    try:
        app = list(xw.apps)[0]
    except IndexError:
        # Excel not open
        return

    app.quit()