from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES


def get_intro_and_problem_lecture() -> Lecture:
    title = 'Introduction and an Example Model'
    youtube_id = 'KL48T_XGbzI'
    week_covered = 1
    notes = LectureNotes([
        'In the beginning of the course, we will do everything with both Excel and Python to understand '
        'the differences. Later we will focus on choosing the best tool for the task at hand and '
        'the ability to combine the two tools.',
        'Everyone should know how to solve this simple time-value of money investment problem',
        'Many would think to reach for a financial calculator and use the five keys',
        'Or to directly type some values into the =NPER function in Excel',
        'With either of these approaches, you are doing a calculation rather than building a model',
        'If you realize you need to adjust the inputs, you need to do the calculation again',
        'With a model, the calculations are linked from the inputs to the outputs, so changing the '
        'inputs changes the outputs. This increases reproducibility and efficiency.'
    ], title=title)
    return Lecture(title, week_covered, notes, youtube_id=youtube_id)


def get_excel_solution_lecture() -> Lecture:
    title = 'Building a Simple Excel Model'
    youtube_id = 'hySE7wOAlfc'
    week_covered = 1
    notes = LectureNotes([
        'It is crucial that all your Excel calculations are linked together by '
        'cell references. If you hard-code values in your calculations you are '
        'just using Excel as a calculator.',
        'It is important to visually separate the inputs from the outputs. This makes '
        'it much more clear for the consumer of your model, especially in more complex models',
        'More complex models should be broken into multiple sheets with each sheet dedicated to a concept or '
        'calculation',
        'Cell formatting can be used in combination with the layout to separate them',
        'For small models, intermediate outputs/calculations may be kept in the outputs section, while '
        'for larger models it makes sense to have separate calculation sections'
    ], title=title)
    resources = [
        RESOURCES.examples.intro.excel.simple_retirement_model,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_solution_lecture() -> Lecture:
    title = 'Building a Simple Python Model'
    youtube_id = 'syrwXU1wqps'
    week_covered = 1
    notes = LectureNotes([
        'In Python, we keep things linked together by using variables. If you hard-code values in '
        'your calculations, you are just using Python as a calculator',
        'Basic math in Python is mostly what you might expect, it is the same as Excel only exponents '
        'are specified by ** and not ^',
        'Jupyter allows us to create an interactive model complete with nicely formatted text, '
        'equations, tables, graphs, etc. with relative ease',
        'Inputs should be kept at the top in a separate section, the main outputs should be kept '
        'at the bottom in a separate section. ',
        'More complex models should be broken into sections and subsections with sections dedicated to a concept or '
        'calculation',
    ], title=title)
    resources = [
        RESOURCES.examples.intro.python.simple_retirement_model,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_basic_iteration_lecture() -> Lecture:
    title = 'Basic Iteration'
    youtube_id = 'vAOrxaKnXaQ'
    week_covered = 1
    notes = LectureNotes([
        'Iteration is a key concept in financial modeling (as well as programming)',
        'Using iteration, we can complete the same process for multiple inputs to '
        'yield multiple outputs',
        'As the same process is applied to each input, the process only needs to be '
        'created once and any updates to the process can flow through all the inputs'
        'Iteration can be internal or external to the main model. You can use iteration '
        'within your model, or you can iterate the model itself',
        'To iterate in Excel, drag formulas. To iterate in Python and other '
        'programming languages, use loops.',
    ], title=title)
    return Lecture(title, week_covered, notes, youtube_id=youtube_id)


def get_excel_extending_lecture() -> Lecture:
    title = 'Extending a Simple Excel Model'
    youtube_id = 'GD34LyjvMaE'
    week_covered = 1
    notes = LectureNotes([
        'Essentially the model with iteration is the same, we just drag the formula to '
        'cover multiple inputs',
        'It is crucial to set up fixed and relative cell references appropriately before you drag formulas'
    ], title=title)
    return Lecture(title, week_covered, notes, youtube_id=youtube_id)


def get_python_extending_lecture() -> Lecture:
    title = 'Extending a Simple Python Model'
    youtube_id = 'Ejk6ektd21I'
    week_covered = 1
    notes = LectureNotes([
        'To add iteration to the Python model, just wrap the existing code in a loop',
        'We must also collect or show the output in some way, as we can no longer take advantage '
        'of the Jupyter shortcut to show the output without printing.',
    ], title=title)
    return Lecture(title, week_covered, notes, youtube_id=youtube_id)


def get_lab_exercise_lecture() -> Lecture:
    title = 'Getting Started with Python and Excel Labs'
    youtube_id = '2J-GCwSNGBw'
    week_covered = 1
    notes = LectureNotes([
        'This is our first real lab exercise (must be submitted). Be sure to complete the same exercise in '
        'both Python and Excel',
        'We often want to iterate over more than one input. Here we want to look at the pairwise combinations '
        'of the savings rate and interest rate possibilities.',
        'Excel hint: there is a nice way to lay this out so you only need to type the formula a single time',
        'Python hint: It is possible to nest loops to loop over the combination of two different inputs',
    ], title=title)
    return Lecture(title, week_covered, notes, youtube_id=youtube_id)
