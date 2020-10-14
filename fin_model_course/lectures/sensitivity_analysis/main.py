from lectures.sensitivity_analysis import notes
from lectures.model import LectureGroup
from resources.models import RESOURCES
from schedule.main import LECTURE_7_NAME


def get_sensitivity_analysis_lecture() -> LectureGroup:
    lecture_index = 7
    title = LECTURE_7_NAME
    description = 'Expand models to check the full range of inputs and see how it impacts the outputs.'
    resources = [
        *RESOURCES.lectures.sensitivity_analysis.resources(),
    ]
    lectures = [
        notes.get_parameter_exploration_intro_lecture(),
        notes.get_sensitivity_analysis_intro_lecture(),
        notes.get_sensitivity_analysis_excel_lecture(),
        notes.get_python_dictionaries_lecture(),
        notes.get_python_list_comprehensions_lecture(),
        notes.get_python_imports_lecture(),
        notes.get_python_sensitivity_analysis_lecture(),
        notes.get_python_sensitivity_analysis_retirement_lecture(),
        notes.get_python_sensitivity_analysis_lab_lecture(),
    ]
    return LectureGroup(title, description, lectures, order=lecture_index, global_resources=resources)
