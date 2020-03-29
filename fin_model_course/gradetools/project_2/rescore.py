import os

import pandas as pd

from gradetools.project_2.check import score_accuracy_of_result_df
from gradetools.project_2.config import ANSWERS_OUTPUT_PATH, TOLERANCE
from gradetools.project_2.main import create_results_summary_from_grade_folder


def rescore_accuracy_based_on_existing_results_csvs_in_subfolders(grade_folder: str, tolerance: float = TOLERANCE,
                                                                  answers_csv_path: str = ANSWERS_OUTPUT_PATH):
    """
    Used when the results csv or tolerance has changed, and want to recalculate
    the accuracy without re-running each model
    """
    answers_df = pd.read_csv(answers_csv_path)
    for folder in next(os.walk(grade_folder))[1]:
        folder_path = os.path.join(grade_folder, folder)
        out_path = os.path.join(folder_path, 'results.csv')
        df = pd.read_csv(out_path)
        score_accuracy_of_result_df(df, answers_df, tolerance=tolerance)
        df.to_csv(out_path, index=False)
    create_results_summary_from_grade_folder(grade_folder)

