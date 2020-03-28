import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

from pltemplates.blocks import LabBlock
from pltemplates.exercises.lab_exercise import LabExercise


def get_intro_monte_carlo_python_exercise() -> LabExercise:
    bullet_contents = [
        [
            pl.TextSize(-2),
            'You are trying to determine the value of a mature company. The company has had stable dividend '
            'growth for a long time so you select the dividend discount model (DDM).',
            pl.Equation(str_eq=r'P = \frac{d_1}{r_s - g}'),
            r'The next dividend will be \$1, and your baseline estimates of the cost of capital and growth are '
            r'9% and 4%, respectively',
            'Write a function which is able to get the price based on values of the inputs',
            'Then you are concerned about mis-estimation of the inputs and how it could affect the price. So then '
            'assume that the growth rate has a mean of 4% but a standard deviation of 1%',
            'Visualize and summarize the resulting probability distribution of the price'
        ],
        [
            pl.TextSize(-1),
            'Continue from the first lab exercise',
            'Now you are also concerned you have mis-estimated the cost of capital. So now use a mean of 9% and '
            'standard deviation of 2%, in addition to varying the growth',
            'Visualize and summarize the resulting probability distribution of the price',
            'Be careful as in some cases, the drawn cost of capital will be lower than the drawn growth rate, '
            'which breaks the DDM. You will need to modify your logic to throw out these cases.'
        ]
    ]

    return LabExercise(
        bullet_contents,
        'Intro Monte Carlo',
        f"Monte Carlo Simulation of DDM",
        label='lab:intro-monte-carlo-python'
    )

def get_monte_carlo_python_exercise() -> LabExercise:
    retirement_model = pl.Monospace('RetirementModel')

    bullet_contents = [
        [
            pl.TextSize(-1),
            'Work off of your existing Project 1 Python model',
            'You are concerned the NPV could be heavily affected by changes in the interest rate. '
            'Instead of fixing it, draw it from a normal distribution with mean of 7% and standard deviation of 2%.',
            'Run the model 10,000 times and collect the years to retirement results. Visualize the results. Create a '
            'table of probabilities and the minimum NPV we could expect with that probability. Output '
            'the chance that the NPV will be more than \\$400,000,000.'
        ],
        [
            pl.TextSize(-1),
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

    return LabExercise(
        bullet_contents,
        'Monte Carlo Python',
        f"Monte Carlo Simulation of Python Models",
        label='lab:monte-carlo-python'
    )


def get_monte_carlo_excel_exercise() -> LabExercise:
    bullet_contents = [
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

    return LabExercise(
        bullet_contents,
        'Monte Carlo Excel',
        f"Monte Carlo Simulation of Excel Models",
        label='lab:monte-carlo-excel'
    )
