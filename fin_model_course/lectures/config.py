from typing import List

from lectures.intro.main import get_intro_lecture
from lectures.model import LectureGroup
from lectures.start_python_excel.main import get_getting_started_with_python_and_excel_lecture


def get_lecture_groups() -> List[LectureGroup]:
    return [
        get_intro_lecture(),
        get_getting_started_with_python_and_excel_lecture(),
    ]