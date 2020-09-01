"""
Canvas renames all the files upon submission and drops into a single folder.

Move each students' files into their own folder and rename to the original names
"""
import os
import re
import pathlib
import shutil

# e.g. johnsmith_956227_46792176_project2.xlsm or johnsmith_LATE_956227_46792176_project2.xlsm
FILE_PATTERN = re.compile(r'([^\W\d_]+)(_LATE)?_\d+_\d+_(.+)')

# TODO [#3]: handle , in file name
def rename_submissions(submissions_folder: str, out_folder: str):
    for file in next(os.walk(submissions_folder))[2]:
        current_path = os.path.join(submissions_folder, file)
        student_name = _name_from_file_name(file)
        original_name = _original_file_name_from_file_name(file)
        is_late = _is_late_from_file_name(file)
        current_out_folder = os.path.join(out_folder, student_name)
        out_path = os.path.join(current_out_folder, original_name)
        if not os.path.exists(current_out_folder):
            os.makedirs(current_out_folder)
        shutil.copy2(current_path, out_path)
        if is_late:
            with open(os.path.join(current_out_folder, 'LATE.txt'), 'w') as f:
                f.write('True')


def _name_from_file_name(file_name: str) -> str:
    match = FILE_PATTERN.match(file_name)
    if not match:
        raise ValueError(f'Could not match {file_name}')

    return match.group(1)


def _is_late_from_file_name(file_name: str) -> bool:
    match = FILE_PATTERN.match(file_name)
    if not match:
        raise ValueError(f'Could not match {file_name}')

    is_late_str = match.group(2)
    if is_late_str is None:
        return False
    elif is_late_str == '_LATE':
        return True
    else:
        raise ValueError(f'could not parse late string {is_late_str}')


def _original_file_name_from_file_name(file_name: str) -> str:
    match = FILE_PATTERN.match(file_name)
    if not match:
        raise ValueError(f'Could not match {file_name}')

    orig_name = match.group(3)

    # May still have dash number for resubmission such as "my project-2.xlsx"
    return _remove_dash_number_from_filename(orig_name)


def _remove_dash_number_from_filename(name: str) -> str:
    """
    Strips off the numbers added to the end of a Canvas filename from multiple submissions.

    When a student submits multiple times in Canvas, it includes only the final submission in the
    download, but it renames the file to add -1 for a second submission, -2 for a third submission, and so on.
    """
    path = pathlib.Path(name)
    base_name = path.stem
    suffix = path.suffix

    # TODO [#4]: come up with a solution that will work for 2+ digit numbers

    if not base_name[-1].isdigit():
        # Doesn't end in number, no need to strip
        return name

    # Ends in number
    if not base_name[-2] == '-':
        # Doesn't end in dash then number (e.g. -2), so must be number actually at end of name
        return name

    new_name = base_name[:-2]
    new_path = new_name + suffix
    return new_path

if __name__ == '__main__':
    in_folder = r'C:\Users\Nick\Desktop\temp for modeling\Grading\orig\submissions'
    out_folder = r'C:\Users\Nick\Desktop\temp for modeling\Grading\processed'
    rename_submissions(in_folder, out_folder)
