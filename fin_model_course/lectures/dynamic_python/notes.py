from lectures.model import LectureNotes, Lecture, LectureResource
from resources.models import RESOURCES

LECTURE_4_COMMON_RESOURCES = [
    RESOURCES.examples.intro.python.basics_notebook,
    RESOURCES.labs.python_basics.python_basics_notebook,
]


def get_jupyter_structure_lecture() -> Lecture:
    title = 'Using Jupyter to Structure a Python Model'
    youtube_id = 'Zk29_tWiWGc'
    week_covered = 4
    notes = LectureNotes([
        'It can be a bit tricky in the beginning to structure Python models in Jupyter as you '
        'are dealing with two different layers of organization',
        'Jupyter gives us nicely formatted markdown cells which make it easy to organize sections '
        'of the model',
        'Markdown is actually a general markup language, not anything specific to Jupyter, and it '
        'supports a lot of features. Jupyter has their own extension to markdown which also '
        'adds LaTeX equation support',
        'Most often, you will just need section headers, bullets, and equations, and anything else '
        'you can look at a Markdown reference',
        'It is easy to add a table of contents for a Jupyter notebook and you should do this to '
        'increase the readability of your model',
        'When adding a TOC item, spaces get converted to dashes for the reference'
    ], title=title)
    resources = [
        LectureResource(
            'Markdown Basic Syntax',
            external_url='https://www.markdownguide.org/basic-syntax/'
        ),
        LectureResource(
            'Markdown Extended Syntax',
            external_url='https://www.markdownguide.org/extended-syntax/'
        ),
        LectureResource(
            'LaTeX Equations in Jupyter',
            external_url='https://medium.com/analytics-vidhya/writing-math-equations-in-jupyter-notebook-a-naive-introduction-a5ce87b9a214'
        )
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_dynamic_salary_model_python_lecture() -> Lecture:
    title = 'Salaries in the Python Dynamic Salary Retirement Model'
    youtube_id = '190Xci0yDpA'
    week_covered = 4
    notes = LectureNotes([
        'For development purposes, create a new variable data which is set equal to model_data. '
        'When you are done with the model, you will remove this.',
        'Write the logic for a function in a cell and run it to ensure it works, then move it '
        'into a function',
        'Using data in the functions while the original variable is model_data ensures that you '
        'are not accidentally accessing the overall (global) model_data when it should be the '
        'specific instance of ModelInputs being passed',
        'This may be confusing and sound like extra unnecessary steps, but setting things up '
        'this way will enable your model to be easily extended',
        'Here we will create a function which can get the salary in any given year',
        'We will write also some example code to test the function and show its results',
        'Later we will use this function in the overall calculation',
    ], title=title)
    resources = [
        RESOURCES.examples.intro.python.dynamic_salary_retirement_model,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_wealth_python_lecture() -> Lecture:
    title = 'Wealth in the Python Dynamic Salary Retirement Model'
    youtube_id = 'ACSk15RnOG0'
    week_covered = 4
    notes = LectureNotes([
        'Here we will develop two functions which comprise the wealth sub-model',
        'First create a function which determines the amount of cash saved in a given year',
        'Then create a function which determines the amount of wealth in a given year',
        'We create some example code to show how the function works, but it will actually be '
        'applied in the Retirement sub-model'
    ], title=title)
    resources = [
        RESOURCES.examples.intro.python.dynamic_salary_retirement_model,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_retirement_python_lecture() -> Lecture:
    title = 'Retirement in the Python Dynamic Salary Retirement Model'
    youtube_id = 'zHoYWl3YHJ8'
    week_covered = 4
    notes = LectureNotes([
        'Now we will bring everything together to calculate the years to retirement',
        'The salary and cash saved functions are already getting called from within the wealth '
        'function, so we only need to call the wealth function in the final loop',
        'Here we are making use of a while loop to stop the loop once a certain condition is met, in this '
        'case once wealth exceeds desired cash',
        'We will use formatted strings and new lines to create a good display for the output',
    ], title=title)
    resources = [
        RESOURCES.examples.intro.python.dynamic_salary_retirement_model,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)


def get_retirement_python_lab_exercise_lecture() -> Lecture:
    title = 'Lab Exercise'
    youtube_id = '5ruLMjkQ6C4'
    week_covered = 4
    notes = LectureNotes([
        'Feel free to work from the example model though I would recommend you '
        'build that out yourself following the prior videos',
        'This exercise is exactly the same as the one we did for Excel to calculate the '
        'desired cash rather than taking it as an input',
        'Hint: You should add the new inputs to the ModelInputs dataclass and remove the desired '
        'cash input. Then you can create a function which calculates the desired cash based on '
        'the model inputs, and use that in place of where the desired cash was being accessed '
        'directly before',
    ], title=title)
    resources = [
        RESOURCES.examples.intro.python.dynamic_salary_retirement_model,
    ]
    return Lecture(title, week_covered, notes, youtube_id=youtube_id, resources=resources)