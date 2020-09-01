from lectures.intro import notes
from lectures.model import LectureGroup


def get_intro_lecture() -> LectureGroup:
    title = 'Introduction'
    lectures = [
        notes.get_about_me_lecture(),
        notes.get_syllabus_lecture(),
        notes.get_what_is_financial_modeling_lecture(),
        notes.get_tools_and_skills_lecture(),
        notes.get_install_python_lecture(),
    ]
    return LectureGroup(title, lectures)
