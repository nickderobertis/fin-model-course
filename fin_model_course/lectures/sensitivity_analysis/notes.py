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
    youtube_id = 'AybxBMC7dzo'
    week_covered = 7
    notes = LectureNotes([
        'With sensitivity analysis in Python, we can get DataFrames looking similar to '
        'the tables with conditional formatting we saw in Excel',
        'We can also output hexbin plots which show the same graphically',
        'Unlike Excel, we are not limited to analyzing two inputs at once, though it still makes '
        'sense to visualize the output in pairs of inputs',
        'The basic setup with pure Python is fairly simple: use loops over the possible input '
        'values and call your model function in the loop, saving the output associated with '
        'the inputs. Changing multiple inputs at once means multiple nested loops.',
        'Then you have to add the conditional formatting or hexbin plot',
        'The sensitivity package reduces this all to a couple lines of code, regardless of '
        'how many inputs you want to look at'
    ], title=title)
    resources = [
        RESOURCES.examples.sensitivity.python.sensitivity_notebook
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_sensitivity_analysis_retirement_lecture() -> Lecture:
    title = 'Sensitivity Analysis in Python Example'
    youtube_id = '7vACMHmUjYY'
    week_covered = 7
    notes = LectureNotes([
        'Here we will focus only on using the sensitivity package rather than carrying '
        'everything out manually',
        'We need to go back and add an optional argument to the model about whether it should '
        'print the results, otherwise we will have the results printed a huge number of times '
        'as we run the sensitivity analysis',
        'The sensitivity package is made to work with functions where each input is passed '
        'separately, whereas our model function takes a single dataclass instance. To make our '
        'model function work with the sensitivity package, we need to create a wrapper function '
        'which takes the separate arguments, creates the dataclass from them, passes that into '
        'the model function and returns the result. You can copy my snippet to do this with '
        'your model.',
        'List comprehensions are a nice easy way to specify values in a range, but you can '
        'also hard-code these lists',
        'Be careful not to look at too many input values as execution could be very slow. '
        'The progress bar will tell you how '
        'many cases of the model you are running and show how long it is taking.',
        'There are a number of options to customize the output from the library. You can change '
        'the names of the inputs and results, the color map, change direction of the colors, '
        'the grid size on the hexbin plots, and the number formatting in styled DataFrames.'
    ], title=title)
    resources = [
        RESOURCES.examples.intro.python.dynamic_salary_retirement_model,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_python_sensitivity_analysis_lab_lecture() -> Lecture:
    title = 'Lab Exercise - Adding Sensitivity Analysis to Project 1 - Python'
    youtube_id = 'YtE5oRv2Ot4'
    week_covered = 7
    notes = LectureNotes([
        'The lab exercise here is the same as that we did for Excel but now just doing it '
        'in Python',
        'You are free to use the manual approach or the sensitivity package but I would recommend '
        'the sensitivity package',
        'Be sure to upgrade your sensitivity package before working on the exercise',
        'The lecture on adding sensitivity analysis to the Python Dynamic Salary Retirement model '
        'will be very helpful for this',
        'You may need to restructure your model before you can even begin adding sensitivity analysis. '
        'You must have a function which accepts the data and produces the final output from that data, and '
        'your functions must not access the overall model_data'

    ], title=title)
    resources = [
        RESOURCES.examples.intro.python.dynamic_salary_retirement_model,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)
