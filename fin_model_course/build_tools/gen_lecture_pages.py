import os
import pathlib
from typing import List, Dict

from jinja2 import Template

from build_tools.config import DOCSRC_SOURCE_PATH
from courses.config import COURSES

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

    all_lecture_paths: Dict[str, List[str]] = {}
    for course in COURSES.values():
        lecture_rst_paths: List[str] = []
        for lg in course.lecture_groups:
            if not lg.has_content:
                continue
            file_path = out_folder / (lg.stub + ".rst")
            file_path.write_text(lg.to_rst())
            lecture_rst_paths.append(f"lectures/{lg.stub}")
        all_lecture_paths[course.title] = lecture_rst_paths

    template = Template(index_template_path.read_text())
    index = template.render(all_lecture_paths=all_lecture_paths)
    index_path.write_text(index)


if __name__ == "__main__":
    build_lecture_pages()
