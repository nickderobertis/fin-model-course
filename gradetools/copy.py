import os
import shutil

PYTHON_EXTENSIONS = ('ipynb', 'py')
EXCEL_EXTENSIONS = ('xlsx', 'xls', 'xlsm')

PYTHON_FOLDER = 'Grading/Python'
EXCEL_FOLDER = 'Grading/Excel'
SOURCE_DIR = '/home/nick/Dropbox/UF/Teaching/Modeling/Me/Grading/Fall 2019/Project 1/submissions'


def copy_for_grading(source_dir: str, python_folder: str, excel_folder: str):
    files = [file for file in next(os.walk(source_dir))[2]]
    for file in files:
        base, extension = os.path.splitext(file)
        extension = extension.lower().strip('.')
        file_path = os.path.join(source_dir, file)
        if extension in PYTHON_EXTENSIONS:
            shutil.copy(file_path, python_folder)
        elif extension in EXCEL_EXTENSIONS:
            shutil.copy(file_path, excel_folder)
        else:
            raise ValueError(f'could not decide where to put file {file}, not a python or excel extension')


if __name__ == '__main__':
    copy_for_grading(SOURCE_DIR, PYTHON_FOLDER, EXCEL_FOLDER)