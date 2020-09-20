import os
import pathlib

from jinja2 import Template

from build_tools.config import DOCSRC_SOURCE_PATH
from lectures.config import get_lecture_groups

OUT_FOLDER = DOCSRC_SOURCE_PATH / "lectures"
INDEX_TEMPLATE_PATH = DOCSRC_SOURCE_PATH / "index.j2.rst"
INDEX_PATH = DOCSRC_SOURCE_PATH / "index.rst"


def build_lecture_pages(
    out_folder: pathlib.Path = OUT_FOLDER,
    index_template_path: pathlib.Path = INDEX_TEMPLATE_PATH,
    index_path: pathlib.Path = INDEX_PATH,
):
    if not out_folder.exists():
        os.makedirs(out_folder)
    lecture_groups = get_lecture_groups()
    lecture_rst_paths = []
    for lg in lecture_groups:
        if not lg.has_content:
            continue
        file_path = out_folder / (lg.stub + ".rst")
        file_path.write_text(lg.to_rst())
        lecture_rst_paths.append(f"lectures/{lg.stub}")

    template = Template(index_template_path.read_text())
    index = template.render(lecture_paths=lecture_rst_paths)
    index_path.write_text(index)


if __name__ == "__main__":
    build_lecture_pages()
