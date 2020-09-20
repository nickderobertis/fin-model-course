from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES

LECTURE_4_COMMON_RESOURCES = [
    RESOURCES.examples.intro.python.basics_notebook,
    RESOURCES.labs.python_basics.python_basics_notebook,
]


def get_jupyter_structure_lecture() -> Lecture:
    title = 'Using Jupyter to Structure a Python Model'
    youtube_id = ''
    week_covered = 4
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_dynamic_salary_model_python_lecture() -> Lecture:
    title = 'Salaries in the Python Dynamic Salary Retirement Model'
    youtube_id = ''
    week_covered = 4
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.intro.python.dynamic_salary_retirement_model,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_wealth_python_lecture() -> Lecture:
    title = 'Wealth in the Python Dynamic Salary Retirement Model'
    youtube_id = ''
    week_covered = 4
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.intro.python.dynamic_salary_retirement_model,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_retirement_python_lecture() -> Lecture:
    title = 'Retirement in the Python Dynamic Salary Retirement Model'
    youtube_id = ''
    week_covered = 4
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.intro.python.dynamic_salary_retirement_model,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)