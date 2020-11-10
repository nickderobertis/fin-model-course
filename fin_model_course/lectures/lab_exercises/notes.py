import datetime
import os

import pandas as pd
import statsmodels.api as sm
import numpy as np
from finstmt import BalanceSheets, IncomeStatements, FinancialStatements

from build_tools.config import LAB_FOLDER_NAME, LAB_EXERCISES_PATH, SITE_URL
from lectures.lab_exercise import LabExerciseLecture
from lectures.model import LectureNotes, Lecture, LectureResource, Equation, Link
from lectures.python_basics.notes import LECTURE_4_COMMON_RESOURCES
from resources.models import RESOURCES
from schedule.main import LECTURE_2_NAME, LECTURE_3_NAME, LECTURE_4_NAME, LECTURE_5_NAME, LECTURE_6_NAME, \
    LECTURE_7_NAME, LECTURE_8_NAME, LECTURE_9_NAME, LECTURE_10_NAME, LECTURE_11_NAME, LECTURE_12_NAME

COURSE_SITE = Link(href=SITE_URL, display_text='the course site')

LAB_LECTURE_4_COMMON_RESOURCES = [
    LECTURE_4_COMMON_RESOURCES[1],
    RESOURCES.lectures.beyond_initial_python.slides,
]

LAB_LECTURE_6_COMMON_RESOURCES = [
    RESOURCES.labs.visualization.pandas_visualization_notebook,
    RESOURCES.lectures.visualization.slides,
]

LECTURE_7_SLIDES = RESOURCES.lectures.sensitivity_analysis.slides
LECTURE_7_LAB_NOTEBOOK = RESOURCES.labs.python_basics.dicts_lists_comprehensions_notebook
LECTURE_7_EXAMPLE_NOTEBOOK = RESOURCES.examples.intro.python.dicts_list_comp_imports_notebook

LECTURE_8_SLIDES = RESOURCES.lectures.probability.slides
LECTURE_9_SLIDES = RESOURCES.lectures.combining_excel_python.slides
LECTURE_10_SLIDES = RESOURCES.lectures.monte_carlo.slides
LECTURE_11_SLIDES = RESOURCES.lectures.dcf_cost_capital.slides
LECTURE_12_SLIDES = RESOURCES.lectures.dcf_fcf.slides

