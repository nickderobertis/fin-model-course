import os
from gradetools.project_1.cases import INPUT_CASE_CONFIGS, OUTPUT_CASES
from gradetools.project_1.excel.config import INPUT_RANGE_DICT, OUTPUT_RANGE_DICT
from gradetools.excel.main import open_all_workbooks_in_folder_check_sheet_create_df
from gradetools.config import EXCEL_FOLDER


if __name__ == '__main__':
    open_all_workbooks_in_folder_check_sheet_create_df(
        EXCEL_FOLDER,
        'Inputs and Outputs',
        INPUT_CASE_CONFIGS,
        OUTPUT_CASES,
        INPUT_RANGE_DICT,
        OUTPUT_RANGE_DICT,
        report_path=os.path.join(EXCEL_FOLDER, 'accuracy report.csv'),
        full_error_path=os.path.join(EXCEL_FOLDER, 'full accuracy data.csv')
    )