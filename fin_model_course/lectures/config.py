from typing import List

from lectures.intro.main import get_intro_lecture
from lectures.model import LectureGroup


def get_lecture_groups() -> List[LectureGroup]:
    return [
        get_intro_lecture()
    ]