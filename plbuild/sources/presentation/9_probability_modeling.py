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
TITLE = 'Probabilistic Modeling'
ORDER = 9


def get_content():
    df_mono = pl.Monospace('DataFrame')
    next_slide = lp.Overlay([lp.NextWithIncrement()])
    with_previous = lp.Overlay([lp.NextWithoutIncrement()])

    return [
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
                ['Another is', pl.Bold('internal randomness'), 'where randomness is incorporated directly within '
                 'the model logic'],
                ['Finally,', pl.Bold("Monte Carlo simulation"), 'treats the model as deterministic but externally varies the '
                'inputs to get a distribution of outputs.']
            ],
            title='How to Bring Probability In'
        ),
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
                pl.TextSize(-2),
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
                        [pl.Bold('Variance'), 'and', pl.Bold('standard deviation'), 'are measures of the dispersion '
                         'of values of a random variable.'],
                        'Variance is the real quantity of interest, but standard deviation is easier to understand '
                        'because it has the same units as the variable, while variance has units squared'
                    ], dim_earlier_items=False),
                ]),
                lp.Block(
                    [
                        EquationWithVariableDefinitions(
                            r'Var[x] = \sigma^2 = \frac{1}{N - 1} \sum_{i=1}^{N} (x_i - \mu)',
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
                ['A', pl.Bold('probability distribution'), 'represents the probabilities of different values of '
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
                pl.TextSize(-1),
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
                pl.TextSize(-2),
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
        lp.Frame(
            [
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
                        "poorly, the individual earns a lower return, but also saves more because they don't want to"
                        "overspend at a bad time",
                        "When the economy does well, the individual earns a higher return, but also spends more"
                    ])
                ]),
            ],
            title='Scenario Modeling'
        ),
        lp.DimRevealListFrame(
            [
                ['We can implement scenario modeling', pl.Bold('internal'), 'or', pl.Bold('external'), 'to our model'],
                ['With an internal implementation, the cases are built', pl.Underline('into the model logic'), 'itself, '
                 'and model logic also takes the expected value of the case outputs.'],
                ['With an external implementation, the', pl.Underline('model logic is left unchanged,'), 'instead the '
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
                                # TODO: each row should come one per slide, but need to allow overlays in lt items
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
                                    ['Complexity to run model is unchanged', 'Complexity to run model has increased']
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
                'the output.'
            ],
            title='Scenario Analysis in Excel'
        ),
        lp.DimRevealListFrame(
            [
                ['For internal scenario analysis, set up a', df_mono, 'of the cases and probabilities. Then calculate '
                 'the expected value of these cases for each model parameter. Then use the expected value as the new '
                'model parameter.'],
                'For external scenario analysis, just call your model function with each input case, collect the '
                'results, and combine them to produce the expected value of the output.'
            ],
            title='Scenario Analysis in Python'
        ),
        lp.Frame(
            [
                LabBlock(
                    [
                        pl.Center(
                            [
                                lt.Tabular(
                                    [
                                        lt.ValuesTable.from_list_of_lists([
                                            ['State of Economy', 'Promotions Every # Years']
                                        ]),
                                        lt.MidRule(),
                                        lt.ValuesTable.from_list_of_lists([
                                            ['Recession', '10'],
                                            ['Normal', '5'],
                                            ['Expansion', '3'],
                                        ]),
                                    ],
                                    align='l|c'
                                )
                            ]
                        ),
                        pl.UnorderedList([
                            "We have just added internal and external scenarios for interest rate and savings rate "
                            "based on the state of the economy.",
                            'Now also add the number of promotions also changing with the state of the economy.',
                            'Make one version of your model which has internal scenarios for number of promotions '
                            'and one version of your model that has external scenarios for number of promotions.',
                            'Complete this exercise for both the Excel and Python models'
                        ])
                    ],
                    title='Adding Scenario Analysis to your Model'
                )
            ],
            title='Implementing Scenario Analysis Internally and Externally'
        )

    ]

DOCUMENT_CLASS_KWARGS = {}
OUTPUT_NAME = TITLE

