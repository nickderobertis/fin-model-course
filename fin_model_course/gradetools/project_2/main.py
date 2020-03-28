import os
import timeit
import datetime
from typing import Dict, List

import xlwings as xw
import pandas as pd


# TODO: iterate through all projects in folder, open project, run, check accuracy, output report
from gradetools.model_type import detect_model_type_in_folder, get_model_file_path_from_folder
from gradetools.project_2.check import score_accuracy_of_result_df
from gradetools.project_2.config import XLWINGS_ADDIN_PATH, TOLERANCE, INPUT_DICTS
from gradetools.project_2.run import run_model_assemble_results_in_df


def run_all_models_in_folder_output_accuracy(grade_folder: str, xlwings_addin_path: str = XLWINGS_ADDIN_PATH,
                                             n_iter: int = 1000, tolerance: float = TOLERANCE,
                                             input_dicts: List[Dict[str, float]] = INPUT_DICTS):
    for folder in next(os.walk(grade_folder))[1]:
        folder_path = os.path.join(grade_folder, folder)
        out_path = os.path.join(folder_path, 'results.csv')
        if os.path.exists(out_path):
            print(f'Skipping {folder} as it already has results')
            continue
        model_type = detect_model_type_in_folder(folder_path)
        model_file = get_model_file_path_from_folder(folder, model_type)
        print(f'Processing {folder} of type {model_type}', end='')
        start_time = timeit.default_timer()
        df = run_model_assemble_results_in_df(n_iter, input_dicts, model_type, model_file)
        score_accuracy_of_result_df(df, tolerance=tolerance)
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
