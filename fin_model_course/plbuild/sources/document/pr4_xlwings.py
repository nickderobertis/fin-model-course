import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

import plbuild
from plbuild.paths import images_path


AUTHORS = ['Nick DeRobertis']

DOCUMENT_CLASS = pl.Document
OUTPUT_LOCATION = plbuild.paths.DOCUMENTS_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = None

TITLE = 'xlwings Problems'
ORDER = 'PR4'


def get_content():
    return [
        pl.Section(
            [
            pl.SubSection(
                [
                    'Create a model of stock returns and correlations. The asset returns should be based on the '
                    'capital asset pricing model (CAPM), which states:',
                    pl.Equation(str_eq=r'r_s = r_f + \beta (r_m - r_f) + \epsilon', inline=False),
                    pl.UnorderedList(
                        [
                            '$r_e$: Return on stock',
                            '$r_f$: Return on risk free asset',
                            '$r_m$: Return on the market portfolio',
                            r'$\beta$: Covariance between the market portfolio and the stock',
                            r'$\epsilon$: Idiosyncratic return, (random, normally distributed with mean 0)'
                        ]
                    ),
                    'Your model should accept the number of assets, '
                    'the average idiosyncratic standard deviation across the assets, the standard deviation of the '
                    'idiosyncratic standard deviation across the assets, the market average return, the '
                    'market standard deviation, the risk-free rate, and the number of periods as the inputs. You should randomly draw '
                    "each asset's standard deviation of idiosyncratic returns from a normal distribution based on the "
                    "inputs. You should also randomly draw the stock's beta from a uniform distribution between 0 and 2. "
                    "Then draw the market returns from a normal distribution with its mean and standard deviation. Then "
                    "the return for each asset in each time period will be determined by drawing its idiosyncratic return "
                    "for that period from its normal distribution, then calculating the CAPM formula. After all the assets "
                    "returns are generated, calculate the correlation between all the assets. Your model should be updating "
                    "the number of assets and number of periods merely by changing the inputs."
                ],
                title='Problem Definition'
            ),
            pl.SubSection(
                [
                    pl.Center(
                        lt.Tabular(
                            [
                                lt.TopRule(),
                                lt.ValuesTable.from_list_of_lists([[
                                    'Input', 'Default Value'
                                ]]),
                                lt.MidRule(),
                                lt.ValuesTable.from_list_of_lists(
                                    [
                                        ['Number of Assets', '3'],
                                        ['Number of Periods', '20'],
                                        ['Average Idiosyncratic Standard Deviation', '20%'],
                                        ['Standard Deviation of Idiosyncratic Return Standard Deviation', '10%'],
                                        ['Market Average Return', '7%'],
                                        ['Market Standard Deviation', '15%'],
                                        ['Risk-Free Rate', '2%'],
                                    ],
                                ),
                                lt.BottomRule(),
                            ],
                            align='l|c'
                        )
                    )
                ],
                title='Model Inputs'
            ),
            ],
            title='Generating Asset Returns using CAPM'
        )
    ]

DOCUMENT_CLASS_KWARGS = dict(
    remove_section_numbering=True,
)
OUTPUT_NAME = TITLE

