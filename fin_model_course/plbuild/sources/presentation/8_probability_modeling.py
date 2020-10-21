import random

import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

import plbuild
from lectures.lab_exercises.notes import get_scenario_analysis_excel_lab_lecture, \
    get_scenario_analysis_python_lab_lecture, get_randomness_excel_lab_lecture, get_randomness_python_lab_lecture, \
    get_random_stock_model_lab_lecture, get_extend_model_internal_randomness_lab_lecture
from lectures.probability.main import get_probability_lecture
from plbuild.paths import images_path
from pltemplates.exercises.lab_exercise import LabExercise
from pltemplates.frames.in_class_example import InClassExampleFrame
from pltemplates.frames.model_flowchart import (
    ModelFlowchartFrame,
    real_world_style,
    model_style,
    in_out_style
)
from pltemplates.blocks import LabBlock
from pltemplates.eq_with_variable_defs import EquationWithVariableDefinitions
from pltemplates.graphics.internal_randomness import internal_randomness_graphic
from pltemplates.hyperlink import Hyperlink
from schedule.main import LECTURE_8_NAME

AUTHORS = ['Nick DeRobertis']
SHORT_TITLE = 'Probability'
SUBTITLE = 'How to Incorporate Probability into Financial Models'

SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [
    ['University of Florida', 'Department of Finance, Insurance, and Real Estate'],
]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = plbuild.paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = plbuild.paths.HANDOUTS_BUILD_PATH
TITLE = LECTURE_8_NAME
ORDER = 'S8'


