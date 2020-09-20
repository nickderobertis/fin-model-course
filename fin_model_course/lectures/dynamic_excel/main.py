from lectures.dynamic_excel import notes
from lectures.model import LectureGroup, LectureResource
from resources.models import RESOURCES
from schedule.main import LECTURE_3_NAME


def get_dynamic_salary_excel_lecture() -> LectureGroup:
    lecture_index = 3
    title = f'{LECTURE_3_NAME}'
    description = 'Explores building a more complex and realistic model with Excel. Here we focus on ' \
                  'extending the simple retirement model to have dynamic salary growth.'
    resources = [
        *RESOURCES.lectures.depth_excel.resources(),
    ]
    lectures = [
        notes.get_extending_simple_retirement_model_lecture(),
        notes.get_relaxing_salary_assumption_lecture(),
        notes.get_advanced_excel_functions_lecture(),
        notes.get_implement_dynamic_salary_excel_lecture(),
        notes.get_lab_excercise_lecture()
    ]
    return LectureGroup(title, description, lectures, order=lecture_index, global_resources=resources)
