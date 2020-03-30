import os
from typing import List, Dict
import json

from gradetools.model_type import detect_model_type_in_folder, get_model_file_paths_from_folder
from gradetools.project_3.config import INPUT_DICTS, ANSWERS_MODEL_FOLDER, ANSWERS_OUTPUT_PATH
from gradetools.project_3.run import run_model_assemble_results
from gradetools.project_3.config import DATA_FILE_NAMES


def run_model_set_answers_json(
    folder_path: str = ANSWERS_MODEL_FOLDER, results_path: str = ANSWERS_OUTPUT_PATH,
    input_dicts: List[Dict[str, Dict[str, float]]] = INPUT_DICTS, data_file_names: List[str] = DATA_FILE_NAMES
):
    orig_path = os.getcwd()
    model_type = detect_model_type_in_folder(folder_path, exclude_files=data_file_names)
    model_files = get_model_file_paths_from_folder(folder_path, model_type, exclude_files=data_file_names)
    os.chdir(folder_path)
    outputs = run_model_assemble_results(input_dicts, model_type, model_files)
    os.chdir(orig_path)
    with open(results_path, 'w') as f:
        f.write(json.dumps(outputs, indent=2))


if __name__ == '__main__':
    run_model_set_answers_json()
