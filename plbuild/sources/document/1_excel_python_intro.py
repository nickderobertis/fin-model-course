import pandas as pd
import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll
from pyexlatex.models.format.centering import Center

import plbuild
from plbuild.paths import images_path
from pltemplates.hyperlink import Hyperlink


AUTHORS = ['Nick DeRobertis']

DOCUMENT_CLASS = pl.Document
OUTPUT_LOCATION = plbuild.paths.DOCUMENTS_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = None

TITLE = 'Project 1 - Excel and Python TVM'
ORDER = None


def get_content():
    align_c = lt.ColumnAlignment('c')
    align_l = lt.ColumnAlignment('l')
    align = lt.ColumnsAlignment([align_l, align_c])
    return [
        pl.Section(
            [
                pl.SubSection(
                    [
                        'You work for new startup that is trying to manufacture phones. You are tasked with building '
                        'a model which will help determine how many machines to invest in and how much to spend on '
                        'marketing. Each machine produces $n_{output}$ chairs per year. Each phone sells '
                        r'for \$$p_{phone}$. '
                        'After $n_{life}$ years, the machine can no longer produce output, but may be scrapped for '
                        r'\$$p_{machine}$. '
                        'Equity investment is limited, so in each year you can either buy a machine or buy '
                        'advertisements. In the first year you must buy a machine. Any other machine purchases must '
                        'be made one after another (advertising can only begin after machine buying is done). '
                        'Demand for your phones starts at '
                        '$d_1$. Each time you advertise, demand increases by $g_d$%. The prevailing market interest '
                        'rate is $r$.'
                    ],
                    title='The Problem'
                ),
                pl.SubSection(
                    [
                        pl.UnorderedList([
                            'You may limit your model to 20 years and a maximum of 5 machines if it is helpful.'
                        ])
                    ],
                    title='Notes'
                ),
                pl.SubSection(
                    [
                        pl.SubSubSection(
                            [
                                pl.UnorderedList([
                                    '$n_{output}$: Number of phones per machine per year',
                                    '$n_{machines}$: Number of machines purchased',
                                    '$n_{life}$: Number of years for which the machine produces phones',
                                    '$p_{phone}$: Price per phone',
                                    '$p_{scrap}$: Scrap value of machine',
                                    '$d_1$: Quantity of phones demanded in the first year',
                                    '$g_d$: Percentage growth in demand for each advertisement',
                                    '$r$: Interest rate earned on investments'

                                ])
                            ],
                            title='Inputs'
                        ),
                        pl.SubSubSection(
                            [
                                pl.UnorderedList([
                                    'Revenue in each year, up to 20 years',
                                    'PV of revenues, years 1 - 20',

                                ])
                            ],
                            title='Outputs'
                        )
                    ],
                    title='The Model'
                )
            ],
            title='Overview'
        ),
        pl.Section(
            [
                'You must start from "Project 1 Template.xlsx" on Canvas. Ensure that you reference all inputs from '
                'the Inputs/Outputs tab. Also ensure that all outputs are referenced back to the Inputs/Outputs tab. '
                'The final submission is your Excel workbook.'
            ],
            title='Excel Exercise'
        ),
        pl.Section(
            [
                'You can submit your Jupyter notebook, but it should be cleaned up. I should be able to run all the '
                'cells and get the output of your model at the bottom, then change the inputs and run again and get '
                'the new output. You may also submit a Python script (plain text file with Python code).'
            ],
            title='Python Exercise'
        ),
        pl.Section(
            [
                Center(
                    lt.Tabular(
                        [

                            lt.MultiColumn('Grading Breakdown', span=2),
                            lt.TopRule(),
                            lt.ValuesTable.from_list_of_lists(
                                [
                                    ['Category', 'Percentage']
                                ]
                            ),
                            lt.TableLineSegment(0, 1),
                            lt.ValuesTable.from_list_of_lists(
                                [
                                    ['Model Accuracy', '70%'],
                                    ['Model Readability', '20%'],
                                    ['Model Formatting', '10%']
                                ]
                            ),
                            lt.BottomRule()

                        ],
                        align=align
                    )
                )
            ],
            title='Grading'
        ),

    ]

DOCUMENT_CLASS_KWARGS = {}
OUTPUT_NAME = TITLE