import os


def remove_results_csvs_in_subfolders(grade_folder: str):
    for folder in next(os.walk(grade_folder))[1]:
        folder_path = os.path.join(grade_folder, folder)
        out_path = os.path.join(folder_path, 'results.csv')
        os.remove(out_path)