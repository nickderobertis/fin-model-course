import os
import timeit
import datetime

import xlwings as xw
import pandas as pd


# TODO: iterate through all projects in folder, open project, run, check accuracy, output report
from gradetools.project_2.check import score_accuracy_of_result_df
from gradetools.project_2.config import XLWINGS_ADDIN_PATH, TOLERANCE
from gradetools.project_2.run import run_model_assemble_results_in_df


def run_all_models_in_folder_output_accuracy(grade_folder: str, xlwings_addin_path: str = XLWINGS_ADDIN_PATH,
                                             n_iter: int = 1000, tolerance: float = TOLERANCE):
    app = xw.App()
    xl_app = app.api
    xl_app.Workbooks.Open(xlwings_addin_path)

    for folder in next(os.walk(grade_folder))[1]:
        folder_path = os.path.join(grade_folder, folder)
        out_path = os.path.join(folder_path, 'results.csv')
        if os.path.exists(out_path):
            print(f'Skipping {folder} as it already has results')
            continue
        print(f'Processing {folder}', end='')
        start_time = timeit.default_timer()
        xl_files = [file for file in next(os.walk(folder_path))[2] if file.lower().endswith('.xlsm')]
        if len(xl_files) > 1:
            print('')  # cancel end=''
            raise ValueError(f'found more than one excel file in {folder}: {xl_files}')
        xl_file = xl_files[0]
        xl_path = os.path.join(folder_path, xl_file)
        book = xw.Book(xl_path)
        df = run_model_assemble_results_in_df(n_iter)
        score_accuracy_of_result_df(df, tolerance=tolerance)
        book.close()
        df.to_csv(out_path, index=False)
        seconds_elapsed = timeit.default_timer() - start_time
        print(f' took {datetime.timedelta(seconds=seconds_elapsed)}')


def create_results_summary_from_grade_folder(grade_folder: str) -> pd.DataFrame:
    out_path = os.path.join(grade_folder, 'results summary.csv')
    out_data = []
    for folder in next(os.walk(grade_folder))[1]:
        folder_path = os.path.join(grade_folder, folder)
        in_path = os.path.join(folder_path, 'results.csv')
        df = pd.read_csv(in_path)
        accuracy_pct = df['Valid'].sum() / len(df['Valid'])
        problem_cases = df[df['Valid'] == False].index.tolist()
        out_data.append(
            (folder, accuracy_pct, problem_cases)
        )
    full_df = pd.DataFrame(out_data, columns=['Name', 'Accuracy Pct', 'Invalid Cases'])
    full_df.to_csv(out_path, index=False)
    return full_df


def full_grade_process(grade_folder: str, xlwings_addin_path: str = XLWINGS_ADDIN_PATH,
                       n_iter: int = 1000, tolerance: float = TOLERANCE):
    run_all_models_in_folder_output_accuracy(
        grade_folder,
        xlwings_addin_path=xlwings_addin_path,
        n_iter=n_iter,
        tolerance=tolerance
    )
    create_results_summary_from_grade_folder(grade_folder)
