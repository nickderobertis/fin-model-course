from typing import List, Optional
import os
import pandas as pd
from gradetools.excel.io import set_inputs_from_input_range_dict, get_output_dict_from_output_range_dict
from gradetools.excel.check import check_output_dict, IncorrectModelOutputException
from gradetools.excel.fileops import open_workbook_get_sheet, close_workbook
from gradetools.config import EXCEL_EXTENSIONS


def open_all_workbooks_in_folder_check_sheet_create_df(folder_path: str, sheet_name: str, input_dict_list: List[dict],
                                                       output_dict_list: List[dict], input_range_dict: dict,
                                                       output_range_dict: dict, tolerance: float = 0.001,
                                                       report_path: Optional[str] = None
                                                       ) -> pd.DataFrame:
    out_df = pd.DataFrame()
    files = [
        file for file in next(os.walk(folder_path))[2]
        if os.path.splitext(file)[1].strip('.').lower() in EXCEL_EXTENSIONS
    ]
    for file in files:
        file_path = os.path.join(folder_path, file)
        print(f'Checking {file}')
        error_dict = open_workbook_check_sheet_close(
            file_path,
            sheet_name,
            input_dict_list,
            output_dict_list,
            input_range_dict,
            output_range_dict,
            tolerance=tolerance
        )
        if error_dict:
            series = pd.Series(error_dict)
            df = pd.DataFrame(series).T
            df.index = [file]
        else:
            df = pd.DataFrame(index=[file])
        out_df = out_df.append(df)
        print('\n')

    if report_path:
        out_df.to_csv(report_path)

    return out_df


def open_workbook_check_sheet_close(file_path: str, sheet_name: str, input_dict_list: List[dict],
                                    output_dict_list: List[dict], input_range_dict: dict,
                                    output_range_dict: dict, tolerance: float = 0.001):
    sheet = open_workbook_get_sheet(file_path, sheet_name)
    errors_dict = check_workbook(sheet, input_dict_list, output_dict_list, input_range_dict,
                                 output_range_dict, tolerance=tolerance)
    close_workbook(sheet)
    return errors_dict


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
