import os
import pathlib

from build_tools.config import DOCSRC_SOURCE_PATH
from lectures.config import get_lecture_groups

OUT_FOLDER = DOCSRC_SOURCE_PATH / "lectures"


def build_lecture_pages():
    if not OUT_FOLDER.exists():
        os.makedirs(OUT_FOLDER)
    lecture_groups = get_lecture_groups()
    for lg in lecture_groups:
        file_path = OUT_FOLDER / (lg.stub + ".rst")
        file_path.write_text(lg.to_rst())


if __name__ == "__main__":
    build_lecture_pages()
