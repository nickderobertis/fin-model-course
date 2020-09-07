from lectures.intro import notes
from lectures.model import LectureGroup, LectureResource


def get_intro_lecture() -> LectureGroup:
    title = 'Introduction'
    lecture_index = 1
    description = 'Introduces myself, the course structure, financial modeling, the tools we will use, ' \
                  'and how to set up Python.'
    resources = [
        LectureResource(f'Syllabus', static_url='generated/pdfs/C1 Financial Modeling Syllabus.pdf'),
        LectureResource(f'Course Schedule', static_url='generated/pdfs/C2 Course Schedule.pdf'),
        LectureResource(f'Lecture Notes - {title}', static_url='generated/pdfs/LN1 Introduction.pdf'),
        LectureResource(f'Slides - {title}', static_url='generated/pdfs/S1 Financial Modeling with Python and Excel.pdf'),
    ]
    lectures = [
        notes.get_about_me_lecture(),
        notes.get_syllabus_lecture(),
        notes.get_what_is_financial_modeling_lecture(),
        notes.get_tools_and_skills_lecture(),
        notes.get_install_python_lecture(),
    ]
    return LectureGroup(title, description, lectures, order=lecture_index, global_resources=resources)
