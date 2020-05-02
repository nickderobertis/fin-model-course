import os
import pathlib
from enum import Enum
from typing import List, Sequence, Optional

EXCEL_EXTENSIONS = ('xlsx', 'xls', 'xlsm')
PYTHON_EXTENSIONS = ('py', 'ipynb')
HIDDEN_FILE_CHARACTERS = ('~', '.')


class ModelType(Enum):
    EXCEL = 'excel'
    PYTHON = 'python'
    COMBO = 'combination'


def detect_model_type_in_folder(folder: str, exclude_files: Optional[Sequence[str]] = None) -> ModelType:
    has_excel = False
    has_python = False
    files = [file for file in next(os.walk(folder))[2] if not file[0] in HIDDEN_FILE_CHARACTERS]
    if exclude_files is not None:
        files = [file for file in files if file not in exclude_files]

    # Handle override of model type
    manual_model_type_file = os.path.join(folder, 'model type.txt')
    if os.path.exists(manual_model_type_file):
        with open(manual_model_type_file, 'r') as f:
            contents = f.read()
        selection = contents.strip().casefold()
        if selection == 'excel':
            return ModelType.EXCEL
        if selection == 'python':
            return ModelType.PYTHON
        if selection == 'combo':
            return ModelType.COMBO
        raise ValueError(f'got unknown manual model type {selection}')

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


def get_model_file_paths_from_folder(folder: str, model_type: ModelType,
                                     exclude_files: Optional[Sequence[str]] = None) -> List[str]:
    if model_type == ModelType.COMBO:
        python_file = _get_file_of_type_from_folder(folder, ModelType.PYTHON, exclude_files=exclude_files)
        excel_file = _get_file_of_type_from_folder(folder, ModelType.EXCEL, exclude_files=exclude_files)
        return [python_file, excel_file]

    # Pure Python or pure Excel, return only that
    return [_get_file_of_type_from_folder(folder, model_type, exclude_files=exclude_files)]


def get_excel_file_from_model_files(model_files: List[str], model_type: ModelType) -> str:
    if model_type == ModelType.PYTHON:
        raise ValueError('trying to get Excel file from Python model')

    if model_type == ModelType.EXCEL:
        return model_files[0]
    else:
        # In combo, python model file comes first
        return model_files[1]


def _get_file_of_type_from_folder(folder: str, model_type: ModelType,
                                  exclude_files: Optional[Sequence[str]] = None) -> str:
    files = [file for file in next(os.walk(folder))[2] if not file[0] in HIDDEN_FILE_CHARACTERS]
    if exclude_files is not None:
        files = [file for file in files if file not in exclude_files]
    if model_type == model_type.EXCEL:
        extensions = EXCEL_EXTENSIONS
    elif model_type == model_type.PYTHON:
        extensions = PYTHON_EXTENSIONS
    else:
        raise ValueError('must pass Excel or Python model type')

    manual_selection = _get_manual_file_selection(folder, model_type)
    if manual_selection is not None:
        return manual_selection

    selected_files = [file for file in files if _get_extension(file) in extensions]
    if len(selected_files) == 0:
        raise ValueError(f'no {model_type} file found in {folder} even though model type is {model_type}')
    elif len(selected_files) > 1:
        raise ValueError(f'found more than one {model_type} file in {folder}, not clear which is model')
    return selected_files[0]


def _get_extension(file: str) -> str:
    plib_file = pathlib.Path(file)
    return plib_file.suffix.strip('.').casefold()


def _get_manual_file_selection(folder: str, model_type: ModelType) -> Optional[str]:
    file_path = os.path.join(folder, f'{model_type.value} file.txt')
    if not os.path.exists(file_path):
        return None

    # Got a manual file selection
    with open(file_path, 'r') as f:
        contents = f.read()
    return contents.strip()