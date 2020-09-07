from lectures.start_python_excel import notes
from lectures.model import LectureGroup, LectureResource
from schedule.main import LECTURE_2_NAME


def get_getting_started_with_python_and_excel_lecture() -> LectureGroup:
    title = 'Getting Started with Python and Excel'
    lecture_index = 2
    description = 'Discusses the basics of financial modeling in both Python and Excel. Explores a ' \
                  'simple time-value of money problem and how to build a model for it in both ' \
                  'Python and Excel.'
    resources = [
        LectureResource(f'Lecture Notes - {title}', static_url=f'generated/pdfs/LN2 {title}.pdf'),
        LectureResource(f'Slides - {LECTURE_2_NAME}', static_url=f'generated/pdfs/S2 {LECTURE_2_NAME}.pdf'),
    ]
    lectures = [
        notes.get_intro_and_problem_lecture(),
        notes.get_excel_solution_lecture(),
        notes.get_python_solution_lecture(),
        notes.get_basic_iteration_lecture(),
        notes.get_excel_extending_lecture(),
        notes.get_python_extending_lecture(),
        notes.get_lab_exercise_lecture(),
    ]
    return LectureGroup(title, description, lectures, order=lecture_index, global_resources=resources)
