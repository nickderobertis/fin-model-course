"""
Project 2 is an xlwings project and needs to have the filename project2 for both the xlsx file and py file. However
Canvas renames all the files upon submission.

Move each students' files into their own folder and rename to project2
"""
# TODO: refactor to use grsdetools.canvas.rename
import os
import re

import shutil

FILE_PATTERN = re.compile(r'([^\W\d_]+)_[\w\-_]+.([^\W\d_]+)') # e.g. johnsmith_956227_46792176_project2.xlsm


def rename_submissions(submissions_folder: str, out_folder: str):
    for file in next(os.walk(submissions_folder))[2]:
        current_path = os.path.join(submissions_folder, file)
        student_name = _name_from_file_name(file)
        extension = _extension_from_file_name(file)
        current_out_folder = os.path.join(out_folder, student_name)
        out_path = os.path.join(current_out_folder, 'project2.' + extension.lower())
        if not os.path.exists(current_out_folder):
            os.makedirs(current_out_folder)
        shutil.copy2(current_path, out_path)


def _name_from_file_name(file_name: str) -> str:
    match = FILE_PATTERN.match(file_name)
    if not match:
        raise ValueError(f'Could not match {file_name}')

    return match.group(1)


def _extension_from_file_name(file_name: str) -> str:
    match = FILE_PATTERN.match(file_name)
    if not match:
        raise ValueError(f'Could not match {file_name}')

    return match.group(2)

