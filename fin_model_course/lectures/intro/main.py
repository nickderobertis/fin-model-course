from lectures.intro import notes
from lectures.model import LectureGroup, LectureResource
from resources.models import RESOURCES
from schedule.main import LECTURE_1_NAME


def get_intro_lecture() -> LectureGroup:
    title = LECTURE_1_NAME
    lecture_index = 1
    description = 'Introduces myself, the course structure, financial modeling, the tools we will use, ' \
                  'and how to set up Python.'
    resources = [
        *RESOURCES.course_materials.resources(),
        *RESOURCES.lectures.intro.resources(),
    ]
    lectures = [
        notes.get_about_me_lecture(),
        notes.get_syllabus_lecture(),
        notes.get_what_is_financial_modeling_lecture(),
        notes.get_tools_and_skills_lecture(),
        notes.get_install_python_lecture(),
    ]
    return LectureGroup(title, description, lectures, order=lecture_index, global_resources=resources)
