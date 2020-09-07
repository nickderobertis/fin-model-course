from lectures.dynamic_excel import notes
from lectures.model import LectureGroup, LectureResource
from schedule.main import LECTURE_3_NAME


def get_dynamic_salary_excel_lecture() -> LectureGroup:
    lecture_index = 3
    title = f'{LECTURE_3_NAME} - Excel'
    description = 'Explores building a more complex and realistic model with Excel. Here we focus on ' \
                  'extending the simple retirement model to have dynamic salary growth.'
    resources = [
        LectureResource(f'Lecture Notes - {LECTURE_3_NAME}', static_url=f'generated/pdfs/LN{lecture_index} {LECTURE_3_NAME}.pdf'),
        LectureResource(f'Slides - {LECTURE_3_NAME}', static_url=f'generated/pdfs/S{lecture_index} {LECTURE_3_NAME}.pdf'),
    ]
    lectures = [
        notes.get_extending_simple_retirement_model_lecture(),
        notes.get_relaxing_salary_assumption_lecture(),
        notes.get_advanced_excel_functions_lecture(),
        notes.get_implement_dynamic_salary_excel_lecture(),
        notes.get_lab_excercise_lecture()
    ]
    return LectureGroup(title, description, lectures, order=lecture_index, global_resources=resources)
