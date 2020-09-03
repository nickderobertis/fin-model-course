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

TITLE = 'Internal Randomness Problems'
ORDER = 'PR3'


def get_content():
    return [
        pl.Section(
            [
                pl.SubSection(
                    [
                        'Create a model with two stocks, A and B. Both start at price 100. Generate stock prices for '
                        '100 periods. Do this by drawing returns from normal distributions defined with the inputs '
                        'below. Then apply the returns to the prior prices to get the price in each period. Create a '
                        "portfolio of the two stocks, by taking the weighted-average of the stock's returns, then applying "
                        "that return to a third Portfolio series starting at 100. Graph "
                        "the two stocks and porfolio performance over time. Calculate the mean and standard deviation "
                        "of the generated returns for the two stocks and the portfolio."
                    ],
                    title='Problem Statement'
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
                                            ['Stock A Weight', '60%'],
                                            ['Stock A Mean Return', '10%'],
                                            ['Stock A Return Standard Deviation', '30%'],
                                            ['Stock B Mean Return', '5%'],
                                            ['Stock B Return Standard Deviation', '10%'],
                                        ],
                                    ),
                                    lt.BottomRule(),
                                ],
                                align='l|c'
                            )
                        )
                    ],
                    title='Inputs'
                ),

            ],
            title='Stock Portfolio'
        )
    ]

DOCUMENT_CLASS_KWARGS = {}
OUTPUT_NAME = TITLE

