from typing import Dict

from courses.model import CourseSelectors, CourseModel

ALL_COURSE_TAGS = ('Finance', 'Modeling', 'Financial Modeling', 'Analysis', 'Python')

COURSES: Dict[CourseSelectors, CourseModel] = {
    CourseSelectors.BASIC: CourseModel(
        title=CourseSelectors.BASIC.value,
        order=0,
        tags=ALL_COURSE_TAGS + ('Excel',)
    ),
    CourseSelectors.ADVANCED: CourseModel(
        title=CourseSelectors.ADVANCED.value,
        order=1,
        stub='adv',
        tags=ALL_COURSE_TAGS
    )
}
