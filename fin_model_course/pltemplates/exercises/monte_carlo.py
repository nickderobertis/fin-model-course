import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

from pltemplates.blocks import LabBlock
from pltemplates.exercises.lab_exercise import LabExercise


def get_monte_carlo_python_exercise() -> LabExercise:
    retirement_model = pl.Monospace('RetirementModel')

    bullet_contents = [
        [
            pl.TextSize(-1),
            'Download the Advanced Retirement Model.ipynb file from Canvas Models > Retirement.',
            ['Run the contents of the notebook so you have the', retirement_model, 'defined.'],
            'You are concerned the retirement model results could be heavily affected by changes in the interest rate. '
            'Instead of fixing it at 5%, draw it from a normal distribution with mean of 5% and standard deviation of 3%.',
            'Run the model 10,000 times and collect the years to retirement results. Visualize the results. Create a '
            'table of probabilities and the minimum years to retirement we could expect with that probability. Output '
            'the chance that the years to retirement will be more than 30.'
        ],
        [
            "Continue from the first lab exercise. Now you are also concerned that you won't get the beginning "
            "salary that you were expecting. So draw that from a normal distribution with mean 60,000 and standard "
            "deviation of 10,000. ",
            "As you run the model, also store what were the interest and salary corresponding "
            "to the years to retirement. You want to see which has a greater impact on the years to retirement: "
            "interest or beginning salary. Visualize the relationship between interest and years to retirement, and "
            "the relationship between beginning salary and years to retirement. By comparing the visualizations, it "
            "should be clear which has a greater effect."
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
