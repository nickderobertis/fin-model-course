import os
from typing import List, Dict

from gradetools.model_type import detect_model_type_in_folder, get_model_file_paths_from_folder
from gradetools.project_2.config import INPUT_DICTS, ANSWERS_MODEL_FOLDER, ANSWERS_OUTPUT_PATH
from gradetools.project_2.run import run_model_assemble_results_in_df


def run_model_set_answers_csv(
    folder_path: str = ANSWERS_MODEL_FOLDER, results_path: str = ANSWERS_OUTPUT_PATH,
    input_dicts: List[Dict[str, float]] = INPUT_DICTS
):
    orig_path = os.getcwd()
    model_type = detect_model_type_in_folder(folder_path)
    model_files = get_model_file_paths_from_folder(folder_path, model_type)
    os.chdir(folder_path)
    df = run_model_assemble_results_in_df(input_dicts, model_type, model_files)
    os.chdir(orig_path)
    df.to_csv(results_path, index=False)

if __name__ == '__main__':
    run_model_set_answers_csv()
