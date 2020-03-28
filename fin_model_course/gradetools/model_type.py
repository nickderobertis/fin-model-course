import os
import pathlib
from enum import Enum
from typing import List

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


def get_model_file_paths_from_folder(folder: str, model_type: ModelType) -> List[str]:
    if model_type == ModelType.COMBO:
        python_file = _get_file_of_type_from_folder(folder, ModelType.PYTHON)
        excel_file = _get_file_of_type_from_folder(folder, ModelType.EXCEL)
        return [python_file, excel_file]

    # Pure Python or pure Excel, return only that
    return [_get_file_of_type_from_folder(folder, model_type)]


def get_excel_file_from_model_files(model_files: List[str], model_type: ModelType) -> str:
    if model_type == ModelType.PYTHON:
        raise ValueError('trying to get Excel file from Python model')

    if model_type == ModelType.EXCEL:
        return model_files[0]
    else:
        # In combo, python model file comes first
        return model_files[1]


def _get_file_of_type_from_folder(folder: str, model_type: ModelType) -> str:
    files = [file for file in next(os.walk(folder))[2]]
    if model_type == model_type.EXCEL:
        extensions = EXCEL_EXTENSIONS
    elif model_type == model_type.PYTHON:
        extensions = PYTHON_EXTENSIONS
    else:
        raise ValueError('must pass Excel or Python model type')

    selected_files = [file for file in files if _get_extension(file) in extensions]
    if len(selected_files) == 0:
        raise ValueError(f'no {model_type} file found in {folder} even though model type is {model_type}')
    elif len(selected_files) > 1:
        raise ValueError(f'found more than one {model_type} file in {folder}, not clear which is model')
    return selected_files[0]


def _get_extension(file: str) -> str:
    plib_file = pathlib.Path(file)
    return plib_file.suffix.strip('.').casefold()
