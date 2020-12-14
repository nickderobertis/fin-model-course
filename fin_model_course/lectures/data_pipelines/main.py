from courses.config import COURSES
from courses.model import CourseSelectors
from lectures.data_pipelines import notes
from lectures.model import LectureGroup
from resources.models import RESOURCES
from schedule.main import LECTURE_ADV_2_NAME


def get_data_pipelines_lecture() -> LectureGroup:
    lecture_index = 1
    title = LECTURE_ADV_2_NAME
    course = COURSES[CourseSelectors.ADVANCED]
    description = "Covers how to collect, clean, and structure the data for your model in " \
                  "an automated way, using Python."
    resources = [
        *RESOURCES.lectures.data_pipelines.resources(),
    ]
    lectures = [
        notes.get_debt_details_pipeline_lecture(),
    ]
    return LectureGroup(title, description, lectures, order=lecture_index, global_resources=resources, course=course)
