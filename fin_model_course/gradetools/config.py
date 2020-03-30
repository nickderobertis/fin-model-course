import os

from gradetools.py.execute2.insert import InsertConfig

PYTHON_EXTENSIONS = ('ipynb', 'py')
EXCEL_EXTENSIONS = ('xlsx', 'xls', 'xlsm')
PYTHON_FOLDER = os.path.sep.join(['Grading', 'Python'])
PYTHON_PLAGIARISM_FOLDER = os.path.sep.join([PYTHON_FOLDER, 'Plagiarism'])
EXCEL_FOLDER = os.path.sep.join(['Grading', 'Excel'])

PYTHON_ALWAYS_INSERT_CONFIGS = [
    InsertConfig(
        [
            'import matplotlib',
            'matplotlib.use("Agg")'
        ],
        0
    )
]