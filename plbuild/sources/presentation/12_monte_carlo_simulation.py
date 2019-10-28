import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

import plbuild
from plbuild.paths import images_path
from pltemplates.exercises.monte_carlo import get_monte_carlo_python_exercise
from pltemplates.frames.in_class_example import InClassExampleFrame
from pltemplates.frames.model_flowchart import (
    ModelFlowchartFrame,
    real_world_style,
    model_style,
    in_out_style
)
from pltemplates.blocks import LabBlock, InClassExampleBlock
from pltemplates.eq_with_variable_defs import EquationWithVariableDefinitions
from pltemplates.graphics.explore_params import explore_parameters_graphic
from pltemplates.hyperlink import Hyperlink


AUTHORS = ['Nick DeRobertis']
SHORT_TITLE = 'MC Sim'
SUBTITLE = 'Analyzing Probabilities of Outputs'

SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [
    ['University of Florida', 'Department of Finance, Insurance, and Real Estate'],
]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = plbuild.paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = plbuild.paths.HANDOUTS_BUILD_PATH
TITLE = 'Monte Carlo Simulation'
ORDER = 12


def get_content():
    ev_bet = (999999/1000000) * 1 + (1/1000000) * (-750001)
    xlwings_mono = pl.Monospace('xlwings')

    mc_python_lab = get_monte_carlo_python_exercise()

    return [
        pl.Section(
            [
                lp.TwoColumnGraphicDimRevealFrame(
                    [
                        [pl.Bold('Monte Carlo Simulation'), 'is a technique which allows understanding the probability '
                         'of acheiving certain outputs from a model.'],
                        'This gives the modeler a greater understanding of the likelihood of different outputs, rather '
                        'than relying on a single number',
                    ],
                    graphics=[
                        images_path('random-numbers.jpg')
                    ],
                    title='What is Monte Carlo Simulation?'
                ),
                lp.DimRevealListFrame(
                    [
                        r'Imagine you have a one-time opportunity to place a bet for \$1. ',
                        r'If you win the bet, you will receive \$2. If you lose the bet, you will lose \$750,000. '
                        r'You cannot avoid the payment by declaring bankruptcy.',
                        r'The odds of winning the bet are 999,999/1,000,000. In 1/1,000,000 you lose the \$750,000.',
                        fr'The expected profit from the bet is \${ev_bet:.2f}. Should you take it? Depends on your '
                        fr'risk tolerance.',
                        'Therefore not only the expected outcome matters, but also what other outcomes may occur and '
                        'their probabilities.'
                    ],
                    title='Why Use Monte Carlo Simulation?'
                ),
                lp.GraphicFrame(
                    explore_parameters_graphic(),
                    title='Monte Carlo Simulation in One Picture'
                ),
                lp.DimRevealListFrame(
                    [
                        'Monte Carlo simulation is carried out similarly to external scenario analysis.',
                        'The main difference is that we manually picked specific cases for the inputs with scenario '
                        'analysis.',
                        'In Monte Carlo simulation, we assign distributions to the inputs, and input values are drawn '
                        'from the distributions for each run of the model',
                        'Finally, we can fit a probability distribution to the outputs to be able to talk about the '
                        'chance of a certain outcome occurring'
                    ],
                    title='Basic Process for Monte Carlo Simulation'
                )
            ],
            title='Introduction'
        ),
        pl.Section(
            [
                lp.DimRevealListFrame(
                    [
                        'Monte Carlo simulation can be applied to any model',
                        'It is generally easier to run them in Python than in Excel.',
                        "With pure Excel, you're either going to VBA or hacking something with data tables",
                        'In Python, just loop for N iterations, each time drawing inputs, running the model, and collecting '
                        'outputs.',
                        ['We will start with a pure Python model, then move to using', xlwings_mono,
                         'to add Monte Carlo '
                         'simulations to our Excel models.'],
                    ],
                    title='Running Monte Carlo Simulations - Python or Excel?'
                ),
                lp.Frame(
                    [
                        lp.Block(
                            [
                                r'You have \$1,000 now and need to pay \$1,050 in one year. You have available to you '
                                r'two assets: a risk free asset that returns 3%, and a stock that returns 10% with a '
                                r'20% standard deviation. How much should you invest in the two assets to maximize '
                                r'your probability of having at least \$1,050 in one year?'
                            ],
                            title='An Investment Problem'
                        ),
                        pl.VFill(),
                        pl.UnorderedList(
                            [
                                lp.DimAndRevealListItems([
                                    'We must first construct the basic model which gets the portfolio value for given '
                                    'returns',
                                    'Then draw values of the stock return from a normal distribution, and run the model '
                                    'many times and visualize the outputs. ',
                                    'Then repeat this process with each weight to determine the best weight.'
                                ])
                            ]
                        )
                    ],
                    title='An Example Application'
                ),
                InClassExampleFrame(
                    [
                        'Go to Canvas and download the Jupyter notebook "MC Investment Returns.ipynb" from '
                        'Examples > Monte Carlo',
                        'I will go through this example notebook to solve the problem from the prior slide.'
                    ],
                    title='Simluating Portfolio Values',
                    block_title='Example for Simulating Portfolio Values'
                ),
                mc_python_lab.presentation_frames(),
            ],
            title='Running a First Monte Carlo Simulation',
            short_title='Run MC'
        ),

        lp.Appendix(
            [
                mc_python_lab.appendix_frames(),
            ]
        )
    ]

DOCUMENT_CLASS_KWARGS = dict(
    nav_header=True,
    toc_sections=True
)
OUTPUT_NAME = TITLE

