import os

from gradetools.config import PYTHON_FOLDER
from gradetools.py.execute2.main import execute_notebooks_by_config

if __name__ == '__main__':
    from gradetools.project_1.cases import OUTPUT_CASES, INPUT_CASES

    report_out_path = os.path.join(PYTHON_FOLDER, 'accuracy report.csv')

    execute_notebooks_by_config(
        PYTHON_FOLDER,
        INPUT_CASES,
        OUTPUT_CASES,
        report_out_path
    )
