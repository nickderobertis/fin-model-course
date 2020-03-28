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


def _get_extension(file: str) -> str:
    plib_file = pathlib.Path(file)
    return plib_file.suffix.strip('.').casefold()
