from build_tools.config import LAB_FOLDER_NAME
from lectures.lab_exercise import LabExerciseLecture
from lectures.model import LectureNotes, Lecture, LectureResource, Equation
from lectures.python_basics.notes import LECTURE_4_COMMON_RESOURCES
from schedule.main import LECTURE_2_NAME, LECTURE_3_NAME, LECTURE_4_NAME, LECTURE_5_NAME, LECTURE_6_NAME, \
    LECTURE_7_NAME, LECTURE_8_NAME, LECTURE_9_NAME, LECTURE_10_NAME

LAB_LECTURE_4_COMMON_RESOURCES = [
    LECTURE_4_COMMON_RESOURCES[1],
    LectureResource(f'Slides - {LECTURE_4_NAME}',
                    static_url=f'generated/pdfs/S4 {LECTURE_4_NAME}.pdf'),
]

LAB_LECTURE_6_COMMON_RESOURCES = [
    LectureResource(f'Pandas and Visualization Labs',
                    static_url=f'{LAB_FOLDER_NAME}/Visualization/Pandas and Visualization Labs.ipynb'),
    LectureResource(f'Slides - {LECTURE_6_NAME}',
                    static_url=f'generated/pdfs/S6 {LECTURE_6_NAME}.pdf'),
]

LECTURE_7_SLIDES = LectureResource(f'Slides - {LECTURE_7_NAME}',
                    static_url=f'generated/pdfs/S7 {LECTURE_7_NAME}.pdf')
LECTURE_7_LAB_NOTEBOOK = LectureResource(f'Dictionaries, List Comprehensions, and Imports Labs',
                    static_url=f'{LAB_FOLDER_NAME}/Python Basics/Dicts and List Comprehensions Lab.ipynb')
LECTURE_7_EXAMPLE_NOTEBOOK = LectureResource(f'Dictionaries, List Comprehensions, and Imports Examples',
                    static_url=f'Examples/Introduction/Python/Python Dicts, List comprehensions, and Imports.ipynb')

LECTURE_8_SLIDES = LectureResource(f'Slides - {LECTURE_8_NAME}',
                    static_url=f'generated/pdfs/S8 {LECTURE_8_NAME}.pdf')
LECTURE_9_SLIDES = LectureResource(f'Slides - {LECTURE_9_NAME}',
                    static_url=f'generated/pdfs/S9 {LECTURE_9_NAME}.pdf')
LECTURE_10_SLIDES = LectureResource(f'Slides - {LECTURE_10_NAME}',
                    static_url=f'generated/pdfs/S10 {LECTURE_10_NAME}.pdf')

