import pathlib
import shutil
from typing import Sequence

from build_tools.config import ZIP_COPY_PATHS, ZIP_FOLDER


def _copy_files_to_folder_for_zip(
    copy_paths: Sequence[pathlib.Path] = ZIP_COPY_PATHS,
    zip_folder: pathlib.Path = ZIP_FOLDER,
    ignore_exts: Sequence[str] = ('tex', 'rst', 'ipynb_checkpoints')
):
    ignore = [f'*.{ext}' for ext in ignore_exts]
    if zip_folder.exists():
        shutil.rmtree(zip_folder)
    for path in copy_paths:
        folder_name = path.stem
        shutil.copytree(path, zip_folder / folder_name, ignore=shutil.ignore_patterns(*ignore))


def _zip_folder(folder: pathlib.Path = ZIP_FOLDER):
    shutil.make_archive(folder, "zip", folder)


def generate_all_content_zip(
    copy_paths: Sequence[pathlib.Path] = ZIP_COPY_PATHS,
    zip_folder: pathlib.Path = ZIP_FOLDER,
):
    _copy_files_to_folder_for_zip(copy_paths, zip_folder)
    _zip_folder(zip_folder)


if __name__ == "__main__":
    generate_all_content_zip()
