import os
import shutil

from gradetools.config import PYTHON_EXTENSIONS, EXCEL_EXTENSIONS, PYTHON_FOLDER, EXCEL_FOLDER

SOURCE_DIR = r'D:\Dropbox (Personal)\UF\Teaching\Modeling\Me\Grading\Spring 2020\Project 1\submissions'


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