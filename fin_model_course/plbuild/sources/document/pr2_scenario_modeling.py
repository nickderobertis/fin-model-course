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

TITLE = 'Scenario Modeling Problems'
ORDER = 'PR2'


def get_content():

    return [
        pl.Section(
            [
                pl.SubSection(
                    [
                        'You are an analyst trying to decide whether it is worth it to launch a new product line selling '
                        't-shirts. The success of the t-shirt business will depend on the state of the economy. '
                        'You can purchase a machine which costs \\$10,000,000 at $t=0$, then each year you will earn '
                        'the profit per unit (revenue minus variable cost), multiplied by the output. The machine will '
                        'last for 10 years. Should this project be undertaken? Will it be successful in all scenarios?',
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
                                        'State of Economy', 'Probability', 'Price', 'Output', 'Interest Rate'
                                    ]]),
                                    lt.MidRule(),
                                    lt.ValuesTable.from_list_of_lists(
                                        [
                                            ['Expansion', '20%', '15', '1000000', '7%'],
                                            ['Normal', '70%', '12', '500000', '5%'],
                                            ['Recession', '10%', '10', '200000', '3%'],
                                        ],
                                    ),
                                    lt.BottomRule(),
                                ],
                                align='l|cccc'
                            )
                        )
                    ],
                    title='Scenarios'
                ),

            ],
            title='Capital Budgeting'
        )
    ]

DOCUMENT_CLASS_KWARGS = {}
OUTPUT_NAME = TITLE