def get_simple_retirement_lab_lecture() -> LabExerciseLecture:
    title = 'Extending a Simple Retirement Model'
    short_title = 'Vary Savings Rate Lab'
    youtube_id = 'KVVabq4n-ow'
    due_week = 2
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
        LectureResource(
            'Simple Retirement Model Excel',
            static_url='Examples/Introduction/Excel/Simple Retirement Model.xlsx'
        ),
        LectureResource(
            'Simple Retirement Model Python',
            static_url='Examples/Introduction/Python/Simple Retirement Model.ipynb'
        ),
        LectureResource(f'Slides - {LECTURE_2_NAME}', static_url=f'generated/pdfs/S2 {LECTURE_2_NAME}.pdf'),
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_extend_dynamic_retirement_excel_lab_lecture() -> LabExerciseLecture:
    title = 'Determining Desired Cash in the Dynamic Salary Retirement Excel Model'
    short_title = 'Dynamic Desired Cash in Excel'
    youtube_id = 'cM3uKsHXS3M'
    due_week = 2
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
        LectureResource(
            'Dynamic Salary Retirement Model - Excel',
            static_url='Examples/Introduction/Excel/Dynamic Salary Retirement Model.xlsx'
        ),
        LectureResource(f'Slides - {LECTURE_3_NAME}',
                        static_url=f'generated/pdfs/S3 {LECTURE_3_NAME}.pdf'),
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_python_basics_conditionals_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Conditionals'
    short_title = 'Python Conditionals Lab'
    youtube_id = 'T4LK0QgPbNA'
    due_week = 2
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
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_python_basics_lists_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Lists'
    short_title = 'Python Lists Lab'
    youtube_id = 'AViA3IBpXcc'
    due_week = 3
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
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_python_basics_functions_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Functions'
    short_title = 'Python Functions Lab'
    youtube_id = 'xOxJst-SMy8'
    due_week = 3
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
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_python_basics_data_types_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Data Types'
    short_title = 'Python Data Types Lab'
    youtube_id = 'pyjfrIzdjgo'
    due_week = 3
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
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_python_basics_classes_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Classes'
    short_title = 'Python Classes Lab'
    youtube_id = 'znxtmT66UAM'
    due_week = 3
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
        LectureResource(
            'Car Class Example',
            static_url='Examples/Introduction/Python/car_example.py'
        ),
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_extend_dynamic_retirement_python_lab_lecture() -> LabExerciseLecture:
    title = 'Determining Desired Cash in the Dynamic Salary Retirement Python Model'
    short_title = 'Dynamic Desired Cash in Python'
    youtube_id = ''
    due_week = 4
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
        LectureResource(
            'Dynamic Salary Retirement Model - Python',
            static_url='Examples/Introduction/Python/Dynamic Salary Retirement Model.ipynb'
        ),
        LectureResource(f'Slides - {LECTURE_5_NAME}',
                        static_url=f'generated/pdfs/S5 {LECTURE_5_NAME}.pdf'),
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_intro_to_pandas_lab_lecture() -> LabExerciseLecture:
    title = 'Getting Started with Pandas'
    short_title = 'Intro Pandas Lab'
    youtube_id = ''
    due_week = 5
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
        *LAB_LECTURE_6_COMMON_RESOURCES
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_pandas_styling_lab_lecture() -> LabExerciseLecture:
    title = 'Styling Pandas DataFrames'
    short_title = 'Pandas Styling Lab'
    youtube_id = ''
    due_week = 5
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
        *LAB_LECTURE_6_COMMON_RESOURCES
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_intro_python_visualization_lab_lecture() -> LabExerciseLecture:
    title = 'Introduction to Graphing with Pandas'
    short_title = 'Intro Visualization Lab'
    youtube_id = ''
    due_week = 5
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
        *LAB_LECTURE_6_COMMON_RESOURCES
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_sensitivity_analysis_excel_lab_lecture() -> LabExerciseLecture:
    title = 'Adding Sensitivity Analysis to Project 1 - Excel'
    short_title = 'Sensitivity Analysis in Excel Lab'
    youtube_id = ''
    due_week = 6
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
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_dictionaries_lab_lecture() -> LabExerciseLecture:
    title = 'Learning How to Use Dictionaries'
    short_title = 'Dictionaries Lab'
    youtube_id = ''
    due_week = 6
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
        LECTURE_7_LAB_NOTEBOOK,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_list_comprehensions_lab_lecture() -> LabExerciseLecture:
    title = 'Learning How to Use List Comprehensions'
    short_title = 'List Comprehensions Lab'
    youtube_id = ''
    due_week = 6
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
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_sensitivity_analysis_python_lab_lecture() -> LabExerciseLecture:
    title = 'Adding Sensitivity Analysis to Project 1 - Python'
    short_title = 'Sensitivity Analysis in Python Lab'
    youtube_id = ''
    due_week = 7
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
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_scenario_analysis_excel_lab_lecture() -> LabExerciseLecture:
    title = 'Adding Scenario Analysis to Project 1 - Excel'
    short_title = 'Scenario Analysis Excel Lab'
    youtube_id = ''
    due_week = 7
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
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_scenario_analysis_python_lab_lecture() -> LabExerciseLecture:
    title = 'Adding Scenario Analysis to Project 1 - Python'
    short_title = 'Scenario Analysis Python Lab'
    youtube_id = ''
    due_week = 8
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
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_randomness_excel_lab_lecture() -> LabExerciseLecture:
    title = 'Generating and Visualizing Random Numbers - Excel'
    short_title = 'Randomness Excel Lab'
    youtube_id = ''
    due_week = 8
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
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_randomness_python_lab_lecture() -> LabExerciseLecture:
    title = 'Generating and Visualizing Random Numbers - Python'
    short_title = 'Randomness Python Lab'
    youtube_id = ''
    due_week = 8
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
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_random_stock_model_lab_lecture() -> LabExerciseLecture:
    title = 'Generating and Visualizing Random Numbers - Python'
    short_title = 'Randomness Python Lab'
    youtube_id = ''
    due_week = 8
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
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_extend_model_internal_randomness_lab_lecture() -> LabExerciseLecture:
    title = 'Extending the Dynamic Salary Retirement Model with Internal Randomness'
    short_title = 'Internal Randomness Model Lab'
    youtube_id = ''
    due_week = 9
    bullets = [
        [
            "Add internal randomness to your Project 1 Excel and Python models",
            "We will relax the assumption that there is a single investment return which holds for every period",
            "Instead we will now assume that investment returns are drawn from a normal distribution",
            "For baseline values of the inputs, you can use a 4% mean and 3% standard deviation",
            "You should be able to run the model repeatedly and see different years to retirement each time"
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
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_read_write_excel_pandas_lab_lecture() -> LabExerciseLecture:
    title = 'Reading and Writing to Excel with Pandas'
    short_title = 'Read Write Pandas Lab'
    youtube_id = ''
    due_week = 9
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
        LectureResource(f'MSFT Financials',
                        static_url=f'{LAB_FOLDER_NAME}/Connecting Python and Excel/pandas/MSFT Financials.xls'),
        LectureResource(f'Read Write Excel Pandas Notebook',
                        static_url=f'Examples/Connecting Python and Excel/pandas/Read Write Excel Pandas.ipynb'),
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_read_write_xlwings_lab_lecture() -> LabExerciseLecture:
    title = 'Reading and Writing to Excel with xlwings'
    short_title = 'Read Write xlwings Lab'
    youtube_id = ''
    due_week = 9
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
        LectureResource(f'xlwings Lab',
                        static_url=f'{LAB_FOLDER_NAME}/Connecting Python and Excel/xlwings/xlwings Lab.xlsx'),
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_intro_monte_carlo_lab_lecture() -> LabExerciseLecture:
    title = 'Monte Carlo Simulation of DDM'
    short_title = 'Intro Monte Carlo Lab'
    youtube_id = ''
    due_week = 10
    bullets = [
        [
            'You are trying to determine the value of a mature company. The company has had stable dividend '
            'growth for a long time so you select the dividend discount model (DDM).',
            Equation(r'P = \frac{d_1}{r_s - g}'),
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
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_python_retirement_monte_carlo_lab_lecture() -> LabExerciseLecture:
    title = 'Monte Carlo Simulation of Python Models'
    short_title = 'Monte Carlo Python Lab'
    youtube_id = ''
    due_week = 10
    bullets = [
        [
            'Work off of your existing Project 1 Python model',
            'You are concerned the NPV could be heavily affected by changes in the interest rate. '
            'Instead of fixing it, draw it from a normal distribution with mean of 7% and standard deviation of 2%.',
            'Run the model 10,000 times and collect the years to retirement results. Visualize the results. Create a '
            'table of probabilities and the minimum NPV we could expect with that probability. Output '
            'the chance that the NPV will be more than \\$400,000,000.'
        ],
        [
            "Continue from the first lab exercise. Now you are also concerned that your assembly line will not be "
            "as efficient amd so the number of phones per machine will be lower. So draw that from a normal "
            "distribution with mean 100,000 and standard deviation of 20,000. ",
            "As you run the model, also store what were the interest and number of phones corresponding "
            "to the NPV. You want to see which has a greater impact on the NPV: "
            "interest or number of phones. Visualize the relationship between interest and NPV, and "
            "the relationship between beginning salary and NPV. Also run a regression "
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
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_excel_retirement_monte_carlo_lab_lecture() -> LabExerciseLecture:
    title = 'Monte Carlo Simulation of Excel Models'
    short_title = 'Monte Carlo Excel Lab'
    youtube_id = ''
    due_week = 10
    bullets = [
        [
            'You will be running Monte Carlo simulations on your existing Excel model from Project 1',
            'You are concerned that your estimate for the number of phones that will be sold is incorrect. ',
            'The number of phones should instead be drawn from a normal distribution with mean 100,000 and '
            'standard deviation of 20,000.',
            'Estimate the model 1,000 times and output the results back to Excel',
            'In Excel, visualize the results.  Create a '
            'table of probabilities and the minimum NPV we could expect with that probability. Output '
            r'the chance that the NPV will be more than \$800,000,000.'
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
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )

def get_lab_lecture() -> LabExerciseLecture:
    title = ''
    short_title = title
    youtube_id = ''
    due_week = 0
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
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )

