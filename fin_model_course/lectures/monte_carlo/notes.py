from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES


def get_intro_monte_carlo_lecture() -> Lecture:
    title = 'Introduction to Monte Carlo Simulations'
    youtube_id = ''
    week_covered = 10
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_mc_investment_returns_lecture() -> Lecture:
    title = 'Monte Carlo Investment Returns'
    youtube_id = ''
    week_covered = 10
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.monte_carlo.python.investment_returns
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_formal_mc_lecture() -> Lecture:
    title = 'Formal Introduction to Monte Carlo Simulations'
    youtube_id = ''
    week_covered = 10
    notes = LectureNotes([

    ], title=title)
    resources = [

    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_io_mc_lecture() -> Lecture:
    title = 'Analyzing Relationships with Monte Carlo Simulations'
    youtube_id = ''
    week_covered = 10
    notes = LectureNotes([

    ], title=title)
    resources = [

    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_mc_retirement_python_lecture() -> Lecture:
    title = 'Applying Monte Carlo Simulation to a Python Model'
    youtube_id = ''
    week_covered = 10
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.monte_carlo.python.dynamic_salary_model_mc,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_mc_retirement_excel_lecture() -> Lecture:
    title = 'Applying Monte Carlo Simulation to an Excel Model'
    youtube_id = ''
    week_covered = 10
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.monte_carlo.excel.dynamic_salary_model_mc,
        RESOURCES.examples.monte_carlo.excel.excel_monte_carlo_notebook,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)

