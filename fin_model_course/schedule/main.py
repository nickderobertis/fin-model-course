from schedule.models import CourseSchedule, ClassContent


def get_course_schedule() -> CourseSchedule:
    weeks = [
        ClassContent(  # week 1
            summary='Introduction to the Class, Modeling, Python, and Excel',
            lectures=[1, 2],
        ),
        ClassContent(  # week 2
            summary='Building a Full Excel Model and Python Basics',
            lectures=[3, 4],
            assigned_projects=[1],
        ),
        ClassContent(  # week 3
            summary='Python Basics, Continued',
            lectures=[4],
        ),
        ClassContent(  # week 4
            summary='Wrapping up Python Basics, and Building a Full Python Model',
            lectures=[4, 5]
        ),
        ClassContent(  # week 5
            summary='Building a Full Python Model and Visualization',
            lectures=[5, 6]
        ),
        ClassContent(  # week 6
            summary='Visualization and Sensitivity Analysis',
            lectures=[6, 7],
            projects_due=[1]
        ),
        ClassContent(  # week 7
            summary='Sensitivity Analysis',
            lectures=[7],
            assigned_projects=[2]
        ),
        ClassContent(  # week 8
            summary='Probability Modeling',
            lectures=[8],
        ),
        ClassContent(  # week 9
            summary='Probability Modeling and Combining Excel and Python',
            lectures=[8, 9]
        ),
        ClassContent(  # week 10
            summary='Monte Carlo Simulation',
            lectures=[10],
            assigned_projects=[3],
            projects_due=[2]
        ),
        ClassContent(  # week 11
            summary='Introduction to DCF Valuation and Cost of Capital Estimation',
            lectures=[11],
        ),
        ClassContent(  # week 12
            summary='Cost of Capital Estimation and Free Cash Flow Estimation',
            lectures=[11, 12],
            assigned_projects=[4],
            projects_due=[3],
        ),
        ClassContent(  # week 13
            summary='Forecasting Free Cash Flows',
            lectures=[12],
        ),
        ClassContent(  # week 14
            summary='Advanced Financial Modeling Roadmap',
            lectures=[13],
        ),
    ]

    schedule = CourseSchedule(weeks=weeks)
    return schedule