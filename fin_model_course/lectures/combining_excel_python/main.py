from lectures.combining_excel_python import notes
from lectures.model import LectureGroup
from resources.models import RESOURCES
from schedule.main import LECTURE_9_NAME


def get_combining_excel_python_lecture() -> LectureGroup:
    lecture_index = 9
    title = LECTURE_9_NAME
    description = 'Use Python from Excel and use Excel from Python. Learn to use the two tools together ' \
                  'flexibly to enable using the most effective tool for each portion of the model.'
    resources = [
        *RESOURCES.lectures.combining_excel_python.resources(),
    ]
    lectures = [
        notes.get_intro_combining_excel_python_lecture(),
        notes.get_pandas_combining_excel_python_lecture(),
        notes.get_xlwings_combining_excel_python_lecture(),
    ]
    return LectureGroup(title, description, lectures, order=lecture_index, global_resources=resources)
