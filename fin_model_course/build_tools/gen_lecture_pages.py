import os
import pathlib

from lectures.config import get_lecture_groups

OUT_FOLDER = pathlib.Path(__file__).parent.parent.parent / "docsrc" / "source" / "lectures"


def build_lecture_pages():
    if not OUT_FOLDER.exists():
        os.makedirs(OUT_FOLDER)
    lecture_groups = get_lecture_groups()
    for lg in lecture_groups:
        file_path = OUT_FOLDER / (lg.stub + ".rst")
        file_path.write_text(lg.to_rst())


if __name__ == "__main__":
    build_lecture_pages()
