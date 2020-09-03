import os
import json

import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll
from jinja2 import FileSystemLoader

import plbuild
from gradetools.project_3.config import ANSWERS_OUTPUT_PATH
from plbuild.paths import images_path
from pltemplates.hyperlink import Hyperlink
from schedule.main import PROJECT_3_NAME

AUTHORS = ['Nick DeRobertis']

DOCUMENT_CLASS = pl.Document
OUTPUT_LOCATION = plbuild.paths.DOCUMENTS_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = None

TITLE = PROJECT_3_NAME
ORDER = 'PJ3'


def get_content():
    jinja_templates_path = os.path.sep.join(['pltemplates', 'projects', 'p3'])
    jinja_env = pl.JinjaEnvironment(loader=FileSystemLoader(jinja_templates_path))

    with open(ANSWERS_OUTPUT_PATH, 'r') as f:
        answers_json = json.load(f)
    answers_dict = answers_json[0]

    beta_std = answers_dict['beta_std']
    mkt_ret_std = answers_dict['mkt_ret_std']
    bond_price_std = answers_dict['bond_price_std']
    tax_rate_std = answers_dict['tax_rate_std']
    bond_years = answers_dict['bond_years']
    bond_coupon = answers_dict['bond_coupon']
    bond_price = answers_dict['bond_price']
    bond_par = answers_dict['bond_par']
    risk_free = answers_dict['risk_free']
    price = answers_dict['price']
    shares_outstanding = answers_dict['shares_outstanding']
    libor_rate = answers_dict['libor_rate']

    inputs_table = pl.Center(
        lt.Tabular(
            [

                pl.MultiColumnLabel('Baseline Inputs', span=2),
                lt.TopRule(),
                lt.ValuesTable.from_list_of_lists(
                    [
                        ['Variable', 'Baseline Value']
                    ]
                ),
                lt.TableLineSegment(0, 1),
                lt.ValuesTable.from_list_of_lists(
                    [
                        ['Market Bond Maturity (Years)', f'{bond_years:.0f}'],
                        ['Market Bond Coupon', f'{bond_coupon:.2%}'],
                        ['Market Bond Price', rf'\${bond_price:.2f}'],
                        ['Market Bond Par Value', rf'\${bond_par:.2f}'],
                        ['Risk Free Rate', f'{risk_free:.2%}'],
                        ['Stock Price', rf'\${price:.2f}'],
                        ['Shares Outstanding', f'{shares_outstanding:,.0f}'],
                        ['LIBOR Rate', f'{libor_rate:.2%}'],
                    ]
                ),
                lt.BottomRule()

            ],
            align='l|c'
        )
    )

    stdev_table = pl.Center(
        lt.Tabular(
            [

                pl.MultiColumnLabel('Standard Deviations', span=2),
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
                        ['Walmart Bond Market Price', rf'\${bond_price_std}'],
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
                        inputs_table
                    ],
                    title='Baseline Model Inputs',
                    label='baseline-inputs'
                ),
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
                                f'WACC: {answers_dict["wacc"]:.2%}',
                                rf'MV Debt: \${answers_dict["mv_debt"] / 1000000000:.1f} billion',
                                f'Cost of Equity: {answers_dict["coe"]:.2%}',
                                f'Pre-Tax Cost of Debt: {answers_dict["pretax_cost_of_debt"]:.2%}'
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

                                    pl.MultiColumnLabel('Grading Breakdown', span=2),
                                    lt.TopRule(),
                                    lt.ValuesTable.from_list_of_lists(
                                        [
                                            ['Category', 'Percentage']
                                        ]
                                    ),
                                    lt.TableLineSegment(0, 1),
                                    lt.ValuesTable.from_list_of_lists(
                                        [
                                            ['Model Accuracy', '60%'],
                                            ['Model Readability', '20%'],
                                            ['Model Formatting', '10%'],
                                            ['Following the Template', '10%'],
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

