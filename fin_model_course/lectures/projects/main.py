from lectures.projects import notes
from lectures.model import LectureGroup, LectureResource


def get_projects_lecture() -> LectureGroup:
    lecture_index = 'PJ1'
    title = f'Projects'
    description = 'Overview of the course projects.'
    resources = [
    ]
    lectures = [
        notes.get_project_overview_lecture(),
        notes.get_project_1_lecture(),
        notes.get_project_2_lecture(),
        notes.get_project_3_lecture(),
    ]
    return LectureGroup(title, description, lectures, order=lecture_index, global_resources=resources)
