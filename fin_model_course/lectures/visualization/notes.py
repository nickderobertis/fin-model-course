from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES


def get_visualization_intro_lecture() -> Lecture:
    title = 'Introduction to Visualization'
    youtube_id = ''
    week_covered = 5
    notes = LectureNotes([

    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_visualize_retirement_excel_lecture() -> Lecture:
    title = 'Visualization in Excel Example'
    youtube_id = ''
    week_covered = 5
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.visualization.excel.dynamic_salary_model_visualized,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_intro_pandas_lecture() -> Lecture:
    title = 'Introduction to Pandas'
    youtube_id = ''
    week_covered = 5
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.visualization.python.intro_pandas_notebook,
        RESOURCES.labs.visualization.pandas_visualization_notebook,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_styling_pandas_lecture() -> Lecture:
    title = 'Styling Pandas DataFrames'
    youtube_id = ''
    week_covered = 5
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.visualization.python.intro_pandas_notebook,
        RESOURCES.labs.visualization.pandas_visualization_notebook,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_pandas_graphing_lecture() -> Lecture:
    title = 'Introduction to Graphs in Python with Pandas'
    youtube_id = ''
    week_covered = 5
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.visualization.python.intro_graphics_notebook,
        RESOURCES.labs.visualization.pandas_visualization_notebook,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_visualize_retirement_python_lecture() -> Lecture:
    title = 'Visualization in Python Example'
    youtube_id = ''
    week_covered = 5
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.visualization.python.dynamic_salary_model_visualized,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)
