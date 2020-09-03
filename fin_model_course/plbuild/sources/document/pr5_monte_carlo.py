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

TITLE = 'Monte Carlo Simulation Problems'
ORDER = 'PR5'


def get_content():
    return [
        pl.Section(
            [
                pl.SubSection(
                    [
                        'You are a financial analyst for an aircraft manufacturer. Your company is trying to decide '
                        'how large its next line of planes should be. Developing a line of planes takes a one-time '
                        'research cost, then each plane has a cost to manufacture afterwards. The larger the plane, '
                        'the higher the research and manufacture costs, but also the more revenue per plane. The '
                        'larger planes are more risky because if the economy goes poorly, not many airlines will want '
                        'to invest in such a large plane, but if the economy goes well, airlines will be rushing to the '
                        'larger planes to fit rising demand.',
                        '',
                        """
                        The research cost will be paid at $t=0$. For simplicity, assume that all planes are manufactured 
                        at $t=1$ and sold at $t=2$. The interest rate is given in the below table.
                        
                        Find the expected NPV and standard deviation of NPV for each plane. Which plane has the lowest
                        chance of a negative NPV? Which has the highest chance of a positive NPV? Visualize the range
                        of possible NPVs for each plane, as well as the probability of acheiving different NPV levels 
                        (probability table). For the mid-size plane, which has a larger impact on the NPV, an 
                        additional plane sold or a decrease in the interest rate by 1%? In your opinion, which
                        plane should the manufacturer create?
                        """
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
                                        'Plane', 'Research Cost', 'Manufacture Cost', 'Sale Price', 'Expected Unit Sales', 'Stdev Unit Sales'
                                    ]]),
                                    lt.MidRule(),
                                    lt.ValuesTable.from_list_of_lists(
                                        [
                                            ['Super Size', r'\$100,000,000', r'\$10,000,000', r'\$11,500,000', '200', '120'],
                                            ['Large', r'\$50,000,000', r'\$5,000,000', r'\$5,600,000', '400', '50'],
                                            ['Mid-size', r'\$25,000,000', r'\$3,000,000', r'\$3,350,000', '500', '20'],
                                        ],
                                    ),
                                    lt.BottomRule(),
                                ],
                                align='l|ccccc'
                            )
                        )
                    ],
                    title='Possible Planes'
                ),
                pl.SubSection(
                    [
                        pl.Center(
                            lt.Tabular(
                                [
                                    lt.TopRule(),
                                    lt.ValuesTable.from_list_of_lists([[
                                        'Input', 'Default Value', 'Default Stdev'
                                    ]]),
                                    lt.MidRule(),
                                    lt.ValuesTable.from_list_of_lists(
                                        [
                                            ['Interest Rate', '7%', '4%'],
                                        ],
                                    ),
                                    lt.BottomRule(),
                                ],
                                align='l|cc'
                            )
                        )
                    ],
                    title='Other Inputs'
                )
            ],
            title='Capital Budgeting Probabilities with Monte Carlo Simulation'
        )
    ]

DOCUMENT_CLASS_KWARGS = dict(
    remove_section_numbering=True,
)
OUTPUT_NAME = TITLE

