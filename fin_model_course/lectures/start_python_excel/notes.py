from lectures.model import LectureNotes, Lecture


def get_intro_and_problem_lecture() -> Lecture:
    title = 'Introduction and an Example Model'
    youtube_id = ''
    notes = LectureNotes([
        'Everyone should know how to solve this simple time-value of money investment problem',
        'Many would think to reach for a financial calculator and use the five keys',
        'Or to directly type some values into the =NPER function in Excel',
        'With either of these approaches, you are doing a calculation rather than building a model',
        'If you realize you need to adjust the inputs, you need to do the calculation again',
        'With a model, the calculations are linked from the inputs to the outputs, so changing the '
        'inputs changes the outputs. This increases reproducibility and efficiency.'
    ], title=title)
    return Lecture(title, notes, youtube_id=youtube_id)


def get_excel_solution_lecture() -> Lecture:
    title = 'Building a Simple Excel Model'
    youtube_id = ''
    notes = LectureNotes([
        'It is crucial that all your Excel calculations are linked together by '
        'cell references. If you hard-code values in your calculations you are '
        'just using Excel as a calculator.'
    ], title=title)
    return Lecture(title, notes, youtube_id=youtube_id)


def get_python_solution_lecture() -> Lecture:
    title = 'Building a Simple Python Model'
    youtube_id = ''
    notes = LectureNotes([

    ], title=title)
    return Lecture(title, notes, youtube_id=youtube_id)


def get_basic_iteration_lecture() -> Lecture:
    title = 'Basic Iteration'
    youtube_id = ''
    notes = LectureNotes([

    ], title=title)
    return Lecture(title, notes, youtube_id=youtube_id)


def get_excel_extending_lecture() -> Lecture:
    title = 'Extending a Simple Excel Model'
    youtube_id = ''
    notes = LectureNotes([

    ], title=title)
    return Lecture(title, notes, youtube_id=youtube_id)


def get_python_extending_lecture() -> Lecture:
    title = 'Extending a Simple Python Model'
    youtube_id = ''
    notes = LectureNotes([

    ], title=title)
    return Lecture(title, notes, youtube_id=youtube_id)


def get_lab_exercise_lecture() -> Lecture:
    title = 'Getting Started with Python and Excel Labs'
    youtube_id = ''
    notes = LectureNotes([

    ], title=title)
    return Lecture(title, notes, youtube_id=youtube_id)


def get_lecture() -> Lecture:
    title = ''
    youtube_id = ''
    notes = LectureNotes([

    ], title=title)
    return Lecture(title, notes, youtube_id=youtube_id)