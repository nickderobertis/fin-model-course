from lectures.python_basics import notes
from lectures.model import LectureGroup, LectureResource
from schedule.main import LECTURE_4_NAME


def get_python_basics_lecture() -> LectureGroup:
    lecture_index = 4
    title = f'{LECTURE_4_NAME}'
    description = 'Aimed at building a solid foundation of technical skills in Python to enable ' \
                  'creating complex financial models solely in Python'
    resources = [
        LectureResource(f'Lecture Notes - {title}', static_url=f'generated/pdfs/LN{lecture_index} {title}.pdf'),
        LectureResource(f'Slides - {LECTURE_4_NAME}', static_url=f'generated/pdfs/S{lecture_index} {LECTURE_4_NAME}.pdf'),
    ]
    lectures = [
        notes.get_intro_structure_lecture(),
        notes.get_conditionals_lecture(),
        notes.get_lists_lecture(),
        notes.get_functions_lecture(),
        notes.get_python_data_types_lecture(),
        notes.get_python_classes_lecture(),
        notes.get_python_error_handling_lecture(),
    ]
    return LectureGroup(title, description, lectures, order=lecture_index, global_resources=resources)
