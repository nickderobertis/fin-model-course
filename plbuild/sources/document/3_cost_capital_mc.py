import os

import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll
from jinja2 import FileSystemLoader

import plbuild
from plbuild.paths import images_path
from pltemplates.hyperlink import Hyperlink

AUTHORS = ['Nick DeRobertis']

DOCUMENT_CLASS = pl.Document
OUTPUT_LOCATION = plbuild.paths.DOCUMENTS_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = None

TITLE = 'Monte Carlo Cost of Capital'
ORDER = 3


def get_content():
    jinja_templates_path = os.path.sep.join(['pltemplates', 'projects', 'p3'])
    jinja_env = pl.JinjaEnvironment(loader=FileSystemLoader(jinja_templates_path))

    beta_std = 0.2
    mkt_ret_std = 0.03
    wmt_bond_price_std = 30
    tax_rate_std = 0.05

    stdev_table = pl.Center(
        lt.Tabular(
            [

                lt.MultiColumn('Standard Deviations', span=2),
                lt.TopRule(),
                lt.ValuesTable.from_list_of_lists(
                    [
                        ['Variable', 'Standard Deviation']
                    ]
                ),
                lt.TableLineSegment(0, 1),
                lt.ValuesTable.from_list_of_lists(
                    [
                        [r'$\beta$', beta_std],
                        ['Market Return', f'{mkt_ret_std:.0%}'],
                        ['Walmart Bond Market Price', rf'\${wmt_bond_price_std}'],
                        ['Tax Rate', f'{tax_rate_std:.0%}'],
                    ]
                ),
                lt.BottomRule()

            ],
            align='l|c'
        )
    )

    return [
        pl.Section(
            [
                Project3ProblemModel(template_path='prob_definition.j2', environment=jinja_env),
                Project3ProblemModel(template_path='notes.j2', environment=jinja_env),
                Project3ProblemModel(template_path='bonus.j2', environment=jinja_env),
                pl.SubSection(
                    [
                        stdev_table
                    ],
                    title='Monte Carlo Inputs',
                    label='mc-inputs'
                ),
            ],
            title='Overview'
        ),

        pl.Section(
            [
                Project3ProblemModel(template_path='submission.j2', environment=jinja_env),
                pl.SubSection(
                    [
                        'Selected solutions with the baseline inputs:',
                        pl.UnorderedList(
                            [
                                'WACC: 5.19%',
                                r'MV Debt: \$83 billion',
                                'Cost of Equity: 5.96%'
                            ]
                        )
                    ],
                    title='Solutions'
                ),
                pl.SubSection(
                    [
                        pl.Center(
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
                                            ['Model Formatting', '10%'],
                                            ['Bonus', '5%']
                                        ]
                                    ),
                                    lt.MidRule(),
                                    lt.ValuesTable.from_list_of_lists(
                                        [
                                            ['Total Possible', '105%']
                                        ]
                                    ),
                                    lt.BottomRule()

                                ],
                                align='l|c'
                            )
                        )
                    ],
                    title='Grading'
                ),
            ],
            title='Submission & Grading'
        )
    ]


class Project3ProblemModel(pl.Model):
    wmt_bond_years = 15
    wmt_bond_coupon = .0525
    wmt_bond_coupon_pct = f'{wmt_bond_coupon:.2%}'
    wmt_bond_price = 130.58
    risk_free = 0.005
    risk_free_pct = f'{risk_free:.2%}'
    wmt_price = 119.51
    wmt_shrout = 2850000000
    wmt_shrout_fmt = f'{wmt_shrout:,.0f}'
    libor_rate = 0.0196
    libor_rate_pct = f'{libor_rate:.2%}'

    bonus_resources_list = pl.UnorderedList([
        Hyperlink(
            'https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html',
            'Advanced Read Excel (look at skiprows)'
        ),
        Hyperlink(
            'https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html#selection',
            'Selecting Values of a DataFrame'
        ),
        Hyperlink(
            'https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html',
            'Dropping missing values'
        ),
        Hyperlink(
            'https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html',
            'Marking Existing Values as Missing'
        ),
        Hyperlink(
            'https://scotch.io/tutorials/an-introduction-to-regex-in-python',
            'Intro to Regular Expressions (not necessarily required, but I used them)'
        ),
        Hyperlink(
            'https://docs.python.org/3/library/re.html',
            'Regular Expression Reference'
        )
    ])


DOCUMENT_CLASS_KWARGS = dict(
    remove_section_numbering=True,
)
OUTPUT_NAME = TITLE

