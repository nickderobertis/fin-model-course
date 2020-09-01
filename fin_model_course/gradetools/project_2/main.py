import os
import timeit
import datetime
from typing import Dict, List

import pandas as pd


# TODO [#5]: iterate through all projects in folder, open project, run, check accuracy, output report
from gradetools.model_type import detect_model_type_in_folder, get_model_file_paths_from_folder
from gradetools.project_2.check import score_accuracy_of_result_df
from gradetools.project_2.config import TOLERANCE, INPUT_DICTS, ANSWERS_OUTPUT_PATH
from gradetools.project_2.run import run_model_assemble_results_in_df


def run_all_models_in_folder_output_accuracy(grade_folder: str, tolerance: float = TOLERANCE,
                                             input_dicts: List[Dict[str, float]] = INPUT_DICTS,
                                             answers_csv_path: str = ANSWERS_OUTPUT_PATH):
    answers_df = pd.read_csv(answers_csv_path)
    orig_path = os.getcwd()
    for folder in next(os.walk(grade_folder))[1]:
        folder_path = os.path.join(grade_folder, folder)
        out_path = os.path.join(folder_path, 'results.csv')
        if os.path.exists(out_path):
            print(f'Skipping {folder} as it already has results')
            continue
        model_type = detect_model_type_in_folder(folder_path)
        model_files = get_model_file_paths_from_folder(folder_path, model_type)
        print(f'Processing {folder} of type {model_type}', end='')
        start_time = timeit.default_timer()
        os.chdir(folder_path)
        df = run_model_assemble_results_in_df(input_dicts, model_type, model_files)
        os.chdir(orig_path)
        score_accuracy_of_result_df(df, answers_df, tolerance=tolerance)
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


def full_grade_process(grade_folder: str, tolerance: float = TOLERANCE):
    run_all_models_in_folder_output_accuracy(
        grade_folder,
        tolerance=tolerance
    )
    create_results_summary_from_grade_folder(grade_folder)
