from lectures.basic_qa import notes
from lectures.model import LectureGroup
from resources.models import RESOURCES
from schedule.main import LECTURE_13_NAME


def get_basic_q_and_a_lecture() -> LectureGroup:
    lecture_index = 13
    title = LECTURE_13_NAME
    description = 'Answers to student questions about Financial Modeling with Python and Excel'
    resources = [
        *RESOURCES.lectures.basic_qa.resources()
    ]
    lectures = [
        notes.get_finstmt_q_a_12_14_2020_lecture(),
        notes.get_project_4_q_a_12_14_2020_lecture(),
    ]
    return LectureGroup(title, description, lectures, order=lecture_index, global_resources=resources)
