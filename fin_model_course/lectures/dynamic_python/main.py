from lectures.dynamic_python import notes
from lectures.model import LectureGroup
from resources.models import RESOURCES
from schedule.main import LECTURE_5_NAME


def get_dynamic_salary_python_lecture() -> LectureGroup:
    lecture_index = 5
    title = LECTURE_5_NAME
    description = 'Explores building a more complex and realistic model with Python. Here we focus on ' \
                  'extending the simple retirement model to have dynamic salary growth.'
    resources = [
        *RESOURCES.lectures.depth_python.resources(),
    ]
    lectures = [
        notes.get_jupyter_structure_lecture(),
        notes.get_dynamic_salary_model_python_lecture(),
        notes.get_wealth_python_lecture(),
        notes.get_retirement_python_lecture(),
        notes.get_retirement_python_lab_exercise_lecture(),
    ]
    return LectureGroup(title, description, lectures, order=lecture_index, global_resources=resources)
