"""
Project 3 allowed students to modify data files. But the bonus was to use the unmodified data files directly.
Students are submitting the data files if they have modified them, and not if they are using the original files.
Therefore need to copy in the original data files for wherever they are missing.
"""
import os
import shutil

from gradetools.project_3.config import DATA_FILE_NAMES, DATA_DIR


def copy_data_files_as_needed_for_all_folders_in_directory(dir: str) -> None:
    for folder in next(os.walk(dir))[1]:
        folder_path = os.path.join(dir, folder)
        _copy_data_files_as_needed(folder_path)


def _copy_data_files_as_needed(dest_dir: str) -> None:
    for file_name in DATA_FILE_NAMES:
        _copy_file_if_necessary(file_name, DATA_DIR, dest_dir)


def _copy_file_if_necessary(file_name: str, source_dir: str, dest_dir: str) -> None:
    source_path = os.path.join(source_dir, file_name)
    out_path = os.path.join(dest_dir, file_name)
    if os.path.exists(out_path):
        print(f'Skipping copy of {file_name} to {dest_dir} as already exists')
        return

    shutil.copy2(source_path, out_path)

