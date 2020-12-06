from typing import Dict

from courses.model import CourseSelectors, CourseModel

COURSES: Dict[CourseSelectors, CourseModel] = {
    CourseSelectors.BASIC: CourseModel(
        title=CourseSelectors.BASIC.value,
        order=0
    ),
    CourseSelectors.ADVANCED: CourseModel(
        title=CourseSelectors.ADVANCED.value,
        order=1,
        stub='adv'
    )
}
