"""
Project 3 allowed students to modify data files. But the bonus was to use the unmodified data files directly.
Students are submitting the data files if they have modified them, and not if they are using the original files.
Therefore need to copy in the original data files for wherever they are missing.
"""
import os
import shutil
from typing import Dict

from gradetools.project_3.config import DATA_FILE_NAMES, DATA_DIR


def copy_data_files_as_needed_for_all_folders_in_directory(dir: str) -> None:
    for folder in next(os.walk(dir))[1]:
        folder_path = os.path.join(dir, folder)
        copied = _copy_data_files_as_needed(folder_path)
        _files_copied_to_txt(copied, folder_path)


def _files_copied_to_txt(copied: Dict[str, bool], folder: str):
    copied_files = [file_name for file_name, was_copied in copied.items() if was_copied]
    if copied_files:
        file_name = ' '.join(copied_files) + '.txt'
        file_path = os.path.join(folder, file_name)
        with open(file_path, 'w') as f:
            f.write(' ')


def _copy_data_files_as_needed(dest_dir: str) -> Dict[str, bool]:
    was_copied_dict = {}
    for file_name in DATA_FILE_NAMES:
        was_copied = _copy_file_if_necessary(file_name, DATA_DIR, dest_dir)
        was_copied_dict[file_name] = was_copied
    return was_copied_dict


def _copy_file_if_necessary(file_name: str, source_dir: str, dest_dir: str) -> bool:
    source_path = os.path.join(source_dir, file_name)
    out_path = os.path.join(dest_dir, file_name)
    if os.path.exists(out_path):
        print(f'Skipping copy of {file_name} to {dest_dir} as already exists')
        return False

    shutil.copy2(source_path, out_path)
    return True

