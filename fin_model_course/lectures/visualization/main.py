from lectures.visualization import notes
from lectures.model import LectureGroup
from resources.models import RESOURCES
from schedule.main import LECTURE_6_NAME


def get_visualization_lecture() -> LectureGroup:
    lecture_index = 6
    title = LECTURE_6_NAME
    description = 'Learn how to analyze and communicate complicated results using visualization.'
    resources = [
        *RESOURCES.lectures.visualization.resources(),
    ]
    lectures = [
        notes.get_visualization_intro_lecture(),
        notes.get_visualize_retirement_excel_lecture(),
        notes.get_intro_pandas_lecture(),
        notes.get_styling_pandas_lecture(),
        notes.get_pandas_graphing_lecture(),
        notes.get_visualize_retirement_python_lecture(),
        notes.get_visualization_lab_excercise_lecture(),
    ]
    return LectureGroup(title, description, lectures, order=lecture_index, global_resources=resources)
