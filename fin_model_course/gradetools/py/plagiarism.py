import os
import sys
sys.path.insert(0, '..')
import env  # sets environment variables

from mosspy import Moss
import mosspy

from gradetools.config import PYTHON_FOLDER, PYTHON_PLAGIARISM_FOLDER
from gradetools.py.execute2.nbsource import source_from_notebook_path


def extract_source_from_notebooks_in_folder_output_in_out_folder(notebook_folder: str, output_folder: str):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for nb_name in next(os.walk(notebook_folder))[2]:
        if not nb_name.casefold().endswith('ipynb'):
            continue
        nb_path = os.path.join(notebook_folder, nb_name)
        out_path = os.path.join(output_folder, nb_name.rstrip('ipynb') + 'py')
        source = source_from_notebook_path(nb_path)
        with open(out_path, 'w') as f:
            f.write(source)


def generate_moss_similarity_reports(folder: str, user_id: int):
    moss, url = _send_files_in_folder_to_moss_get_url(folder, user_id)
    _download_results_from_moss_url(moss, url, folder)


def _send_files_in_folder_to_moss_get_url(folder: str, user_id: int):
    moss = Moss(user_id, 'python')
    search_path = os.path.join(folder, '*.py')
    moss.addFilesByWildcard(search_path)
    url = moss.send()
    print(f'MOSS Python plagiarism results available at: {url}')
    return moss, url


def _download_results_from_moss_url(moss: Moss, url: str, results_base_folder: str):
    report_folder = os.path.join(results_base_folder, 'Reports')
    summary_path = os.path.join(results_base_folder, 'report.html')
    moss.saveWebPage(url, summary_path)
    mosspy.download_report(url, report_folder, connections=8)


def main():
    moss_id = int(os.environ['MOSS_USER_ID'])
    extract_source_from_notebooks_in_folder_output_in_out_folder(PYTHON_FOLDER, PYTHON_PLAGIARISM_FOLDER)
    generate_moss_similarity_reports(PYTHON_PLAGIARISM_FOLDER, moss_id)


if __name__ == '__main__':
    main()