def get_simple_retirement_lab_lecture() -> LabExerciseLecture:
    title = 'Extending a Simple Retirement Model'
    short_title = 'Vary Savings Rate Lab'
    youtube_id = 'KVVabq4n-ow'
    week_covered = 2
    bullets = [
        [
            "Now we want to see the effect of savings rate on time until retirement, in addition to interest rate",
            "In both Excel and Python, calculate the years to retirement for savings rates of 10%, 25%, and 40%, "
            "and each of these cases with each of the interest rate cases, 4%, 5%, and 6%",
            f"Be sure that you drag formulas in Excel and use for loops in Python to accomplish this",
            "In total you should have 9 calculated years to retirement numbers, in each of the two models.",
        ]
    ]
    answers = [
        [
            "Martha has 61.1 years to retirement if she earns a 4% return and saves 10%.",
            "Martha has 41.0 years to retirement if she earns a 4% return and saves 25%.",
            "Martha has 31.9 years to retirement if she earns a 4% return and saves 40%.",
            "Martha has 53.3 years to retirement if she earns a 5% return and saves 10%.",
            "Martha has 36.7 years to retirement if she earns a 5% return and saves 25%.",
            "Martha has 29.0 years to retirement if she earns a 5% return and saves 40%.",
            "Martha has 47.6 years to retirement if she earns a 6% return and saves 10%.",
            "Martha has 33.4 years to retirement if she earns a 6% return and saves 25%.",
            "Martha has 26.7 years to retirement if she earns a 6% return and saves 40%.",
        ]
    ]
    resources = [
        RESOURCES.examples.intro.excel.simple_retirement_model,
        RESOURCES.examples.intro.python.simple_retirement_model,
        RESOURCES.lectures.getting_started.slides,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_extend_dynamic_retirement_excel_lab_lecture() -> LabExerciseLecture:
    title = 'Determining Desired Cash in the Dynamic Salary Retirement Excel Model'
    short_title = 'Dynamic Desired Cash in Excel'
    youtube_id = 'cM3uKsHXS3M'
    week_covered = 2
    bullets = [
        [
            'We want to relax the assumption that the amount needed in retirement is given by '
            'a fixed amount of desired cash',
            'Add new inputs to the model, "Annual Cash Spend During Retirement" and "Years in Retirement"',
            'Calculate desired cash based on interest, cash spend, and years in retirement',
            'Use the calculated desired cash in the model to determine years to retirement',

        ]
    ]
    answers = [
        [
            r'If annual spend is 40k for 25 years in retirement, \$563,757.78 should be the retirement cash and there '
            r'should be 18 years to retirement.'
        ]
    ]
    resources = [
        RESOURCES.examples.intro.excel.dynamic_salary_retirement_model,
        RESOURCES.lectures.depth_excel.slides,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_python_basics_conditionals_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Conditionals'
    short_title = 'Python Conditionals Lab'
    youtube_id = 'T4LK0QgPbNA'
    week_covered = 2
    bullets = [
        [
            f"The Jupyter notebook called Python Basics Lab contains "
            f"all of the labs for today's lecture",
            'Please complete the exercises under "Conditionals"'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        *LAB_LECTURE_4_COMMON_RESOURCES,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_python_basics_lists_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Lists'
    short_title = 'Python Lists Lab'
    youtube_id = 'AViA3IBpXcc'
    week_covered = 3
    bullets = [
        [
            "Keep working off of Python Basics Lab.ipynb",
            'Please complete the exercises under "Working with Lists"'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        *LAB_LECTURE_4_COMMON_RESOURCES,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_python_basics_functions_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Functions'
    short_title = 'Python Functions Lab'
    youtube_id = 'xOxJst-SMy8'
    week_covered = 3
    bullets = [
        [
            "Keep working off of Python Basics Lab.ipynb",
            'Please complete the exercises under "Functions"'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        *LAB_LECTURE_4_COMMON_RESOURCES,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_python_basics_data_types_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Data Types'
    short_title = 'Python Data Types Lab'
    youtube_id = 'pyjfrIzdjgo'
    week_covered = 3
    bullets = [
        [
            "Keep working off of Python Basics Lab.ipynb",
            'Please complete the exercises under "Data Types"'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        *LAB_LECTURE_4_COMMON_RESOURCES,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_python_basics_classes_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Classes'
    short_title = 'Python Classes Lab'
    youtube_id = 'znxtmT66UAM'
    week_covered = 3
    bullets = [
        [
            "Keep working off of Python Basics Lab.ipynb",
            'Make sure you have car_example.py in the same folder',
            'Please complete the exercises under "Working with Classes"'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        *LAB_LECTURE_4_COMMON_RESOURCES,
        RESOURCES.examples.intro.python.car_example,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_extend_dynamic_retirement_python_lab_lecture() -> LabExerciseLecture:
    title = 'Determining Desired Cash in the Dynamic Salary Retirement Python Model'
    short_title = 'Dynamic Desired Cash in Python'
    youtube_id = 'TotudqllyGo'
    week_covered = 4
    bullets = [
        [
            'We want to relax the assumption that the amount needed in retirement is given by '
            'a fixed amount of desired cash',
            'Start from the completed retirement model Jupyter notebook Dynamic Salary Retirement Model.ipynb',
            'Add new inputs to the model, "Annual Cash Spend During Retirement" and "Years in Retirement"',
            'Calculate desired cash based on interest, cash spend, and years in retirement',
            'Use the calculated desired cash in the model to determine years to retirement',
        ]
    ]
    answers = [
        [
            r'If annual spend is 40k for 25 years in retirement, \$563,757.78 should be the retirement cash and there '
            r'should be 18 years to retirement.'
        ]
    ]
    resources = [
        RESOURCES.examples.intro.python.dynamic_salary_retirement_model,
        RESOURCES.lectures.depth_python.slides,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_intro_to_pandas_lab_lecture() -> LabExerciseLecture:
    title = 'Getting Started with Pandas'
    short_title = 'Intro Pandas Lab'
    youtube_id = 'XYBS-XhHyHo'
    week_covered = 5
    bullets = [
        [
            'Work off of the Jupyter notebook Pandas and Visualization Labs.ipynb',
            'Complete the lab exercises in the first section entitled "Pandas"'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        *LAB_LECTURE_6_COMMON_RESOURCES,
        RESOURCES.external.visualization.pandas_official_intro,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_pandas_styling_lab_lecture() -> LabExerciseLecture:
    title = 'Styling Pandas DataFrames'
    short_title = 'Pandas Styling Lab'
    youtube_id = 'LwO9NblsC40'
    week_covered = 5
    bullets = [
        [
            'Keep working with the same lab Jupyter Notebook',
            'Complete the lab exercises in the second section entitled "Pandas Styling"'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        *LAB_LECTURE_6_COMMON_RESOURCES,
        RESOURCES.external.visualization.pandas_styling_guide,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_intro_python_visualization_lab_lecture() -> LabExerciseLecture:
    title = 'Introduction to Graphing with Pandas'
    short_title = 'Intro Visualization Lab'
    youtube_id = 'C9yYyuzZPDw'
    week_covered = 5
    bullets = [
        [
            'Keep working with the same lab Jupyter Notebook',
            'Complete the lab exercises in the final section entitled "Graphics"'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        *LAB_LECTURE_6_COMMON_RESOURCES,
        RESOURCES.external.visualization.pandas_visualization_guide,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_sensitivity_analysis_excel_lab_lecture() -> LabExerciseLecture:
    title = 'Adding Sensitivity Analysis to Project 1 - Excel'
    short_title = 'Sensitivity Analysis in Excel Lab'
    youtube_id = 'p9n8uKZOqAY'
    week_covered = 6
    bullets = [
        [
            'Add sensitivity analysis to your Excel model from Project 1',
            'See how the NPV changes when the number of machines and initial demand change',
            'Do a one-way Data Table with a graph for each of the two inputs, then a two-way '
            'data table with conditional formatting'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        LECTURE_7_SLIDES
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_dictionaries_lab_lecture() -> LabExerciseLecture:
    title = 'Learning How to Use Dictionaries'
    short_title = 'Dictionaries Lab'
    youtube_id = 'AwdowFEtoOU'
    week_covered = 6
    bullets = [
        [
            'For this Python section, lab exercises are in the Jupyter notebook '
            'Dicts and List Comprehensions Lab.ipynb',
            'Complete the exercises in the dictionaries section for now',
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        LECTURE_7_SLIDES,
        LECTURE_7_EXAMPLE_NOTEBOOK,
        RESOURCES.labs.python_basics.dicts_lists_comprehensions_notebook,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_list_comprehensions_lab_lecture() -> LabExerciseLecture:
    title = 'Learning How to Use List Comprehensions'
    short_title = 'List Comprehensions Lab'
    youtube_id = 'fEPsRi1DWdg'
    week_covered = 6
    bullets = [
        [
            'Continue working on the same Jupyter notebook from the previous lab exercise',
            'Complete the exercises in the List Comprehensions section for now',
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        LECTURE_7_SLIDES,
        LECTURE_7_EXAMPLE_NOTEBOOK,
        LECTURE_7_LAB_NOTEBOOK,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_sensitivity_analysis_python_lab_lecture() -> LabExerciseLecture:
    title = 'Adding Sensitivity Analysis to Project 1 - Python'
    short_title = 'Sensitivity Analysis in Python Lab'
    youtube_id = 'r8ly1gY3jDA'
    week_covered = 7
    bullets = [
        [
            'Add sensitivity analysis to your Python model from Project 1',
            'See how the NPV changes when the number of machines and initial demand change',
            'Output both a hex-bin plot and a styled DataFrame'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        LECTURE_7_SLIDES,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_scenario_analysis_excel_lab_lecture() -> LabExerciseLecture:
    title = 'Adding Scenario Analysis to Project 1 - Excel'
    short_title = 'Scenario Analysis Excel Lab'
    youtube_id = 'wOrBz9ddCpA'
    week_covered = 7
    bullets = [
        [
            'Add external scenario analysis to your Excel model from Project 1',
            'Create three cases, for a bad, normal, and good economy. Change the initial demand '
            'and price per phone in each of the cases. Both demand and price should be higher '
            'in better economic situations. ',
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        LECTURE_8_SLIDES
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_scenario_analysis_python_lab_lecture() -> LabExerciseLecture:
    title = 'Adding Scenario Analysis to Project 1 - Python'
    short_title = 'Scenario Analysis Python Lab'
    youtube_id = '4MDIUB1kcY4'
    week_covered = 8
    bullets = [
        [
            'Add external scenario analysis to your Python model from Project 1',
            'Create three cases, for a bad, normal, and good economy. Change the initial demand '
            'and price per phone in each of the cases. Both demand and price should be higher '
            'in better economic situations. ',
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        LECTURE_8_SLIDES
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_randomness_excel_lab_lecture() -> LabExerciseLecture:
    title = 'Generating and Visualizing Random Numbers - Excel'
    short_title = 'Randomness Excel Lab'
    youtube_id = 'dxCFS4dQqVo'
    week_covered = 8
    bullets = [
        [
            'Complete the following excercise in Excel for n=10 and n=1000',
            'Generate n values between 0 and 1 with a uniform distribution',
            'Generate n values from a normal distribution with a 0.5 mean and 10 standard deviation',
            'Visualize each of the two outputs with a histogram',
            'Calculate the mean and standard deviation of each of the two sets of generated numbers',
            'Re-calculate it a few times, take note of how much the mean and standard deviation change'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        LECTURE_8_SLIDES
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_randomness_python_lab_lecture() -> LabExerciseLecture:
    title = 'Generating and Visualizing Random Numbers - Python'
    short_title = 'Randomness Python Lab'
    youtube_id = 'A42MrQL6Dz4'
    week_covered = 8
    bullets = [
        [
            'Complete the following excercise in Python for n=10 and n=1000',
            'Generate n values between 0 and 1 with a uniform distribution',
            'Generate n values from a normal distribution with a 0.5 mean and 10 standard deviation',
            'Visualize each of the two outputs with a histogram',
            'Calculate the mean and standard deviation of each of the two sets of generated numbers',
            'Re-calculate it a few times, take note of how much the mean and standard deviation change'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        LECTURE_8_SLIDES
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_random_stock_model_lab_lecture() -> LabExerciseLecture:
    title = 'Building a Simple Model of Stock Returns'
    short_title = 'Internal Randomness Simple Model Lab'
    youtube_id = 'mRiaOqoKuQQ'
    week_covered = 8
    bullets = [
        [
            'Create the following model in both Excel and Python',
            'A stock starts out priced at 100. Each period, it can either go up or down.',
            'When it goes up, it will grow by 1%. When it goes down, it will decrease by 1%.',
            'The likelihood of the stock going up is 60%, and down 40%.',
            'Build a model which shows how the stock price changes throughout time. Visualize it up to 100 periods and '
            'show the final price.'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        LECTURE_8_SLIDES
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_extend_model_internal_randomness_lab_lecture() -> LabExerciseLecture:
    title = 'Extending the Project 1 Model with Internal Randomness'
    short_title = 'Internal Randomness Model Lab'
    youtube_id = 'LBXRPocOCDs'
    week_covered = 9
    bullets = [
        [
            "Add internal randomness to your Project 1 Excel and Python models",
            "Now assume that the interest rate is drawn from a normal distribution",
            "For baseline values of the inputs, you can use a 4% mean and 3% standard deviation",
            "You should be able to run the model repeatedly and see a different NPV each time"
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        LECTURE_8_SLIDES
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_read_write_excel_pandas_lab_lecture() -> LabExerciseLecture:
    title = 'Reading and Writing to Excel with Pandas'
    short_title = 'Read Write Pandas Lab'
    youtube_id = 'Y1A39qzglik'
    week_covered = 9
    bullets = [
        [
            'Download "MSFT Financials.xls" from the course site',
            'Read the sheet "Income Statement" into a DataFrame',
            'Write the DataFrame to a new workbook, "My Data.xlsx", with the sheet '
            'name "Income Statement"'
        ],
        [
            'Use the same "MSFT Financials.xls" from the first exercise',
            'Output to five separate workbooks, named "My Data1.xlsx", "My Data2.xlsx", and so on.',
            ['Do this without writing the to_excel command multiple times']
        ],
        [
            'Note: this exercise uses the Advanced material covered in the example '
            'Jupyter notebook Read Write Excel Pandas.ipynb',
            ['Use the same "MSFT Financials.xls" from the first exercise'],
            'Output to five separate sheets in the same workbook "My Data.xlsx". The sheets should '
            'be named "Income Statement 1", "Income Statement 2", and so on.',
            ['Do this without writing the to_excel command multiple times']
        ]
    ]
    answers = [
        [], [], []
    ]
    resources = [
        LECTURE_9_SLIDES,
        RESOURCES.labs.connecting_python_excel.pandas.msft_financials,
        RESOURCES.examples.connecting_python_excel.pandas.read_write_excel_pandas,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_read_write_xlwings_lab_lecture() -> LabExerciseLecture:
    title = 'Reading and Writing to Excel with xlwings'
    short_title = 'Read Write xlwings Lab'
    youtube_id = 'Jgjml7JnYwY'
    week_covered = 9
    bullets = [
        [
            ['For all of the xlwings lab exercises, work with "xlwings Lab.xlsx".'],
            ['Use xlwings to read the values in the column A and then write them beside',
             'the initial values in column B']
        ],
        [
            'Get the value in C9 and multiply it by 2.5 in Python',
        ],
        [
            'Read the table which starts in E4 into Python. Multiply the prices by 2.5, and then output '
            'back into Excel starting in cell H5.',
            'Ensure that the outputted table appears in the same format as the original (pay attention to '
            'index and header)'
        ],
        [
            'In column L, write 5, 10, 15 ... 100 spaced two cells apart, so L1 would have 5, L4 would have 10, '
            'and so on.'
        ]
    ]
    answers = [
        [], [], [], []
    ]
    resources = [
        LECTURE_9_SLIDES,
        RESOURCES.labs.connecting_python_excel.xlwings.lab_xlsx,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_intro_monte_carlo_lab_lecture() -> LabExerciseLecture:
    title = 'Monte Carlo Simulation of DDM'
    short_title = 'Intro Monte Carlo Lab'
    youtube_id = 'ZR8AiEaOEJs'
    week_covered = 10
    bullets = [
        [
            'You are trying to determine the value of a mature company. The company has had stable dividend '
            'growth for a long time so you select the dividend discount model (DDM).',
            Equation(latex=r'P = \frac{d_1}{r_s - g}'),
            r'The next dividend will be \$1, and your baseline estimates of the cost of capital and growth are '
            r'9% and 4%, respectively',
            'Write a function which is able to get the price based on values of the inputs',
            'Then you are concerned about mis-estimation of the inputs and how it could affect the price. So then '
            'assume that the growth rate has a mean of 4% but a standard deviation of 1%',
            'Visualize and summarize the resulting probability distribution of the price'
        ],
        [
            'Continue from the first lab exercise',
            'Now you are also concerned you have mis-estimated the cost of capital. So now use a mean of 9% and '
            'standard deviation of 2%, in addition to varying the growth',
            'Visualize and summarize the resulting probability distribution of the price',
            'Be careful as in some cases, the drawn cost of capital will be lower than the drawn growth rate, '
            'which breaks the DDM. You will need to modify your logic to throw out these cases.'
        ]
    ]
    answers = [
        [], [],
    ]
    resources = [
        LECTURE_10_SLIDES,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_python_retirement_monte_carlo_lab_lecture() -> LabExerciseLecture:
    title = 'Monte Carlo Simulation of Python Models'
    short_title = 'Monte Carlo Python Lab'
    youtube_id = 'CkfhvKfXR9k'
    week_covered = 10
    bullets = [
        [
            'Work off of your existing Project 1 Python model',
            'You are concerned the NPV could be heavily affected by changes in the interest rate. '
            'Instead of fixing it, draw it from a normal distribution with mean of 7% and standard deviation of 2%.',
            'Run the model 10,000 times and collect the NPV results. Visualize the results. Create a '
            'table of probabilities and the minimum NPV we could expect with that probability. Output '
            'the chance that the NPV will be more than \\$400,000,000.'
        ],
        [
            "Continue from the first lab exercise. Now you are also concerned that your assembly line will not be "
            "as efficient and so the number of phones per machine will be lower. So draw that from a normal "
            "distribution with mean 100,000 and standard deviation of 20,000. ",
            "As you run the model, also store what were the interest and number of phones corresponding "
            "to the NPV. You want to see which has a greater impact on the NPV: "
            "interest or number of phones. Visualize the relationship between interest and NPV, and "
            "the relationship between number of phones and NPV. Also run a regression "
            "to quantitatively determine which has a greater effect."
        ]
    ]
    answers = [
        [], [],
    ]
    resources = [
        LECTURE_10_SLIDES,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_excel_retirement_monte_carlo_lab_lecture() -> LabExerciseLecture:
    title = 'Monte Carlo Simulation of Excel Models'
    short_title = 'Monte Carlo Excel Lab'
    youtube_id = 'xCMov82vyD4'
    week_covered = 10
    bullets = [
        [
            'You will be running Monte Carlo simulations on your existing Excel model from Project 1',
            'You are concerned that your estimate for the number of phones that will be sold is incorrect. ',
            'The number of phones should instead be drawn from a normal distribution with mean 100,000 and '
            'standard deviation of 20,000.',
            'Estimate the model 1,000 times and output the results back to Excel',
            'In Excel, visualize the results.  Create a '
            'table of probabilities and the minimum NPV we could expect with that probability. Output '
            r'the chance that the NPV will be more than \$400,000,000.'
        ],
        [
            "Continue from the first lab exercise. Now you are also concerned that there is varying quality "
            "in the machines, so they may have a different lifespan. Draw that from a normal distribution with mean "
            "10 years and standard deviation of 2 years.",
            "As you run the model, also store what were the number of phones and machine life corresponding "
            "to the NPV, all in Excel. You want to see which has a greater impact on the NPV: "
            "number of phones or machine life. Visualize the relationship between number of phones and NPV, and "
            "the relationship between beginning machine life and NPV. Try to determine which has a greater effect."
        ]
    ]
    answers = [
        [], [],
    ]
    resources = [
        LECTURE_10_SLIDES,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_enterprise_value_lab_lecture() -> LabExerciseLecture:
    title = 'Finding Enterprise and Equity Value Given FCF and WACC'
    short_title = 'Enterprise and Equity Value Lab'
    youtube_id = 'iWEDRKSZx70'
    week_covered = 11
    bullets = [
        [
            'You are the CFO for a startup developing artificial intelligence technologies. There will be an '
            'initial research phase before making any money. Google is watching your development and will purchase '
            'the company after it is profitable.',
            r'For the first two years (years 0 and 1), the company loses \$20 million. Then there is one breakeven year, after which '
            r'the profit is \$10 million for year 3. Finally in year 4, Google purchases the company for \$70 million.',
            'The WACC for the company is 15% and it has 1 million shares outstanding. The company has \$5 million '
            'in debt and \$1 million in cash.',
            'What is the enterprise value of the stock at year 4 before Google acquires the company? '
            'What about the enterprise value today? '
            'What is the price of the stock today?'
        ],
        [
            'A pharmaceutical company developed a new drug and has 4 years to sell it before the patent expires. '
            'It forms a new company to manufacture and sell the drug. After 4 years, the company will be sold to '
            'someone that wants to continue manufacturing at the lower price. The company is just about to pay a dividend.',
            r'The new company pays a dividend of \$1 per share each year for years 0 to 3, before selling it for \$30 million in '
            r'year 4.',
            r'There are 10 million shares outstanding, \$10 million of debt and \$1 million of cash throughout the '
            r'life of the company. The WACC is 10% today.',
            'What is the enterprise value at year 4 and today? What is the price of the stock today?'
        ]
    ]
    answers = [
        [
            r'The enterprise value at year 4 is \$70 million',
            r'The enterprise value at year 0 is \$9.2 million',
            r'The equity value at year 0 is \$5.21 million so the share price is \$5.21'
        ],
        [
            r'The enterprise value at year 4 is \$30 million',
            r'The equity value at year 0 is \$48.5 million so the share price is \$4.85',
            r'The enterprise value at year 0 is \$57.5 million',
        ]
    ]
    resources = [
        LECTURE_11_SLIDES,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_dcf_cost_equity_lab_lecture() -> LabExerciseLecture:
    title = 'Finding Cost of Equity Given Historical Prices'
    short_title = 'DCF Cost of Equity Lab'
    youtube_id = 'GRlIQDVznGE'
    week_covered = 11

    risk_free = 0.02

    data_path = LAB_EXERCISES_PATH / 'DCF' / 'Cost of Equity' / 'prices.xlsx'
    df = pd.read_excel(data_path)
    returns = df.pct_change().dropna()
    returns['MRP'] = returns['Market'] - risk_free
    model = sm.OLS(returns['Asset'], sm.add_constant(returns['MRP']), hasconst=True)
    results = model.fit()
    beta = results.params['MRP']
    market_return = returns['Market'].mean()
    cost_of_equity = risk_free + beta * (market_return - risk_free)
    recession_cost_of_equity = risk_free + beta * ((market_return - 0.03) - risk_free)

    bullets = [
        [
            'Download "prices.xlsx" from the course site',
            f'Assume the risk free rate is {risk_free:.0%}',
            'What is the beta and the cost of equity for this company?',
            'If you thought there was going to be a recession, such that the average market return would be '
            '3% lower, then what would you expect the cost of equity to be?',
            'Complete this exercise with the tool of your choice.'
        ],
    ]
    answers = [
        [
            rf'The beta is {beta:.3f}',
            rf'The cost of equity is {cost_of_equity:.2%}',
            rf'The cost of equity in the recession is {recession_cost_of_equity:.2%}'
        ],
    ]
    resources = [
        LECTURE_11_SLIDES,
        RESOURCES.labs.dcf.cost_of_equity.prices_xlsx,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_dcf_cost_debt_lab_lecture() -> LabExerciseLecture:
    title = 'Finding Cost of Debt Given Financial and Market Info'
    short_title = 'DCF Cost of Debt Lab'
    youtube_id = 'ozWU9mIkXCM'
    week_covered = 11

    risk_free = 0.02

    today = datetime.datetime.today().date()
    bond_price = 1042.12
    coupon_rate = 0.07
    maturity_date = datetime.date(today.year + 3, today.month, today.day)
    par_value = 1000
    tax_rate = 0.35

    # Levels 1 exercise
    l1_pretax_cost_of_debt = np.irr(
        [-bond_price] + [coupon_rate * par_value for _ in range(3 - 1)] + [(1 + coupon_rate) * par_value])
    l1_aftertax_cost_of_debt = l1_pretax_cost_of_debt * (1 - tax_rate)

    # Level 2 exercise
    wmt_int_exp = 641
    wmt_total_debt = 74709
    wmt_ebt = 4843
    wmt_tax_paid = 1233

    wmt_tax_rate = wmt_tax_paid / wmt_ebt
    wmt_pre_tax_cd = wmt_int_exp / wmt_total_debt
    wmt_after_tax_cd = wmt_pre_tax_cd * (1 - wmt_tax_rate)

    bullets = [
        [
            rf'A chemical manufacturer has a {coupon_rate:.1%} coupon, annual pay {par_value} par value bond outstanding, priced '
            rf'at \${bond_price} on {today}.',
            f'If the bond matures on {maturity_date}, what is the '
            rf'cost of debt for this company? The tax rate is {tax_rate:.0%}.',
        ],
        [
            ['Go to', Link(href='https://stockrow.com'),
             "and search for WMT to get Walmart's financials. Calculate "
             "the cost of debt for 2019-07-31 using the financial statements approach. Note that you will also "
             "need to determine the effective tax rate using actual tax paid and EBT."]
        ],
    ]
    answers = [
        [
            f'The pre-tax cost of debt for the chemical manufacturer is {l1_pretax_cost_of_debt:.2%}',
            f'The after-tax cost of debt for the chemical manufacturer is {l1_aftertax_cost_of_debt:.2%}',
        ],
        [
            f'The pre-tax cost of debt for Walmart in 2019-07-31 is {wmt_pre_tax_cd:.2%}',
            f'The after-tax cost of debt for Walmart in 2019-07-31 is {wmt_after_tax_cd:.2%}',
        ],
    ]
    resources = [
        LECTURE_11_SLIDES,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_fcf_calculation_lab_lecture() -> LabExerciseLecture:
    title = 'Free Cash Flow Calculation'
    short_title = 'Calculate FCF Lab'
    youtube_id = ''
    week_covered = 12

    lab_1_inputs = dict(
        adjustments=100,
        change_ar=1000,
        change_inventory=500,
        change_ap=800,
        change_ppe=2000,
        dep_amort=200,
        net_income=300
    )

    lab_1_nwc = lab_1_inputs['change_ar'] + lab_1_inputs['change_inventory'] - lab_1_inputs['change_ap']
    lab_1_capex = lab_1_inputs['change_ppe'] + lab_1_inputs['dep_amort']
    lab_1_fcf = lab_1_inputs['net_income'] + lab_1_inputs['adjustments'] - lab_1_nwc - lab_1_capex

    stmt_folder = LAB_EXERCISES_PATH / 'DCF' / 'FCF'
    bs_path = os.path.join(stmt_folder, 'WMT Balance Sheet.xlsx')
    inc_path = os.path.join(stmt_folder, 'WMT Income Statement.xlsx')

    bs_df = pd.read_excel(bs_path, index_col=0)
    inc_df = pd.read_excel(inc_path, index_col=0)

    bs_data = BalanceSheets.from_df(bs_df)
    inc_data = IncomeStatements.from_df(inc_df)
    stmts = FinancialStatements(inc_data, bs_data)
    lab_2_date_1 = '2019-04-30'
    lab_2_date_2 = '2019-07-31'

    bullets = [
        [
            'Calculate free cash flow from the following information:',
            f"Net income is {lab_1_inputs['net_income']}, the total of non-cash expenditures is "
            f"{lab_1_inputs['adjustments']}, "
            f"the changes in accounts receivable, inventory, accounts payable, and PPE are {lab_1_inputs['change_ar']}, "
            f"{lab_1_inputs['change_inventory']}, {lab_1_inputs['change_ap']}, and {lab_1_inputs['change_ppe']}, "
            f"and depreciation & amortization is {lab_1_inputs['dep_amort']}."
        ],
        [
            'Load in the income statement and balance sheet data associated with Project 3, "WMT Balance Sheet.xlsx" '
            'and "WMT Income Statement.xlsx"',
            'Calculate the free cash flows from these data. Note that some items are missing in these data such as '
            'depreciation. You will just need to exclude any missing items from your calculation',
            f'Get the FCFs for {lab_2_date_1} and {lab_2_date_2}.'
        ]
    ]
    answers = [
        [
            fr'The NWC is \${lab_1_nwc:,.0f}',
            fr'The CapEx is \${lab_1_capex:,.0f}',
            fr'The FCF is \${lab_1_fcf:,.0f}'
        ],
        [
            fr'The FCF for {lab_2_date_1} is \${stmts.fcf[lab_2_date_1]:,.0f}',
            fr'The FCF for {lab_2_date_2} is \${stmts.fcf[lab_2_date_2]:,.0f}',
        ]
    ]
    resources = [
        LECTURE_12_SLIDES,
        RESOURCES.labs.dcf.fcf.wmt_balance_sheet,
        RESOURCES.labs.dcf.fcf.wmt_income_statement,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_simple_forecast_lab_lecture() -> LabExerciseLecture:
    title = 'Forecasting Simple Time-Series'
    short_title = 'Simple Forecast Lab'
    youtube_id = ''
    week_covered = 12

    # NOTE: to get answers, ran Forecast Sales COGS simple but loading in these data instead

    bullets = [
        [
            ['Go to', COURSE_SITE, 'and download "Debt Interest.xlsx"'],
            'Forecast the next value of total debt using trend regression approach',
            'Forecast the next value of interest using the four approaches (average, recent, trend reg, trend CAGR)',
            'Forecast the next value of interest using the % of total debt method, with the percentages forecasted '
            'using the four approaches (average, recent, trend reg, trend CAGR)',
        ],
    ]
    answers = [
        [
            r'The forecasted value of total debt should be \$6,867',
            r'The directly forecasted values of interest should be \$1,600, \$1,900, \$2,300, and \$2,391, '
            r'for average, recent, trend reg, trend CAGR, respectively',
            r'The % of debt forecasted values of interest should be \$2,072, \$2,139, \$2,379, and \$2,312, '
            r'for average, recent, trend reg, trend CAGR, respectively',
        ],
    ]
    resources = [
        LECTURE_12_SLIDES,
        RESOURCES.labs.dcf.forecasting.simple.debt_interest,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_complex_forecast_lab_lecture() -> LabExerciseLecture:
    title = 'Forecasting Complex Time-Series'
    short_title = 'Complex Forecast Lab'
    youtube_id = ''
    week_covered = 13

    #  NOTE: to get answers, ran Forecast Quarterly Financial Statements.ipynb but loading in these data instead

    bullets = [
        [
            ['Go to', COURSE_SITE, 'and download "CAT Balance Sheet.xlsx" and "CAT Income Statement.xlsx"'],
            'Forecast the next four periods (one year) of cash using both the Quarterly Seasonal Trend Model and '
            'the automated software approach.',
            'Plot both forecasts to see how they worked.'
        ],
    ]
    answers = [
        [
            r'The forecasted values of cash using the Quarterly Seasonal Trend Model should be \$8,454,920,455, '
            r'\$8,833,593,182, \$8,869,693,182, and \$10,251,393,182',
            r'The forecasted values of cash using the automated approach should be \$8,071,641,657, \$8,185,822,286, '
            r'\$9,132,093,865, and \$9,502,395,879'
        ],
    ]
    resources = [
        LECTURE_12_SLIDES,
        RESOURCES.labs.dcf.forecasting.complex.cat_balance_sheet,
        RESOURCES.labs.dcf.forecasting.complex.cat_income_statement,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_dcf_tv_lab_lecture() -> LabExerciseLecture:
    title = 'DCF Stock Price using Terminal Values'
    short_title = 'Terminal Values Lab'
    youtube_id = ''
    week_covered = 13

    ev_ebitda = 18.58
    ev_sales = 1.92
    ev_fcf = 11.82
    pe = 39.30

    ebitda = 1500
    sales = 7898
    shrout = 561
    fcf = 2.36 * shrout
    earnings = 232
    debt = 11631
    cash = 4867
    wacc = 0.1
    growth = 0.03

    def p_from_ev(ev):
        current_ev = np.npv(wacc, [0] + [fcf] * 4 + [fcf + ev])
        equity_value = current_ev - debt + cash
        return equity_value / shrout

    ev_from_ebitda = ev_ebitda * ebitda
    p_from_ebitda = p_from_ev(ev_from_ebitda)
    ev_from_sales = ev_sales * sales
    p_from_sales = p_from_ev(ev_from_sales)
    ev_from_fcf = ev_fcf * fcf
    p_from_fcf = p_from_ev(ev_from_fcf)

    eps = earnings / shrout
    tv_p_from_pe = pe * eps
    ev_from_pe = tv_p_from_pe * shrout
    p_from_pe = p_from_ev(ev_from_pe)

    ev_from_perp = (fcf * (1 + growth)) / (wacc - growth)
    p_from_perp = p_from_ev(ev_from_perp)

    bullets = [
        [
            'Calculate possible stock prices today for a hypothetical company. Use EV/EBITDA, EV/Sales, EV/FCF, and P/E '
            'and the perpetuity growth method to determine five different possible terminal values. '
            'You have already determined that the next 5 years '
            fr'FCFs will be \${fcf:,.0f}M. ',
            fr'EV/EBITDA is {ev_ebitda:.2f}, EV/Sales is {ev_sales:.2f}, EV/FCF is {ev_fcf:.2f}, and P/E is {pe:.2f}.',
            fr'Final period forecasted financial statement values are as follows: EBITDA is \${ebitda:,.0f}M, '
            fr'sales is \${sales:,.0f}M, and net income is \${earnings:,.0f}M',
            fr'Current period financial statement values are as follows: total debt is \${debt:,.0f}M, and '
            fr'cash is \${cash:,.0f}M',
            fr'Shares outstanding is \${shrout:,.0f}M and WACC is {wacc:.1%} for the entire time period',
            f'The terminal growth rate is {growth:.1%}',
            'You can assume the next free cash flow is one year away.'
        ],
    ]
    answers = [
        [
            'The stock prices using the five methods are as follows:',
            fr'EV/EBITDA: \${p_from_ebitda:.2f}',
            fr'EV/Sales: \${p_from_sales:.2f}',
            fr'EV/FCF: \${p_from_fcf:.2f}',
            fr'P/E: \${p_from_pe:.2f}',
            fr'Perpetuity Growth: \${p_from_perp:.2f}',
        ],
    ]
    resources = [
        LECTURE_12_SLIDES,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )


def get_lab_lecture() -> LabExerciseLecture:
    title = ''
    short_title = title
    youtube_id = ''
    week_covered = 0
    bullets = [
        [

        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [

    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, week_covered=week_covered,
    )

