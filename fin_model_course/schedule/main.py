import datetime
from typing import Optional

from schedule.models import CourseSchedule, ClassContent, ScheduleProject, ScheduleLecture

COURSE_BEGIN_DATE = datetime.date(2020, 8, 31)
COURSE_END_DATE = datetime.date(2020, 12, 17)

PROJECT_1_NAME = 'Excel and Python TVM'
PROJECT_2_NAME = 'Probabilistic Loan Pricing'
PROJECT_3_NAME = 'Monte Carlo Cost of Capital'
PROJECT_4_NAME = 'Full DCF Valuation'

LECTURE_1_NAME = 'Financial Modeling with Python and Excel'
LECTURE_2_NAME = 'Getting Started with Python and Excel'
LECTURE_3_NAME = 'The Depth of a Financial Model'
LECTURE_4_NAME = 'Going Beyond an Initial Python Script'
LECTURE_5_NAME = 'The Depth of a Financial Model, Continued'
LECTURE_6_NAME = 'Understanding Complex Results'
LECTURE_7_NAME = 'Exploring the Parameter Space'
LECTURE_8_NAME = 'Probabilistic Modeling'
LECTURE_9_NAME = 'Combining Excel and Python'
LECTURE_10_NAME = 'Monte Carlo Simulation'
LECTURE_11_NAME = 'Introduction to DCF Valuation and Cost of Capital Estimation'
LECTURE_12_NAME = 'Free Cash Flow Estimation and Forecasting'
LECTURE_13_NAME = 'Advanced Financial Modeling'

SCHEDULE: Optional[CourseSchedule] = None


def get_course_schedule(use_cache: bool = True, overwrite_cache: bool = True) -> CourseSchedule:
    global SCHEDULE

    if use_cache:
        if SCHEDULE is not None:
            return SCHEDULE

    from lectures.lab_exercises.main import get_lab_exercises_lecture
    from lectures.config import get_lecture_groups

    project_1 = ScheduleProject(name=PROJECT_1_NAME, index=1)
    project_2 = ScheduleProject(name=PROJECT_2_NAME, index=2)
    project_3 = ScheduleProject(name=PROJECT_3_NAME, index=3)
    project_4 = ScheduleProject(name=PROJECT_4_NAME, index=4)

    lecture_1 = ScheduleLecture(name=LECTURE_1_NAME, index=1)
    lecture_2 = ScheduleLecture(name=LECTURE_2_NAME, index=2)
    lecture_3 = ScheduleLecture(name=LECTURE_3_NAME, index=3)
    lecture_4 = ScheduleLecture(name=LECTURE_4_NAME, index=4)
    lecture_5 = ScheduleLecture(name=LECTURE_5_NAME, index=5)
    lecture_6 = ScheduleLecture(name=LECTURE_6_NAME, index=6)
    lecture_7 = ScheduleLecture(name=LECTURE_7_NAME, index=7)
    lecture_8 = ScheduleLecture(name=LECTURE_8_NAME, index=8)
    lecture_9 = ScheduleLecture(name=LECTURE_9_NAME, index=9)
    lecture_10 = ScheduleLecture(name=LECTURE_10_NAME, index=10)
    lecture_11 = ScheduleLecture(name=LECTURE_11_NAME, index=11)
    lecture_12 = ScheduleLecture(name=LECTURE_12_NAME, index=12)
    lecture_13 = ScheduleLecture(name=LECTURE_13_NAME, index=13)

    weeks = [
        ClassContent(  # week 1
            summary='Introduction to the Class, Modeling, Python, and Excel',
            lectures=[lecture_1, lecture_2],
        ),
        ClassContent(  # week 2
            summary='Building a Full Excel Model and Python Basics',
            lectures=[lecture_3, lecture_4],
            assigned_projects=[project_1],
        ),
        ClassContent(  # week 3
            summary='Python Basics, Continued',
            lectures=[lecture_4],
        ),
        ClassContent(  # week 4
            summary='Building a Full Python Model',
            lectures=[lecture_5]
        ),
        ClassContent(  # week 5
            summary='Visualization',
            lectures=[lecture_6]
        ),
        ClassContent(  # week 6
            summary='Sensitivity Analysis',
            lectures=[lecture_7],
            projects_due=[project_1]
        ),
        ClassContent(  # week 7
            summary='Sensitivity Analysis and Probability Modeling',
            lectures=[lecture_7, lecture_8],
            assigned_projects=[project_2]
        ),
        ClassContent(  # week 8
            summary='Probability Modeling',
            lectures=[lecture_8],
        ),
        ClassContent(  # week 9
            summary='Probability Modeling and Combining Excel and Python',
            lectures=[lecture_8, lecture_9]
        ),
        ClassContent(  # week 10
            summary='Monte Carlo Simulation',
            lectures=[lecture_10],
            assigned_projects=[project_3],
            projects_due=[project_2]
        ),
        ClassContent(  # week 11
            summary='Introduction to DCF Valuation and Cost of Capital Estimation',
            lectures=[lecture_11],
        ),
        ClassContent(  # week 12
            summary='Free Cash Flow Estimation and Intro to Forecasting',
            lectures=[lecture_12],
            assigned_projects=[project_4],
        ),
        ClassContent(  # week 13
            summary='Forecasting Free Cash Flows',
            lectures=[lecture_12],
            projects_due=[project_3],
        ),
        ClassContent(  # week 14
            summary='Advanced Financial Modeling Roadmap',
            lectures=[lecture_13],
        ),
        ClassContent(  # finals week
            summary='Final Project Time',
            lectures=[],
            projects_due=[project_4]
        )
    ]

    lab_exercises = get_lab_exercises_lecture()
    lectures = get_lecture_groups(include_labs=False, include_projects=False)

    schedule = CourseSchedule(
        weeks=weeks, start_date=COURSE_BEGIN_DATE, end_date=COURSE_END_DATE, lab_exercises=lab_exercises,
        lectures=lectures,
    )

    if overwrite_cache:
        SCHEDULE = schedule

    return schedule