def get_content():
    random.seed(1000)

    lecture = get_probability_lecture()
    scenario_excel_lab = get_scenario_analysis_excel_lab_lecture().to_pyexlatex()
    scenario_python_lab = get_scenario_analysis_python_lab_lecture().to_pyexlatex()
    randomness_excel_lab = get_randomness_excel_lab_lecture().to_pyexlatex()
    randomness_python_lab = get_randomness_python_lab_lecture().to_pyexlatex()
    random_stock_lab = get_random_stock_model_lab_lecture().to_pyexlatex()
    full_model_internal_randomness_lab = get_extend_model_internal_randomness_lab_lecture().to_pyexlatex()
    appendix_frames = [
        lecture.pyexlatex_resources_frame,
        scenario_excel_lab.appendix_frames(),
        scenario_python_lab.appendix_frames(),
        randomness_excel_lab.appendix_frames(),
        randomness_python_lab.appendix_frames(),
        random_stock_lab.appendix_frames(),
        full_model_internal_randomness_lab.appendix_frames(),
    ]

    df_mono = pl.Monospace('DataFrame')
    next_slide = lp.Overlay([lp.NextWithIncrement()])
    with_previous = lp.Overlay([lp.NextWithoutIncrement()])
    rand_mono = pl.Monospace('=RAND')
    rand_between_mono = pl.Monospace('=RANDBETWEEN')
    norm_inv_mono = pl.Monospace('=NORM.INV')
    excel_random_normal_example = pl.Monospace('=NORM.INV(RAND(), 10, 1)')
    random_module_mono = pl.Monospace('random')
    py_rand_mono = pl.Monospace('random.random')
    py_rand_uniform_mono = pl.Monospace('random.uniform')
    py_rand_norm_mono = pl.Monospace('random.normalvariate')
    py_random_link = Hyperlink('https://docs.python.org/3.7/library/random.html#real-valued-distributions',
                               '(and other distributions)')
    py_random_normal_example = pl.Monospace('random.normalvariate(10, 1)')
    random_seed_example = pl.Monospace('random.seed(0)')
    next_slide = lp.Overlay([lp.NextWithIncrement()])
    n_iter = pl.Equation(str_eq='n_{iter}')
    df_mono = pl.Monospace('DataFrame')
    df_std = pl.Monospace('df.std()')
    df_mean = pl.Monospace('df.mean()')
    random_choices_mono = pl.Monospace('random.choices')
    random_choices_example = pl.Monospace("random.choices(['Recession', 'Normal', 'Expansion'], [0.3, 0.5, 0.2])")

    return [
        pl.Section(
            [
                lp.TwoColumnGraphicDimRevealFrame(
                    [
                        'So far everything in our models has been deterministic',
                        'Further, we have not explored any scenarios in our models, we have taken the base case as '
                        'the only case',
                        'Unfortunately, the real world is very random. Many possible scenarios could occur.'
                    ],
                    [
                        images_path('dice.jpg'),
                    ],
                    title='Why Model Probability'
                ),
                lp.DimRevealListFrame(
                    [
                        'There are a few ways we can gain a richer understanding of the modeled situation by '
                        'incorporating probability',
                        f'The simplest is {pl.Bold("scenario modeling")}, in which different situations are defined with probabilities, '
                        'and the result of the model is the expected value across the cases.',
                        ['Another is', pl.Bold('internal randomness'),
                         'where randomness is incorporated directly within '
                         'the model logic'],
                        ['Finally,', pl.Bold("Monte Carlo simulation"),
                         'treats the model as deterministic but externally varies the '
                         'inputs to get a distribution of outputs.']
                    ],
                    title='How to Bring Probability In'
                ),
            ],
            title='Motivation for Probability Modeling',
            short_title='Intro',
        ),
        pl.Section(
            [
                lp.Frame(
                    [
                        pl.UnorderedList([
                            lp.DimAndRevealListItems([
                                ['When something is measured numerically, it can be either a', pl.Bold('discrete'),
                                 'variable, or a', pl.Bold('continuous'), 'variable.'],

                            ])
                        ]),
                        lp.Block(
                            [
                                pl.Equation(str_eq=r'x \in \{x_1, x_2, ... x_n\}', inline=False),
                                pl.VSpace(-0.4),
                                pl.UnorderedList([
                                    [pl.Equation(str_eq=r'\{x_1, x_2, ... x_n\}:'), 'A specific set of values'],
                                ])
                            ],
                            title='Discrete Variables'
                        ),
                        lp.Block(
                            [
                                pl.Equation(str_eq=r'x \in \mathbb{R} \text{ or } [a, b]', inline=False),
                                pl.VSpace(-0.4),
                                pl.UnorderedList([
                                    [pl.Equation(str_eq='\mathbb{R}:'), 'All real numbers'],
                                    [pl.Equation(str_eq='[a, b]:'), 'Some interval between two values or infinity'],

                                ])
                            ],
                            title='Continuous Variables'
                        ),
                    ],
                    title='Math Review: Discrete and Continuous Variables'
                ),
                lp.Frame(
                    [
                        pl.TextSize(-3),
                        pl.UnorderedList([
                            lp.DimAndRevealListItems([
                                [pl.Bold('Expected value'), 'is the average outcome over repeated trials'],
                                "It is generally useful to get a single output from multiple possible cases",
                            ], dim_earlier_items=False)
                        ]),
                        lp.Block(
                            [
                                pl.Equation(str_eq=r'E[x] = \sum_{i=1}^{N} p_i x_i', inline=False),
                                pl.VSpace(-0.4),
                                pl.UnorderedList([
                                    [pl.Equation(str_eq=r'E[x]:'), 'Expected value for', pl.Equation(str_eq='x')],
                                    [pl.Equation(str_eq=r'x_i:'), 'A specific value for', pl.Equation(str_eq='x')],
                                    [pl.Equation(str_eq=r'p_i:'), 'The probability associated with value',
                                     pl.Equation(str_eq='x_i')],
                                    [pl.Equation(str_eq=r'N:'), 'The total number of possible values of',
                                     pl.Equation(str_eq='x')],
                                ])
                            ],
                            title='Discrete Variables'
                        ),
                        lp.Block(
                            [
                                pl.Equation(str_eq=r'E[x] = \frac{1}{N} \sum_{i=1}^{N} x_i', inline=False),
                                pl.VSpace(-0.4),
                                pl.UnorderedList([
                                    [pl.Equation(str_eq=r'N:'), 'The number of samples collected for',
                                     pl.Equation(str_eq='x')],
                                ])
                            ],
                            title='Continuous Variables'
                        ),
                    ],
                    title='Math Review: Expected Value'
                ),
                lp.GraphicFrame(
                    images_path('different-variance-plot.pdf'),
                    title='Math Review: Variance in One Picture'
                ),
                lp.Frame(
                    [
                        pl.TextSize(-2),
                        pl.UnorderedList([
                            lp.DimAndRevealListItems([
                                [pl.Bold('Variance'), 'and', pl.Bold('standard deviation'),
                                 'are measures of the dispersion '
                                 'of values of a random variable.'],
                                'Variance is the real quantity of interest, but standard deviation is easier to understand '
                                'because it has the same units as the variable, while variance has units squared'
                            ], dim_earlier_items=False),
                        ]),
                        lp.Block(
                            [
                                EquationWithVariableDefinitions(
                                    r'Var[x] = \sigma^2 = \frac{1}{N - 1} \sum_{i=1}^{N} (x_i - \mu)^2',
                                    [
                                        [pl.Equation(str_eq=r'N:'), 'Number of samples of', pl.Equation(str_eq=r'x')],
                                        [pl.Equation(str_eq=r'\mu:'), 'Sample mean'],
                                    ]
                                ),
                            ],
                            title='Variance of a Continuous Variable'
                        ),
                        lp.Block(
                            [
                                EquationWithVariableDefinitions(
                                    r'\sigma = \sqrt{Var[x]}',
                                    [
                                        [pl.Equation(str_eq=r'\sigma:'), 'Standard deviation'],
                                    ],
                                    space_adjustment=-0.5
                                ),
                            ],
                            title='Standard Deviation'
                        ),
                    ],
                    title='Math Review: Variance and Standard Deviation'
                ),
                lp.TwoColumnGraphicDimRevealFrame(
                    [
                        ['A', pl.Bold('probability distribution'),
                         'represents the probabilities of different values of '
                         'a variable'],
                        'For discrete variables, this is simply a mapping of possible values to probabilities, e.g. for a coin '
                        'toss, heads = 50% and tails = 50%',
                        'For continuous variables, a continuous distribution is needed, such as the normal distribution',
                    ],
                    graphics=[
                        images_path('normal-distribution.png'),
                    ],
                    title='Math Review: Probability Distributions'
                ),
                lp.TwoColumnGraphicDimRevealFrame(
                    [
                        pl.TextSize(-2),
                        ["You've probably heard of the", pl.Bold('normal distribution'),
                         'as it is very commonly used because it occurs a lot in nature'],
                        ['It is so common because of the', pl.Bold('central limit theorem'), 'which says that '
                                                                                             'averages of variables will follow a normal distribution, regardless of the distribution of the '
                                                                                             'variable itself'],
                        'This has many applications. For example, we can view the investment rate as an average across '
                        'individual investment returns, and so it will be normally distributed.',
                    ],
                    graphics=[
                        images_path('normal-distribution-percentages.png'),
                    ],
                    title='Math Review: Normal Distribution'
                ),
                lp.Frame(
                    [
                        pl.TextSize(-3),
                        pl.UnorderedList([
                            lp.DimAndRevealListItems([
                                'We want to extend our retirement model to say that the investment return is not constant.',
                                'We can treat the interest rate as either a discrete (specific values) or a continuous '
                                '(range of values, more realistic) variable'
                            ], dim_earlier_items=False),

                        ]),
                        lp.Block(
                            [
                                pl.Center(
                                    [
                                        lt.Tabular(
                                            [
                                                lt.ValuesTable.from_list_of_lists([
                                                    ['Interest Rate', 'Probability']
                                                ]),
                                                lt.MidRule(),
                                                lt.ValuesTable.from_list_of_lists([
                                                    ['2%', '30%'],
                                                    ['5%', '50%'],
                                                    ['7%', '20%'],
                                                ]),
                                            ],
                                            align='cc'
                                        )
                                    ]
                                )
                            ],
                            title='As a Discrete Variable'
                        ),
                        lp.Block(
                            [
                                pl.Equation(str_eq=r'r_i \sim N(\mu, \sigma^2)', inline=False),
                                pl.VSpace(-0.5),
                                pl.UnorderedList([
                                    [pl.Equation(str_eq=r'N:'), 'Normal distribution'],
                                    [pl.Equation(str_eq=r'\mu:'), 'Interest rate mean'],
                                    [pl.Equation(str_eq=r'\sigma:'), 'Interest rate standard deviation'],
                                ])
                            ],
                            title='As a Continuous Variable'
                        ),
                    ],
                    title='A Non-Constant Interest Rate'
                ),
            ],
            title='Mathematical Tools for Probability Modeling',
            short_title='Math Review'
        ),
        pl.Section(
            [
                lp.Frame(
                    [
                        pl.TextSize(-1),
                        lp.Block(
                            [
                                pl.Center(
                                    [
                                        lt.Tabular(
                                            [
                                                lt.ValuesTable.from_list_of_lists([
                                                    ['State of Economy', 'Interest Rate', 'Savings Rate', 'Probability']
                                                ]),
                                                lt.MidRule(),
                                                lt.ValuesTable.from_list_of_lists([
                                                    ['Recession', '2%', '35%', '30%'],
                                                    ['Normal', '5%', '30%', '50%'],
                                                    ['Expansion', '7%', '25%', '20%'],
                                                ]),
                                            ],
                                            align='l|ccc'
                                        )
                                    ]
                                )
                            ],
                            title='Interest Rate Scenarios'
                        ),
                        pl.UnorderedList([
                            lp.DimAndRevealListItems([
                                ['In scenario modeling, different cases for model parameters are chosen. Several '
                                 'parameters may be altered at once in a given case.'],
                                "Here we are making the different cases the state of the economy. When the economy is doing "
                                "poorly, the individual earns a lower return, but also saves more because they don't want to "
                                "overspend at a bad time",
                                "When the economy does well, the individual earns a higher return, but also spends more"
                            ])
                        ]),
                    ],
                    title='Scenario Modeling'
                ),
                lp.DimRevealListFrame(
                    [
                        ['We can implement scenario modeling', pl.Bold('internal'), 'or', pl.Bold('external'),
                         'to our model'],
                        ['With an internal implementation, the cases are built', pl.Underline('into the model logic'),
                         'itself, '
                         'and model logic also takes the expected value of the case outputs. The inputs of the model',
                         'are now the cases and probabilities.'],
                        ['With an external implementation, the', pl.Underline('model logic is left unchanged,'),
                         'instead the '
                         'model is run separately with each case, then the expected value is calculated across the outputs '
                         'from the multiple model runs.'],
                    ],
                    title='Implementing Scenario Modeling'
                ),
                lp.Frame(
                    [
                        pl.Center(
                            [
                                lt.Tabular(
                                    [
                                        lt.ValuesTable.from_list_of_lists([
                                            [pl.Bold('Internal'), pl.Bold('External')]
                                        ]),
                                        lt.MidRule(),
                                        lt.MidRule(),
                                        lt.ValuesTable.from_list_of_lists([
                                            ['Original model is now an old version',
                                             'Original model can still be used normally'],
                                        ]),
                                        # TODO [#14]: each row should come one per slide, but need to allow overlays in lt items
                                        lt.MidRule(),
                                        lt.ValuesTable.from_list_of_lists([
                                            ['Model runs exactly as before',
                                             'Getting full results of model requires running the model multiple times and '
                                             'aggregating output']
                                        ]),
                                        lt.MidRule(),
                                        lt.ValuesTable.from_list_of_lists([
                                            ['Model complexity has increased', 'Model complexity unchanged']
                                        ]),
                                        lt.MidRule(),
                                        lt.ValuesTable.from_list_of_lists([
                                            ['Complexity to run model is unchanged',
                                             'Complexity to run model has increased']
                                        ]),
                                    ],
                                    align='L{5cm}|R{5cm}'
                                )
                            ]
                        )
                    ],
                    title='Internal or External Scenario Analysis?'
                ),
                lp.DimRevealListFrame(
                    [
                        'For internal scenario analysis, set up a table of the cases and probabilities. Then calculate the '
                        'expected value of these cases for each model parameter. Then use the expected value as the new '
                        'model parameter.',
                        'For external scenario analysis, a data table is useful. Create the data table of outputs for each case '
                        'and another table of case probabilities, then combine them to produce the expected value of '
                        'the output.',
                        'If you are trying to change more than two inputs at once in external scenario '
                        'analysis, this becomes more '
                        'challenging but you can assign a number to each set of inputs and have the model look up the '
                        'inputs based on the case number, using the case number as the data table input.'

                    ],
                    title='Scenario Analysis in Excel'
                ),
                InClassExampleFrame(
                    [
                        'I will now go through adding external scenario analysis to the Dynamic Salary Retirement Model '
                        'in Excel',
                        'The completed exercise on the course site as "Dynamic Salary Retirement Model Sensitivity.xlsx"',
                    ],
                    title='Scenario Analysis in Excel',
                    block_title='Adding Scenario Analysis to the Dynamic Retirement Excel Model'
                ),
                scenario_excel_lab.presentation_frames(),
                lp.DimRevealListFrame(
                    [
                        ['For internal scenario analysis, set up a', df_mono,
                         'or dictionary of the cases and probabilities. Then calculate '
                         'the expected value of these cases for each model parameter. Then use the expected value as the new '
                         'model parameter.'],
                        'For external scenario analysis, just call your model function with each input case, collect the '
                        'results, and combine them to produce the expected value of the output.'
                    ],
                    title='Scenario Analysis in Python'
                ),
                InClassExampleFrame(
                    [
                        'I will now go through adding external scenario analysis to the Dynamic Salary Retirement Model '
                        'in Python',
                        'he completed exercise on the course site as "Dynamic Salary Retirement Model Scenario.ipynb"',
                    ],
                    title='Scenario Analysis in Python',
                    block_title='Adding Scenario Analysis to the Dynamic Retirement Python Model'
                ),
                scenario_python_lab.presentation_frames(),
            ],
            title='Scenario Modeling'
        ),
        pl.Section(
            [
                lp.DimRevealListFrame(
                    [
                        ["Using the technique of", pl.Bold('internal randomness,'),
                         'something random is added internally to the model'],
                        'Instead of taking a fixed input, random values for that variable are drawn',
                        'This technique can be used with both discrete and continuous variables'
                    ],
                    title='What is Internal Randomness?'
                ),
                lp.GraphicFrame(
                    internal_randomness_graphic(),
                    title='Internal Randomness in One Picture'
                ),
                lp.DimRevealListFrame(
                    [
                        'Internal randomness makes sense when the random behavior is integral to your model',
                        'If you are just trying to see how changing inputs affects outputs, or trying to get confidence intervals for outputs, '
                        'an external method such as sensitivity analysis or Monte Carlo simulation would make more sense.',
                        'For example, if we want to allow investment returns to vary in our retirement model, an external method fits well because '
                        'the core model itself is deterministic',
                        'If instead we were modeling a portfolio, we might use internal randomness to get the returns for each asset.'
                    ],
                    title='Should I Use Internal Randomness?'
                ),
                lp.DimRevealListFrame(
                    [
                        'Similarly to our discussion of internal vs. external sensitivity analysis, internal randomness keeps '
                        'operational complexity (how to run the model) low, but increases model complexity.',
                        'The main drawback of internal randomness is that the same set of inputs will give different outputs each time the model is run',
                        'While this is the desired behavior, it can make it difficult to determine whether everything is working.'
                    ],
                    title='Internal Randomness Advantages and Pitfalls'
                ),
                lp.TwoColumnGraphicDimRevealFrame(
                    [
                        'Instead of taking the input as fixed, draw it from a distribution',
                        'We need to define a distribution for each input we want to randomize. This will typically be a normal distribution, and then '
                        'we just need to give it a reasonable mean and standard deviation',
                        'Put the most reasonable or usual value as the mean. Then think about the probabilities of the normal distribution relative '
                        'to standard deviation to set it'
                    ],
                    graphics=[
                        images_path('normal-distribution-percentages.png'),
                    ],
                    title='Internal Randomness with Continuous Variables'
                ),
                lp.DimRevealListFrame(
                    [
                        ['The main functions for randomness in Excel are', rand_mono, 'and', rand_between_mono],
                        'The latter gives a random number between two numbers, while the former gives a random number '
                        'between 0 and 1. Both of these draw from a uniform distribution (every number equally likely)',
                        ['Meanwhile, the', norm_inv_mono,
                         'function gives the value for a certain normal distribution at a certain probability (it is not random)'],
                        'We can combine these two functions to draw random numbers from a normal distribution',
                        [excel_random_normal_example,
                         'would draw a number from a normal distribution with mean 10 and standard deviation 1'],
                    ],
                    title='Internal Randomness with Continuous Variables in Excel'
                ),
                InClassExampleFrame(
                    [
                        'I will now go through generating random continuous variables '
                        'in Excel',
                        'The completed exercise on the course site is called "Generating Random Numbers.xlsx"',
                        'We will focus only on the "Continuous" sheet for now',
                    ],
                    title='Example for Continuous Random Variables in Excel',
                    block_title='Generating Random Numbers from Normal Distributions in Excel'
                ),
                randomness_excel_lab.presentation_frames(),
                lp.DimRevealListFrame(
                    [
                        ['In Python, we have the built-in', random_module_mono, 'module'],
                        ['It has functions analagous to those in Excel:', py_rand_mono, 'works like', rand_mono,
                         'and', py_rand_uniform_mono, 'works like', rand_between_mono],
                        ['Drawing numbers from a normal distribution', py_random_link, 'is easier: just one function',
                         py_rand_norm_mono],
                        [py_random_normal_example,
                         'would draw a number from a normal distribution with mean 10 and standard deviation 1']
                    ],
                    title='Internal Randomness with Continuous Variables in Python'
                ),
                InClassExampleFrame(
                    [
                        'I will now go through generating random continuous variables '
                        'in Python',
                        'The completed exercise on the course site is called "Generating Random Numbers.ipynb"',
                        'We will focus only on the "Continuous" section for now',
                    ],
                    title='Example for Continuous Random Variables in Python',
                    block_title='Generating Random Numbers from Normal Distributions in Python'
                ),
                randomness_python_lab.presentation_frames(),
                lp.DimRevealListFrame(
                    [
                        'We can also build randomness into the model for discrete variables',
                        "With discrete variables, our distribution is just a table of probabilities for the different values",
                        'To pick a random value for a discrete variable, first add another column to your table which has the '
                        'cumulative sum of the prior probabilties, and then another column which is that column plus the '
                        'current probability',
                        'Then generate a random number between 0 and 1 from a uniform distribution',
                        'If the generated number is between the probability and the cumulative sum of prior probabilities, choose that case'
                    ],
                    title='Internal Randomness with Discrete Variables'
                ),
                lp.Frame(
                    [
                        pl.TextSize(-1),
                        lp.Block(
                            [
                                pl.Center(
                                    [
                                        lt.Tabular(
                                            [
                                                lt.ValuesTable.from_list_of_lists([
                                                    ['State of Economy', 'Interest Rate', 'Probability', 'Begin Range',
                                                     'End Range']
                                                ]),
                                                lt.MidRule(),
                                                lt.ValuesTable.from_list_of_lists([
                                                    ['Recession', '2%', '30%', '0%', '30%'],
                                                    ['Normal', '5%', '50%', '30%', '80%'],
                                                    ['Expansion', '7%', '20%', '80%', '100%'],
                                                ]),
                                            ],
                                            align='L{2cm}|cccc'
                                        )
                                    ]
                                )
                            ],
                            title='Interest Rate Scenarios'
                        ),
                        pl.UnorderedList([
                            pl.TextSize(-2),
                            lp.DimAndRevealListItems([
                                'The Begin Range column is calculated as the cumulative sum of prior probabilities',
                                'The End Range column is calculated as Begin Range + Probability',
                                "Generate a random number between 0 and 1. If it is between the begin and end range, "
                                "that is the selected value",
                                "If it's 0.15, it's a recession. If it's 0.45, it's a normal period. If it's 0.94, it's "
                                "an expansion period."
                            ], vertical_fill=True)
                        ]),
                    ],
                    title='An Example of Internal Randomness with Discrete Variables'
                ),
                lp.DimRevealListFrame(
                    [
                        'The steps in the preceeding slides need to be carried out manually in Excel',
                        ['In Python, there is a built-in function which is doing all of this in the background,',
                         random_choices_mono],
                        ['Simply do', random_choices_example, 'to yield the exact same result for the prior example']
                    ],
                    title='Random Discrete Variables in Python'
                ),
                InClassExampleFrame(
                    [
                        'I will now go through generating random discrete variables '
                        'in both Excel and Python',
                        'We will be continuing with the same Excel workbook and Jupyter notebook from before, '
                        '"Generating Random Numbers.xlsx" and "Generating Random Numbers.ipynb"',
                        'We will focus only on the "Discrete" sheet/section now',
                    ],
                    title='Example for Discrete Random Variables in Excel and Python',
                    block_title='Generating Random Numbers from Discrete Distributions in Excel and Python'
                ),
                random_stock_lab.presentation_frames(),
                InClassExampleFrame(
                    [
                        'I will now add internal randomness with discrete variables to '
                        'both the Excel and Python Dynamic Salary Retirement models to simulate economic conditions '
                        'changing year by year',
                        'The completed models on the course site are called '
                        '"Dynamic Salary Retirement Model Internal Randomness.xlsx" and '
                        '"Dynamic Salary Retirement Model Internal Randomness.ipynb"',
                    ],
                    title='Adding Internal Randomness to Excel and Python Models',
                    block_title='Extending the Dynamic Salary Retirement Model with Internal Randomness'
                ),
                full_model_internal_randomness_lab.presentation_frames(),
            ],
            title='Internal Randomness'
        ),
        pl.PresentationAppendix(appendix_frames),
    ]

DOCUMENT_CLASS_KWARGS = dict(
    nav_header=True,
    toc_sections=True
)
OUTPUT_NAME = TITLE

