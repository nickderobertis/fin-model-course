from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES


def get_intro_combining_excel_python_lecture() -> Lecture:
    title = 'Introduction to Combining Excel and Python'
    youtube_id = ''
    week_covered = 9
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_pandas_combining_excel_python_lecture() -> Lecture:
    title = 'Combining Excel and Python using Pandas'
    youtube_id = ''
    week_covered = 9
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.connecting_python_excel.pandas.read_write_excel_pandas,
        RESOURCES.labs.connecting_python_excel.pandas.msft_financials,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_xlwings_combining_excel_python_lecture() -> Lecture:
    title = 'Combining Excel and Python using xlwings'
    youtube_id = ''
    week_covered = 9
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.connecting_python_excel.xlwings.example_notebook,
        RESOURCES.examples.connecting_python_excel.xlwings.example_workbook,
        RESOURCES.labs.connecting_python_excel.xlwings.lab_xlsx,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)
