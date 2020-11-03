import random
import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

import plbuild
from lectures.lab_exercises.notes import get_intro_monte_carlo_lab_lecture, \
    get_python_retirement_monte_carlo_lab_lecture, get_excel_retirement_monte_carlo_lab_lecture
from lectures.monte_carlo.main import get_monte_carlo_lecture
from plbuild.paths import images_path
from pltemplates.exercises.monte_carlo import get_monte_carlo_python_exercise, get_monte_carlo_excel_exercise, \
    get_intro_monte_carlo_python_exercise
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
from schedule.main import LECTURE_10_NAME

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
TITLE = LECTURE_10_NAME
ORDER = 'S10'


def get_content():
    random.seed(1000)
    ev_bet = (999999/1000000) * 1 + (1/1000000) * (-750001)
    xlwings_mono = pl.Monospace('xlwings')
    pd_mono = pl.Monospace('pandas')
    quickstart_mono = pl.Monospace('quickstart')

    read_from_excel_example = pl.Python("""
my_value = xw.Range("G11").value  # single value
# all values in cell range
my_value = xw.Range("G11:F13").value  
# expands cell range down and left getting all values
my_values = xw.Range("G11").expand().value  
    """)

    write_to_excel_example = pl.Python("""
xw.Range("G11").value = 10
xw.Range("G11").value = [10, 11]  # horizontal
xw.Range("G11").value = [[10], [11]]  # vertical
xw.Range("G11").value = [[10, 11], [12, 13]]  # table
    """)

    ball_options = [
        'fill',
        'circle',
        'inner sep=8pt'
    ]

    blue_ball_options = ball_options + [
        'blue'
    ]

    red_ball_options = ball_options + [
        'red'
    ]

    def rand_pos():
        return random.randrange(-150, 150) / 100

    blue_nodes = [lg.Node(None, (rand_pos(), rand_pos()), options=blue_ball_options) for _ in range(10)]
    red_nodes = [lg.Node(None, (rand_pos(), rand_pos()), options=red_ball_options) for _ in range(10)]

    red_blue_ball_graphic = lg.TikZPicture(
        [
            lg.Rectangle(5, 5, shape_options=['blue', 'thick']),
            *blue_nodes,
            *red_nodes
        ]
    )

    lecture = get_monte_carlo_lecture()
    intro_mc_python_lab = get_intro_monte_carlo_lab_lecture().to_pyexlatex()
    mc_python_lab = get_python_retirement_monte_carlo_lab_lecture().to_pyexlatex()
    mc_excel_lab = get_excel_retirement_monte_carlo_lab_lecture().to_pyexlatex()

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
                        'Go to the course site and download the Jupyter notebook "MC Investment Returns.ipynb" from '
                        'Monte Carlo Examples',
                        'I will go through this example notebook to solve the problem from the prior slide.'
                    ],
                    title='Simluating Portfolio Values',
                    block_title='Example for Simulating Portfolio Values'
                ),
                pl.TextSize(-2),
                intro_mc_python_lab.presentation_frames(),
                pl.TextSize(0),
            ],
            title='Running a First Monte Carlo Simulation',
            short_title='Run MC',
        ),
        pl.Section(
            [
                lp.Frame(
                    [
                        pl.TextSize(-2),
                        'For the model given by:',
                        pl.Equation(str_eq='y = f(X)', inline=False),
                        pl.Equation(str_eq='X = [x_1, x_2, ..., x_n]', inline=False),
                        pl.UnorderedList([
                            [pl.Equation(str_eq='y:'), 'Model output'],
                            [pl.Equation(str_eq='X:'), 'Model input matrix'],
                            [pl.Equation(str_eq='x_i:'), 'Value of $i$th $x$ variable']

                        ]),
                        'To run $N$ Monte Carlo simulations, follow the following steps:',
                        pl.OrderedList([
                            ['Assign a probability distribution for each', pl.Equation(str_eq='x_i')],
                            ['For each', pl.Equation(str_eq='x_i'),
                             'randomly pick a value from its probability distribution. Store them as',
                             pl.Equation(str_eq='X_j')],
                            ['Repeat the previous step $N$ times, yielding',
                             pl.Equation(str_eq='[X_1, X_2, ..., X_N]')],
                            ['For each', pl.Equation(str_eq='X_j'), 'calculate', pl.Equation(str_eq='y_j = f(X_j)')],
                            ['Store the values of', pl.Equation(str_eq='X_j'), 'mapped to', pl.Equation(str_eq='y_j')],
                            ['Visualize and analyze', pl.Equation(str_eq='y_j'), 'versus', pl.Equation(str_eq='X_j')]
                        ])
                    ],
                    title='Monte Carlo Simulation Process'
                ),
                lp.DimRevealListFrame(
                    [
                        'There are a multitude of outputs we can get from a Monte Carlo simulation. We saw a few '
                        'already in the example.',
                        [pl.Bold('Outcome probability distributions'), 'are the main output. We saw this with two '
                         'approaches in the example, a', pl.Underline('histogram'), 'and a',
                         pl.Underline('probability table.')],
                        ['We also examined the', pl.Bold('probability of a certain outcome'), 'in whether we reached '
                         'the desired cash.'],
                        ['The last main output is examining the', pl.Bold('relationship between inputs and outputs.'),
                         'for which common approaches include', pl.Underline('scatter plots'), 'and',
                         pl.Underline('regressions.')]
                    ],
                    title='Outputs from Monte Carlo Simulation'
                ),
                lp.TwoColumnGraphicDimRevealFrame(
                    [
                        pl.TextSize(-3),
                        'The outcome probability distribution represents the chance of receiving different '
                        'outcomes from your model.',
                        'There are two main ways to visualize a probability distribution: a plot and a table.',
                        ['The plot, usually a', pl.Underline('histogram'), 'or', pl.Underline('KDE'),
                         'gives a high-level overview of the probabilities and can uncover any non-normal '
                         'features of the distribution.'],
                        ['The probability table represents the chance of receiving the given value or '
                         'lower.'],
                        'The Value at Risk (VaR) is a common measure calculated in the industry, and it represents '
                        'the probability of losing at least a certain amount. This would be a subset of this analysis '
                        'and so this analysis can be used to calculate VaR',
                    ],
                    graphics=[
                        images_path('outcome-probability-distribution.png'),
                        lt.Tabular(
                            [

                                pl.MultiColumnLabel('Probability Table', span=2),
                                lt.TopRule(),
                                lt.ValuesTable.from_list_of_lists(
                                    [
                                        ['Probability', 'Value']
                                    ]
                                ),
                                lt.TableLineSegment(0, 1),
                                lt.ValuesTable.from_list_of_lists(
                                    [
                                        ['25%', '1020'],
                                        ['50%', '1039'],
                                        ['75%', '1053']
                                    ]
                                ),
                                lt.BottomRule()

                            ],
                            align='c|c'
                        )
                    ],
                    title='Outcome Probability Distributions',
                    graphics_on_right=False,
                ),
                lp.TwoColumnGraphicDimRevealFrame(
                    [
                        'Imagine a box which contains red and blue balls. You do not know in advance how many there '
                        'are of each color.',
                        'You want to estimate the probability of getting a blue ball when pulling a ball from the box.',
                        'To evaluate this, you grab a ball, write down its color, and put it back, 1,000 times.',
                        'You pull a blue ball in 350 out of the 1,000 trials. What is the probability of getting blue?'
                    ],
                    graphics=[
                        red_blue_ball_graphic
                    ],
                    title='Probability of a Certain Outcome - A Simple Example'
                ),
                lp.DimRevealListFrame(
                    [
                        'We followed the same logic when estimating the probability of receiving our desired cash '
                        'in the investment example.',
                        pl.Equation(str_eq=fr'p = \frac{{{pl.Text("Count of positive outcomes")}}}{{{pl.Text("Count of trials")}}}'),
                        ['For the balls example, this is simply',
                         pl.Equation(str_eq=r'p = \frac{350}{1000} = 0.35'),],
                        ['In the investment example, we used', pd_mono, 'to check for each trial, whether it was a '
                         'positive outcome (made it a 1) or not (made it a 0). Then the sum is the count of '
                         'positive outcomes and so the mean is the probability.'],
                    ],
                    title='Probability of a Certain Outcome, Formally'
                ),
                lp.DimRevealListFrame(
                    [
                        'Monte Carlo simulation can also provide a more comprehensive look at the relationship between '
                        'inputs and outputs.',
                        'While sensitivity analysis can be used to estimate the relationship between an input and '
                        'output, it is usually done with other inputs at their base case',
                        'The values of inputs may affect how other inputs affect the output. E.g. for the retirement '
                        'model, an increase in interest rate increases wealth more if the initial salary was higher.',
                        'As all the inputs change each time, you can get a more realistic view of the relationship, e.g. '
                        'some trials with a higher interest rate will have high salary and some will have low salary.'
                    ],
                    title='Why Monte Carlo Simulations Help Understand Inputs vs. Outputs'
                ),
                lp.TwoColumnGraphicDimRevealFrame(
                    [
                        pl.TextSize(-1),
                        'A scatter plot is a simple way to visualize the relationship between two variables',
                        'If there is a relationship, you will see some defined pattern in the points. This may be '
                        'somewhat of an upward or downward line (linear relationship) or some other shape such '
                        'as a U (non-linear relationship).',
                        'If there is no relationship, then there will just be a random cloud of points (lower '
                        'plot) or a horizontal line.'
                    ],
                    graphics=[
                        images_path('scatter-plot-line.png'),
                        images_path('scatter-plot-no-relationship.png')
                    ],
                    graphics_on_right=False,
                    title='Visualizing the Relationship between Inputs and Outputs'
                ),
                lp.TwoColumnGraphicDimRevealFrame(
                    [
                        pl.TextSize(-2),
                        'The scatter plots help give a broad understanding of the relationship but do not answer the '
                        'question, how much will my output change if my input changes? E.g. if I earn 10,000 more '
                        'for a starting salary, how much sooner can I retire?',
                        'Simply increasing the input in your model and checking the output is not enough, because it '
                        'does not take into account how all the other variables may be changing.',
                        'Multivariate regression is a general tool which is good at answering these kinds of questions, '
                        'while taking into account all the changing inputs.'
                    ],
                    graphics=[
                        images_path('excel-multivariate-reg.png')
                    ],
                    title='Numerically Analyzing the Relationships'
                ),
                lp.DimRevealListFrame(
                    [
                        pl.TextSize(-1),
                        'The coefficient in a multivariate regression represents how much the outcome variable '
                        'changes with a one unit change in the input variable.',
                        'E.g. a coefficient of -.0002 on starting salary in explaining years to retirement would mean '
                        r'that a \$1 increase in starting salary is associated with a decrease in years to retirement by .0002 years, or '
                        r'a \$10,000 increase in starting salary is associated with a decrease in years to retirement by 2 years.',
                        'All interpretations are "all else constant", meaning that it does not consider relationships '
                        'between the inputs. E.g. if starting salary is higher because of a good economy, and interest '
                        'rates are also higher due to the good economy, the starting salary coefficient is not taking '
                        'into account the increase in interest rates.',
                        'Be careful about units. If you use decimals for percentages, you will need to multiply or '
                        'divide by 100 to get the effect in percentages.'
                    ],
                    title='How to use Multivariate Regression'
                ),
                InClassExampleFrame(
                    [
                        'I will now go through adding a Monte Carlo simulation to the Dynamic Salary Retirement '
                        'Model in Python',
                        'The completed example is on the course site in '
                        'Monte Carlo Examples',
                    ],
                    title='Adding Monte Carlo Simulation to a Formal Model',
                    block_title='Dynamic Salary Retirement with Monte Carlo'
                ),
                mc_python_lab.presentation_frames(),
            ],
            title='A More Formal Treatment of Monte Carlo Simulation',
            short_title='Formal MC',
        ),
        pl.Section(
            [
                lp.DimRevealListFrame(
                    [
                        'In pure Excel, it is much more difficult to run a Monte Carlo Simulation',
                        'Without going to VBA, typically the only way is to use a data table',
                        'A data table can be used in situations where you only want to have one or two inputs '
                        'varying at once. Just generate the random inputs and use them as the axes of the data table',
                        'If you want to vary more than two inputs, VBA or Python would be required',
                        'There are also add-ons that accomplish this but they are usually not free'
                    ],
                    title="How is it Different Running MC in Excel?"
                ),
                lp.DimRevealListFrame(
                    [
                        'The process for Monte Carlo Simulation which works for any number of variables is '
                        'very similar to what we were doing in Python.',
                        'We are still just changing the inputs, running the model, and storing the outputs from each run',
                        ['Using', xlwings_mono, 'from Python code we can change and retrieve the values of cells'],
                        'This allows us to change inputs, run the model, and store outputs, just as in Python, but running our Excel model.',
                        'We can either analyze the outputs in Python or output them back to Excel for analysis'
                    ],
                    title='Monte Carlo in Excel with More than Two Variables'
                ),
                InClassExampleFrame(
                    [
                        'Go to the course site and download the "Dynamic Salary Retirement Model.xlsx" and '
                        '"Excel Monte Carlo.ipynb" from the Monte Carlo Examples',
                        'Open up the Jupyter notebook and follow along with me',
                        'The completed Excel model is also there in case you lose track. Visualizations '
                        'were added after running the Jupyter notebook on the original Excel model.',
                    ],
                    title='Monte Carlo Excel Retirement Model',
                    block_title=f'Using {xlwings_mono} to Run Monte Carlo Simulations'
                ),
                mc_excel_lab.presentation_frames(),
            ],
            title='Monte Carlo Simulation in Excel',
            short_title='Excel MC'
        ),
        pl.PresentationAppendix(
            [
                lecture.pyexlatex_resources_frame,
                intro_mc_python_lab.appendix_frames(),
                mc_python_lab.appendix_frames(),
                mc_excel_lab.appendix_frames(),
            ]
        )
    ]

DOCUMENT_CLASS_KWARGS = dict(
    nav_header=True,
    toc_sections=True
)
OUTPUT_NAME = TITLE
