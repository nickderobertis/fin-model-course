from typing import List

from lectures.dynamic_excel.main import get_dynamic_salary_excel_lecture
from lectures.intro.main import get_intro_lecture
from lectures.model import LectureGroup
from lectures.projects.main import get_projects_lecture
from lectures.python_basics.main import get_python_basics_lecture
from lectures.start_python_excel.main import get_getting_started_with_python_and_excel_lecture


def get_lecture_groups() -> List[LectureGroup]:
    return [
        get_intro_lecture(),
        get_getting_started_with_python_and_excel_lecture(),
        get_dynamic_salary_excel_lecture(),
        get_python_basics_lecture(),
        get_projects_lecture(),
    ]