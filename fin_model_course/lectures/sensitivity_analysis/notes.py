from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES

EXTRA_PYTHON_BASICS_RESOURCES = [
    RESOURCES.examples.intro.python.dicts_list_comp_imports_notebook,
    RESOURCES.labs.python_basics.dicts_lists_comprehensions_notebook,
]


def get_parameter_exploration_intro_lecture() -> Lecture:
    title = 'Introduction to Parameter Exploration'
    youtube_id = 'IVC38ksxNfI'
    week_covered = 6
    notes = LectureNotes([
        "If you've merely done a calculation, you have a single answer and can't learn any more about the "
        "problem without redoing the calculations",
        'Instead because we are building models which can flexibly take any input and convert that into the '
        'appropriate output, it opens up a lot of possible extensions to the model',
        'This is our main focus for a large portion of the course: how can we extend any financial model to '
        'get a greater understanding of the underlying problem',
        'Sensitivity analysis is useful to understand how the full range of possible inputs affects the main '
        'results of your model',
        'Scenario analysis allows analyzing outcomes in example situations',
        'Monte Carlo Simulation allows assigning outputs to a probability distribution, which helps you '
        'understand the risk of your result',
    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_sensitivity_analysis_intro_lecture() -> Lecture:
    title = 'Introduction to Sensitivity Analysis'
    youtube_id = 'dMpQNAnIhJQ'
    week_covered = 6
    notes = LectureNotes([
        'The formal definition of sensitivity analysis may seem complicated, but all we are doing is '
        'running the model multiple times with different inputs and showing the outputs',
        'A key component of sensitivity analysis is the visualization, as now that there are many different '
        'outputs it is much easier to draw meaning from them when visualized',
    ], title=title)
    resources = []
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_sensitivity_analysis_excel_lecture() -> Lecture:
    title = 'Sensitivity Analysis in Excel'
    youtube_id = '1wECF1RjsNM'
    week_covered = 6
    notes = LectureNotes([
        'Data tables in Excel allow calculating a cell multiple times, changing some other cell. This is perfect for '
        'sensitivity analysis if we target an output cell and change an input cell',
        'One-way data tables change one input at a time, two-way data tables change two inputs at a time',
        'You are basically limited to changing two inputs at once, without doing some clever hacks',
        'Visualization rule of thumb: graph one-way data tables and use conditional formatting for two-way',
        'Conditional formatting changes the format of cells based on conditions, such as putting the largest numbers '
        'in green and the smallest in red',
        'Row input cell means that your inputs are going horizontally in a row. Column input cell means that your '
        'inputs going vertically in a column. For one-way data tables, you will use only one of the two. For '
        'two-way data tables, you will use both'
    ], title=title)
    resources = [
        RESOURCES.examples.intro.excel.dynamic_salary_retirement_model,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_dictionaries_lecture() -> Lecture:
    title = 'Using Python Dictionaries'
    youtube_id = '6Q8LvUQmykE'
    week_covered = 6
    notes = LectureNotes([
        'There are three ways to loop through dictionaries: through the keys (the default), '
        'through the values (.values()), and through '
        'both at once (.items())',
        'If you want one way to do it, just always loop through the items as you have access to '
        'both the key and the value at once',
        'Combine dictionaries using update. Add items to dictionaries with brackets and assignment. '
        'Remove items from dictionaries with pop'
    ], title=title)
    resources = [
        *EXTRA_PYTHON_BASICS_RESOURCES,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_list_comprehensions_lecture() -> Lecture:
    title = 'Python List Comprehensions - Convenient List Building'
    youtube_id = '6GpCoTG704o'
    week_covered = 6
    notes = LectureNotes([
        'List comprehensions are an example of "syntactic sugar," or a feature of a programming language '
        'which is not necessary but makes things easier (makes the programming experience "sweeter")',
        'They allow us to write simple loops made to create lists with only a single line of code'
    ], title=title)
    resources = [
        *EXTRA_PYTHON_BASICS_RESOURCES,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_imports_lecture() -> Lecture:
    title = 'Python Imports and Installing Packages'
    youtube_id = 'xSX8sg7Twqw'
    week_covered = 6
    notes = LectureNotes([
        "Import can be used for third-party and built-in packages, but also for your own code offloaded into "
        "separate files",
        "I had you install Anaconda to get Python because it includes most of the Python packages we would want "
        "to use pre-installed. So we haven't had to install any package up to now",
        "With more than 250k packages out there and only about 200 installed in Anaconda, the time will come when you "
        "need to install something",
        "It will even happen in this course because we will use some packages I have created"
    ], title=title)
    resources = [
        RESOURCES.examples.intro.python.dicts_list_comp_imports_notebook,
        RESOURCES.external.python.imports_guide,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_sensitivity_analysis_lecture() -> Lecture:
    title = 'Introduction to Sensitivity Analysis in Python'
    youtube_id = ''
    week_covered = 7
    notes = LectureNotes([

    ], title=title)
    resources = [

    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_sensitivity_analysis_retirement_lecture() -> Lecture:
    title = 'Sensitivity Analysis in Python Example'
    youtube_id = ''
    week_covered = 7
    notes = LectureNotes([

    ], title=title)
    resources = [
        RESOURCES.examples.intro.python.dynamic_salary_retirement_model,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)
