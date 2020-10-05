from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES

EXTRA_PYTHON_BASICS_RESOURCES = [
    RESOURCES.examples.intro.python.dicts_list_comp_imports_notebook,
    RESOURCES.labs.python_basics.dicts_lists_comprehensions_notebook,
]


def get_parameter_exploration_intro_lecture() -> Lecture:
    title = 'Introduction to Parameter Exploration'
    youtube_id = ''
    week_covered = 6
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_sensitivity_analysis_intro_lecture() -> Lecture:
    title = 'Introduction to Sensitivity Analysis'
    youtube_id = ''
    week_covered = 6
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_sensitivity_analysis_excel_lecture() -> Lecture:
    title = 'Sensitivity Analysis in Excel'
    youtube_id = ''
    week_covered = 6
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.intro.excel.dynamic_salary_retirement_model,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_dictionaries_lecture() -> Lecture:
    title = 'Using Python Dictionaries'
    youtube_id = ''
    week_covered = 6
    notes = LectureNotes([

    ], title=title)
    resources = [
        *EXTRA_PYTHON_BASICS_RESOURCES,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_list_comprehensions_lecture() -> Lecture:
    title = 'Python List Comprehensions - Convenient List Building'
    youtube_id = ''
    week_covered = 6
    notes = LectureNotes([

    ], title=title)
    resources = [
        *EXTRA_PYTHON_BASICS_RESOURCES,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_imports_lecture() -> Lecture:
    title = 'Python Imports and Installing Packages'
    youtube_id = ''
    week_covered = 6
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.intro.python.dicts_list_comp_imports_notebook,
        RESOURCES.external.python.imports_guide,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_sensitivity_analysis_lecture() -> Lecture:
    title = 'Introduction to Sensitivity Analysis in Python'
    youtube_id = ''
    week_covered = 7
    notes = LectureNotes([

    ], title=title)
    resources = [

    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_sensitivity_analysis_retirement_lecture() -> Lecture:
    title = 'Sensitivity Analysis in Python Example'
    youtube_id = ''
    week_covered = 7
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.intro.python.dynamic_salary_retirement_model,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)
