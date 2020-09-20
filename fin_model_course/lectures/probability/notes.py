from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES


def get_intro_probabilistic_modeling_lecture() -> Lecture:
    title = 'Introduction to Probabilistic Modeling'
    youtube_id = ''
    week_covered = 7
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_probability_math_review_lecture() -> Lecture:
    title = 'Math Review for Probabilistic Modeling'
    youtube_id = ''
    week_covered = 7
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_intro_scenario_analysis_lecture() -> Lecture:
    title = 'Introduction to Scenario Analysis'
    youtube_id = ''
    week_covered = 7
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_excel_scenario_analysis_lecture() -> Lecture:
    title = 'Scenario Analysis in Excel'
    youtube_id = ''
    week_covered = 7
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.scenario.excel.dynamic_salary_model_scenario,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_scenario_analysis_lecture() -> Lecture:
    title = 'Scenario Analysis in Python'
    youtube_id = ''
    week_covered = 8
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.scenario.python.dynamic_salary_model_scenario,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_intro_internal_randomness_lecture() -> Lecture:
    title = 'Introduction to Internal Randomness'
    youtube_id = ''
    week_covered = 8
    notes = LectureNotes([

    ], title=title)
    resources = [

    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_excel_internal_randomness_lecture() -> Lecture:
    title = 'Intro to Randomness in Excel'
    youtube_id = ''
    week_covered = 8
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.internal_randomness.excel.generate_numbers,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_internal_randomness_lecture() -> Lecture:
    title = 'Intro to Randomness in Python'
    youtube_id = ''
    week_covered = 8
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.internal_randomness.python.generate_numbers,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_discrete_randomness_lecture() -> Lecture:
    title = 'Discrete Randomness'
    youtube_id = ''
    week_covered = 8
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.internal_randomness.excel.generate_numbers,
        RESOURCES.examples.internal_randomness.python.generate_numbers,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_internal_randomness_retirement_excel_lecture() -> Lecture:
    title = 'Adding Internal Randomness to an Excel Model'
    youtube_id = ''
    week_covered = 9
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.internal_randomness.excel.dynamic_salary_model_random,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_internal_randomness_retirement_python_lecture() -> Lecture:
    title = 'Adding Internal Randomness to a Python Model'
    youtube_id = ''
    week_covered = 9
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.internal_randomness.python.dynamic_salary_model_random,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_internal_randomness_lab_overview_lecture() -> Lecture:
    title = 'Internal Randomness Lab Exercises Overview'
    youtube_id = ''
    week_covered = 9
    notes = LectureNotes([

    ], title=title)
    resources = [

    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)