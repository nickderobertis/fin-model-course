import os
from gradetools.project_1.py.config import POSSIBLE_INPUT_NAMES, NOTEBOOK_SLICES
from gradetools.config import PYTHON_FOLDER
from gradetools.project_1.cases import INPUT_CASES, OUTPUT_CASES
from gradetools.py.execute.main import execute_notebooks_by_config


def grade_notebooks_by_accuracy():
    return execute_notebooks_by_config(
        NOTEBOOK_SLICES,
        PYTHON_FOLDER,
        INPUT_CASES,
        OUTPUT_CASES,
        possible_names_dict=POSSIBLE_INPUT_NAMES,
        remove_input_cells=True,
        report_out_path=os.path.join(PYTHON_FOLDER, 'accuracy report.csv')
    )


if __name__ == '__main__':
    grade_notebooks_by_accuracy()