from typing import List, Optional
import os
import pandas as pd
from gradetools.excel.io import set_inputs_from_input_range_dict, get_output_dict_from_output_range_dict
from gradetools.excel.check import check_output_dict, IncorrectModelOutputException
from gradetools.excel.fileops import open_workbook_get_sheet, close_workbook
from gradetools.excel.error_df import error_dict_to_df, single_workbook_report_df_from_full_workbook_df
from gradetools.config import EXCEL_EXTENSIONS
from gradetools.case_config import CaseConfig


def open_all_workbooks_in_folder_check_sheet_create_df(folder_path: str, sheet_name: str,
                                                       input_configs: List[CaseConfig],
                                                       output_dict_list: List[dict], input_range_dict: dict,
                                                       output_range_dict: dict, tolerance: float = 0.001,
                                                       report_path: Optional[str] = None,
                                                       full_error_path: str = 'full accuracy data.csv'
                                                       ) -> pd.DataFrame:
    report_df = pd.DataFrame()
    full_df = pd.DataFrame()
    files = [
        file for file in next(os.walk(folder_path))[2]
        if os.path.splitext(file)[1].strip('.').lower() in EXCEL_EXTENSIONS and
        not file.startswith('~')
    ]
    for file in files:
        file_path = os.path.join(folder_path, file)
        print(f'Checking {file}')
        error_dict = open_workbook_check_sheet_close(
            file_path,
            sheet_name,
            input_configs,
            output_dict_list,
            input_range_dict,
            output_range_dict,
            tolerance=tolerance
        )
        if error_dict:
            wb_full_df = error_dict_to_df(error_dict)
            wb_report_df = single_workbook_report_df_from_full_workbook_df(wb_full_df)
            wb_full_df.index = [file for _ in range(len(wb_full_df))]
            wb_report_df.index = [file]
            full_df = full_df.append(wb_full_df)
        else:
            wb_report_df = pd.DataFrame(index=[file])
        report_df = report_df.append(wb_report_df)
        print('\n')

    if report_path:
        report_df.to_csv(report_path)

    full_df.to_csv(full_error_path)

    return report_df


def open_workbook_check_sheet_close(file_path: str, sheet_name: str, input_configs: List[CaseConfig],
                                    output_dict_list: List[dict], input_range_dict: dict,
                                    output_range_dict: dict, tolerance: float = 0.001):
    sheet = open_workbook_get_sheet(file_path, sheet_name)
    errors_dict = check_workbook(sheet, input_configs, output_dict_list, input_range_dict,
                                 output_range_dict, tolerance=tolerance)
    close_workbook(sheet)
    return errors_dict


def check_workbook(wb, input_configs: List[CaseConfig], output_dict_list: List[dict], input_range_dict: dict,
                   output_range_dict: dict, tolerance: float = 0.001):
    errors_dict = {}
    for i, (input_case, output_case) in enumerate(zip(input_configs, output_dict_list)):
        case_num = i + 1
        name = input_case.case_name
        print(f'Checking case {case_num}: {name}')
        errors = _check_workbook_for_inputs(
            wb, input_case.input_dict, output_case, input_range_dict, output_range_dict, tolerance=tolerance
        )
        if errors:
            errors_dict[name] = errors
    return errors_dict


def _check_workbook_for_inputs(wb, input_dict: dict, correct_values: dict, input_range_dict: dict,
                               output_range_dict: dict, tolerance: float = 0.001
                               ) -> List[IncorrectModelOutputException]:
    set_inputs_from_input_range_dict(wb, input_range_dict, input_dict)
    output_dict = get_output_dict_from_output_range_dict(wb, output_range_dict)
    errors = check_output_dict(output_dict, correct_values, tolerance=tolerance)
    return errors
