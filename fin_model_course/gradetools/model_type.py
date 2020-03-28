import os
import pathlib
from enum import Enum

EXCEL_EXTENSIONS = ('xlsx', 'xls', 'xlsm')
PYTHON_EXTENSIONS = ('py', 'ipynb')


class ModelType(Enum):
    EXCEL = 'excel'
    PYTHON = 'python'
    COMBO = 'combination'


def detect_model_type_in_folder(folder: str) -> ModelType:
    has_excel = False
    has_python = False
    files = [file for file in next(os.walk(folder))[2]]
    extensions = set([_get_extension(file) for file in files])
    if any(ext in extensions for ext in EXCEL_EXTENSIONS):
        has_excel = True
    if any(ext in extensions for ext in PYTHON_EXTENSIONS):
        has_python = True
    if has_excel and has_python:
        return ModelType.COMBO
    elif has_python:
        return ModelType.PYTHON
    elif has_excel:
        return ModelType.EXCEL
    else:
        raise ValueError(f'did not detect any model in {folder}')


def get_model_file_path_from_folder(folder: str, model_type: ModelType) -> str:
    files = [file for file in next(os.walk(folder))[2]]
    if model_type == ModelType.EXCEL:
        excel_files = [file for file in files if _get_extension(file) in EXCEL_EXTENSIONS]
        if len(excel_files) == 0:
            raise ValueError(f'no Excel file found in {folder} even though model type is Excel')
        elif len(excel_files) > 1:
            raise ValueError(f'found more than one Excel file in {folder}, not clear which is model')
        return excel_files[0]

    # Python or combination, Python runs model
    python_files = [file for file in files if _get_extension(file) in PYTHON_EXTENSIONS]
    if len(python_files) == 0:
        raise ValueError(f'no Python file found in {folder} even though model type is Python')
    elif len(python_files) > 1:
        raise ValueError(f'found more than one Python file in {folder}, not clear which is model')
    return python_files[0]


def _get_extension(file: str) -> str:
    plib_file = pathlib.Path(file)
    return plib_file.suffix.strip('.').casefold()
