from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES


def get_intro_advanced_lecture() -> Lecture:
    title = 'Introduction to Advanced Financial Modeling'
    youtube_id = ''
    week_covered = 14
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_model_types_lecture() -> Lecture:
    title = 'Additional Types of Financial Models'
    youtube_id = ''
    week_covered = 14
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_data_pipelines_lecture() -> Lecture:
    title = 'Data Pipelines for Financial Modeling'
    youtube_id = ''
    week_covered = 14
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_math_tools_lecture() -> Lecture:
    title = 'Advanced Mathematical Tools for Financial Modeling'
    youtube_id = ''
    week_covered = 14
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_present_model_lecture() -> Lecture:
    title = 'Better Presentation of Python Financial Models'
    youtube_id = ''
    week_covered = 14
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_programming_lecture() -> Lecture:
    title = 'Programming Skills for Advanced Financial Models'
    youtube_id = ''
    week_covered = 14
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_extras_lecture() -> Lecture:
    title = 'Extra Resources for Python Financial Modeling'
    youtube_id = ''
    week_covered = 14
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)
