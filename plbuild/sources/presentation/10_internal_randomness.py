import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

import plbuild
from plbuild.paths import images_path
from pltemplates.frames.model_flowchart import (
    ModelFlowchartFrame,
    real_world_style,
    model_style,
    in_out_style
)
from pltemplates.labblock import LabBlock
from pltemplates.eq_with_variable_defs import EquationWithVariableDefinitions
from pltemplates.hyperlink import Hyperlink
from pltemplates.graphics.internal_randomness import internal_randomness_graphic


AUTHORS = ['Nick DeRobertis']
SHORT_TITLE = 'Internal Randomness'
SUBTITLE = 'An Approach to Probability Modeling'

SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [
    ['University of Florida', 'Department of Finance, Insurance, and Real Estate'],
]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = plbuild.paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = plbuild.paths.HANDOUTS_BUILD_PATH
TITLE = 'Building Randomness Into Models'
ORDER = 10


def get_content():
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
        lp.Frame(
            [
                LabBlock(
                    [
                        ['Complete the following excercise in Excel for', pl.Equation(str_eq='n_{iter} = 10'), 'and',
                         pl.Equation(str_eq='n_{iter} = 1000')],
                        pl.UnorderedList([
                            ['Generate', n_iter, 'values between 0 and 1 with a uniform distribution'],
                            ['Generate', n_iter,
                             'values from a normal distribution with a 0.5 mean and 10 standard deviation'],
                            'Visualize each of the two outputs with a histogram',
                            'Calculate the mean and standard deviation of each of the two sets of generated numbers',
                            'Re-calculate it a few times, take note of how much the mean and standard deviation change'
                        ])
                    ],
                    title='Getting Started with Randomness in Excel'
                )
            ],
            title='Generating and Visualizing Random Numbers in Excel'
        ),
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
        lp.Frame(
            [
                pl.UnorderedList([
                    lp.DimAndRevealListItems([
                        'Unlike in Excel, it is easy to deal with the problem of the same input giving different outputs while you develop the model',
                        ['A', pl.Bold('random seed'), 'is a way to get the same set of random numbers every time'],
                        'If the seed is set before the model is run each time, the same input will always give the same output, even though parts of the '
                        'model are random.',
                        ['In Python, just run', random_seed_example,
                         'before running your model, and it will give the same results every time.'],
                    ], vertical_fill=True, dim_last_item=True)
                ]),
                pl.VFill(),
                lp.AlertBlock(
                    [
                        "Note that random seeds are typically just for developing the model, you'll want to remove this in the finished product."
                    ],
                    overlay=next_slide
                )

            ],
            title='Mitigating the Downsides of Internal Randomness in Python'
        ),
        lp.Frame(
            [
                pl.TextSize(-2),
                LabBlock(
                    [
                        ['Complete the following excercise in Python for', pl.Equation(str_eq='n_{iter} = 10'), 'and',
                         pl.Equation(str_eq='n_{iter} = 1000')],
                        pl.UnorderedList([
                            ['Generate', n_iter, 'values between 0 and 1 with a uniform distribution'],
                            ['Generate', n_iter,
                             'values from a normal distribution with a 0.5 mean and 10 standard deviation'],
                            'Visualize each of the two outputs with a histogram',
                            'Calculate the mean and standard deviation of each of the two sets of generated numbers',
                            'Re-calculate it a few times, take note of how much the mean and standard deviation change'
                        ])
                    ],
                    title='Getting Started with Randomness in Python'
                ),
                lp.Block(
                    [
                        pl.UnorderedList([
                            ['You will likely find it useful to store your data in a', df_mono,
                             'as that makes it easy to '
                             'calculate mean and standard deviation'],
                            ['Once you have your columns in the', df_mono, 'just do', df_mean, 'to get the mean and',
                             df_std, 'to get the standard deviations for each column.']
                        ])
                    ],
                    title='Taking Mean and Standard Deviation in Python'
                )
            ],
            title='Generating and Visualizing Random Numbers in Python'
        ),
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
        lp.Frame(
            [
                LabBlock(
                    [
                        pl.UnorderedList([
                            'A stock starts out priced at 100. Each period, it can either go up or down.',
                            'When it goes up, it will grow by 1%. When it goes down, it will decrease by 1%.',
                            'The likelihood of the stock going up is 60%, and down 40%.',
                            'Build a model which shows how the stock price changes throughout time. Visualize it up to 100 periods and '
                            'show the final price.'
                        ]),
                    ],
                    title='A Simple Model of a Stock Price Over Time'
                )
            ],
            title='Random Discrete Variables in Python and Excel'
        )


    ]

DOCUMENT_CLASS_KWARGS = {}
OUTPUT_NAME = TITLE

