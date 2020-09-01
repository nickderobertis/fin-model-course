import os
import timeit
import datetime
from typing import Dict, List, Sequence

import pandas as pd


# TODO [#7]: iterate through all projects in folder, open project, run, check accuracy, output report
from gradetools.excel.io import close_excel_if_open
from gradetools.model_type import detect_model_type_in_folder, get_model_file_paths_from_folder
from gradetools.project_3.check import score_accuracy_of_result_dicts, load_answers
from gradetools.project_3.config import TOLERANCES, INPUT_DICTS, ANSWERS_OUTPUT_PATH, EXCEL_INPUT_LOCATIONS, \
    DATA_FILE_NAMES
from gradetools.project_3.run import run_model_assemble_results


def run_all_models_in_folder_output_accuracy(grade_folder: str, tolerances: Dict[str, float] = TOLERANCES,
                                             input_dicts: List[Dict[str, Dict[str, float]]] = INPUT_DICTS,
                                             answers_path: str = ANSWERS_OUTPUT_PATH,
                                             cell_location_dict: Dict[str, str] = EXCEL_INPUT_LOCATIONS,
                                             exclude_files: Sequence[str] = DATA_FILE_NAMES):
    answers = load_answers(answers_path)
    orig_path = os.getcwd()
    for folder in next(os.walk(grade_folder))[1]:
        folder_path = os.path.join(grade_folder, folder)
        out_path = os.path.join(folder_path, 'results.csv')
        if os.path.exists(out_path):
            print(f'Skipping {folder} as it already has results')
            continue
        model_type = detect_model_type_in_folder(folder_path, exclude_files=exclude_files)
        model_files = get_model_file_paths_from_folder(folder_path, model_type, exclude_files=exclude_files)
        print(f'Processing {folder} of type {model_type}', end='')
        start_time = timeit.default_timer()
        os.chdir(folder_path)
        try:
            results = run_model_assemble_results(input_dicts, model_type, model_files, cell_location_dict=cell_location_dict)
        finally:
            os.chdir(orig_path)
        df = score_accuracy_of_result_dicts(results, answers, tolerances=tolerances)
        df.to_csv(out_path)
        seconds_elapsed = timeit.default_timer() - start_time
        print(f' took {datetime.timedelta(seconds=seconds_elapsed)}')
        close_excel_if_open()


def create_results_summary_from_grade_folder(grade_folder: str) -> pd.DataFrame:
    out_path = os.path.join(grade_folder, 'results summary.csv')
    out_data = []
    for folder in next(os.walk(grade_folder))[1]:
        folder_path = os.path.join(grade_folder, folder)
        in_path = os.path.join(folder_path, 'results.csv')
        df = pd.read_csv(in_path, index_col=0)
        valid_cols = [col for col in df.columns if 'Valid' in col]
        total_answers = len(valid_cols) * len(df)
        accuracy_pct = df[valid_cols].sum().sum() / total_answers
        query_str = ' | '.join([f'`{col}` == False' for col in valid_cols])
        problem_cases = df.query(query_str).index.tolist()
        out_data.append(
            (folder, accuracy_pct, problem_cases)
        )
    full_df = pd.DataFrame(out_data, columns=['Name', 'Accuracy Pct', 'Invalid Cases'])
    full_df.to_csv(out_path, index=False)
    return full_df


def full_grade_process(grade_folder: str, tolerances: Dict[str, float] = TOLERANCES):
    run_all_models_in_folder_output_accuracy(
        grade_folder,
        tolerances=tolerances
    )
    create_results_summary_from_grade_folder(grade_folder)

if __name__ == '__main__':
    grade_folder = r'C:\Users\Nick\Desktop\temp for modeling\Grading Project 3\test'
    full_grade_process(grade_folder)
