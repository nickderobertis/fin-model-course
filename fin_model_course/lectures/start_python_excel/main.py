from lectures.start_python_excel import notes
from lectures.model import LectureGroup, LectureResource
from schedule.main import LECTURE_2_NAME


def get_getting_started_with_python_and_excel_lecture() -> LectureGroup:
    title = 'Getting Started with Python and Excel'
    description = 'Discusses the basics of financial modeling in both Python and Excel. Explores a ' \
                  'simple time-value of money problem and how to build a model for it in both ' \
                  'Python and Excel.'
    resources = [
        LectureResource(f'Lecture Notes - {title}', generated_url=f'pdfs/LN2 {title}.pdf'),
        LectureResource(f'Slides - {LECTURE_2_NAME}', generated_url=f'pdfs/2 {LECTURE_2_NAME}.pdf'),
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
    return LectureGroup(title, description, lectures, resources=resources)
