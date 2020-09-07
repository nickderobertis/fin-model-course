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
from models.project_1 import PhoneManufacturingModel, ELASTICITY_CONSTANT_CASES
from pyexlatex.texgen.packages.default import default_packages

from schedule.main import PROJECT_1_NAME

AUTHORS = ['Nick DeRobertis']

DOCUMENT_CLASS = pl.Document
OUTPUT_LOCATION = plbuild.paths.DOCUMENTS_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = None

TITLE = PROJECT_1_NAME
ORDER = 'PJ1'


def get_content():
    align_c = lt.ColumnAlignment('c')
    align_l = lt.ColumnAlignment('l')
    align = lt.ColumnsAlignment([align_l, align_c])

    n_phones = 100000
    price_scrap = 50000
    price_phone = 500
    cogs_phone = 250
    price_machine_adv = 1000000
    n_life = 10
    n_machines = 5
    d_1 = 100000
    g_d = 0.2
    max_year = 20
    interest = 0.05

    pmm = PhoneManufacturingModel(
        n_phones, price_scrap, price_phone, n_life, n_machines, d_1, g_d, max_year, interest
    )

    scipy_mono = pl.Monospace('scipy')
    scipy_minimize_link = 'https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize_scalar.html#' \
                          'scipy-optimize-minimize-scalar'
    scipy_minimize_mono = pl.Monospace('scipy.optimize.minimize_scalar')

    possible_elasicity_str = ', '.join([f'($E = {ec[0]}$, $d_c = {ec[1]}$)' for ec in ELASTICITY_CONSTANT_CASES])
    possible_elasicity_str = ', '.join([f'($E = {ec[0]}$, $d_c = {ec[1]}$)' for ec in ELASTICITY_CONSTANT_CASES])
    possible_elasicity_str = '[' + possible_elasicity_str + ']'


    return [
        pl.Section(
            [
                pl.SubSection(
                    [
                        'You work for a new startup that is trying to manufacture phones. You are tasked with building '
                        'a model which will help determine how many machines to invest in and how much to spend on '
                        'marketing. Each machine produces $n_{output}$ phones per year. Each phone sells '
                        r'for \$$p_{phone}$ and costs \$$c_{phone}$ in variable costs to produce. '
                        'After $n_{life}$ years, the machine can no longer produce output, but may be scrapped for '
                        r'\$$p_{scrap}$. The machine will not be replaced, so you may end up with zero total output '
                        r'before your model time period ends. '
                        'Equity investment is limited, so in each year you can spend $c_{machine}$ to either buy a machine or buy '
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
                            'You may limit your model to 20 years and a maximum of 5 machines if it is helpful.',
                            'For simplicity, assume that $c_{machine}$ is paid in every year, '
                            'even after all machines have shut down.',
                            'Ensure that you can change the inputs and the outputs change as expected.',
                            'For simplicity, assume that fractional phones can be sold, you do not '
                            'need to round the quantity transacted.'
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
                                    '$c_{machine}$: Price per machine or advertising year',
                                    '$c_{phone}$: Variable cost per phone',
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
                                    'Cash flows in each year, up to 20 years',
                                    'PV of cash flows, years 1 - 20',

                                ])
                            ],
                            title='Outputs'
                        )
                    ],
                    title='The Model'
                ),
                pl.SubSection(
                    [
                        "It is unrealistic to assume that price and demand are unrelated. To extend the model, "
                        "we can introduce a relationship between price and demand, given by the following equation: ",
                        pl.Equation(str_eq=r'd_1 = d_c - Ep_{phone}', inline=False),
                        pl.UnorderedList([
                            f'{pl.Equation(str_eq="E")}: Price elasticity of demand',
                            f'{pl.Equation(str_eq="d_c")}: Demand constant'
                        ]),
                        [f"For elasticities and constants {possible_elasicity_str} "
                         f"({len(ELASTICITY_CONSTANT_CASES)} total cases), and taking the other "
                         "model inputs in the ", pl.NameRef('check-work'), ' section, determine the optimal price for each '
                         'elasticity, that is the price which maximizes the NPV.'],
                        pl.SubSubSection(
                            [
                                pl.UnorderedList([
                                    '$d_1$ is no longer an input, but an output.',
                                    'This bonus requires optimization, which we have not yet covered in class.',
                                    'In Excel, you can use Solver.',
                                    [f'In Python, the {scipy_mono} package provides optimization tools. You will '
                                     f'probably want to use:',],
                                    pl.UnorderedList([
                                        Hyperlink(scipy_minimize_link, scipy_minimize_mono),
                                        "You will need to write a function which accepts price and returns NPV, "
                                        "with other model inputs fixed.",
                                        pl.UnorderedList([
                                            [
                                                'Depending on how you set this up,',
                                                Hyperlink('https://www.learnpython.org/en/Partial_functions',
                                                          'functools.partial'),
                                                'may be helpful for this.'
                                            ]
                                        ]),
                                        "It will actually need to return negative NPV, as the optimizer only minimizes, "
                                        "but we want maximum NPV.",
                                        ['No answers to check your work are given for this bonus. The',
                                         pl.NameRef('check-work'), 'section only applies to without the bonus.']
                                    ])
                                ])
                            ],
                            title='Notes'
                        )
                    ],
                    title='Bonus Problem'
                ),
            ],
            title='Overview'
        ),
        pl.Section(
            [
                'You must start from "Project 1 Template.xlsx". Ensure that you reference all inputs from '
                'the Inputs/Outputs tab. Also ensure that all outputs are referenced back to the Inputs/Outputs tab. '
                'Do not change any locations of the inputs or outputs. '
                'The final submission is your Excel workbook.'
            ],
            title='Excel Exercise'
        ),
        pl.Section(
            [
                [
                    'You must start from "Project 1 Template.ipynb". '
                    'I should be able to run all the '
                    'cells and get the output of your model at the bottom. ',
                    ['You should not change the name of the', pl.Monospace('ModelInputs'), 'class or the',
                     pl.Monospace('model_data'), 'variable.'],
                    'You need to define', pl.Monospace('cash_flows'), 'as your output cash flows (numbers, '
                    'not formatted), and ', pl.Monospace('npv'), 'as your NPV (number, not formatted). When you '
                    'show your final outputs in the notebook, then they should be formatted.'
                ]
            ],
            title='Python Exercise'
        ),
        pl.Section(
            [
                Center(
                    lt.Tabular(
                        [

                            lt.MultiColumnLabel('Grading Breakdown', span=2),
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
                        align=align
                    )
                )
            ],
            title='Grading'
        ),
        pl.Section(
            [
                'If you pass the following inputs (to the basic model, not bonus model): ',
                pl.UnorderedList([
                    f'{pl.Equation(str_eq="n_{output}")}: {n_phones:,.0f}',
                    f'{pl.Equation(str_eq="p_{scrap}")}: \${price_scrap:,.0f}',
                    f'{pl.Equation(str_eq="p_{phone}")}: \${price_phone:,.0f}',
                    f'{pl.Equation(str_eq="c_{machine}")}: \${price_machine_adv:,.0f}',
                    f'{pl.Equation(str_eq="c_{phone}")}: \${cogs_phone:,.0f}',
                    f'{pl.Equation(str_eq="n_{life}")}: {n_life}',
                    f'{pl.Equation(str_eq="n_{machines}")}: {n_machines}',
                    f'{pl.Equation(str_eq="d_1")}: {d_1:,.0f}',
                    f'{pl.Equation(str_eq="g_d")}: {g_d:.0%}',
                    f'{pl.Equation(str_eq="r")}: {interest:.0%}',
                ]),
                'You should get the following result:',
                # TODO [#10]: replace project 1 result using notebook executor
                """
                Cash Flows:

Year 1: \$24,000,000

Year 2: \$24,000,000

Year 3: \$24,000,000

Year 4: \$24,000,000

Year 5: \$24,000,000

Year 6: \$29,000,000

Year 7: \$35,000,000

Year 8: \$42,200,000

Year 9: \$50,840,000

Year 10: \$61,208,000

Year 11: \$73,699,600

Year 12: \$74,050,000

Year 13: \$49,050,000

Year 14: \$24,050,000

Year 15: \$-950,000

Year 16: \$-1,000,000

Year 17: \$-1,000,000

Year 18: \$-1,000,000

Year 19: \$-1,000,000

Year 20: \$-1,000,000



NPV: \$369,276,542
                """
            ],
            title='Check your Work',
            label='check-work'
        )

    ]

DOCUMENT_CLASS_KWARGS = dict(
    remove_section_numbering=True,
    # packages=default_packages + [pl.Package('hyperref', modifier_str='colorlinks, linkcolor=blue')]
)
OUTPUT_NAME = TITLE