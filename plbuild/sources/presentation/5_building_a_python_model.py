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
from pltemplates.frames.tvm.salary_eq import salary_block_content

TITLE = 'The Depth of a Financial Model, Continued'
SHORT_TITLE = 'TVM Deep Dive Python'
SUBTITLE = 'Extending a Simple Retirement Model in Python'
ORDER = 5


AUTHORS = ['Nick DeRobertis']
SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [['University of Florida', 'Department of Finance, Insurance, and Real Estate']]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = plbuild.paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = plbuild.paths.HANDOUTS_BUILD_PATH


def get_content():
    dark_green_def = pl.RGB(15, 82, 13, color_name='darkgreen')

    model_block_options = [
        'fill=darkgreen!60'
    ]

    model_sub_block_options = [
        'fill=darkgreen'
    ]

    text_options = [
        'text=white'
    ]

    model_node = lg.Rectangle(
        5, 8, offset=(1.25, 4), contents=pl.Bold('Model'), content_position='bottom', content_offset=0.2,
        shape_options=model_block_options, text_options=text_options
    )
    salary_node = lg.Rectangle(
        4, 1.75, offset=(1.25, 6.75), contents='Salary', shape_options=model_sub_block_options,
        text_options=text_options
    )
    wealth_node = lg.Rectangle(
        4, 1.75, offset=(1.25, 4.25), contents='Wealths', shape_options=model_sub_block_options,
        text_options=text_options
    )
    retirement_node = lg.Rectangle(
        4, 1.75, offset=(1.25, 1.75), contents='Retirement', shape_options=model_sub_block_options,
        text_options=text_options
    )

    next_until_end_ov = lp.Overlay([lp.UntilEnd(lp.NextWithIncrement())])


    return [
        lp.GraphicFrame(
            [
                lg.TikZPicture([
                    model_node,
                    salary_node,
                    wealth_node,
                    retirement_node,
                    lg.Arrow(salary_node, wealth_node),
                    lg.Arrow(wealth_node, retirement_node)
                ])
            ],
            title='The Structure of the Retirement Model',
            pre_env_contents=dark_green_def
        ),
        lp.Frame(
            [
                lp.Block(
                    salary_block_content,
                    title='Salary with Promotions and Cost of Living Raises'
                )
            ],
            title='Revisiting the Model Salary Equation'
        ),
        lp.Frame(
            [
                pl.UnorderedList([
                    'For wealths, we need to add the investment return and then the savings in each year',
                ], overlay=next_until_end_ov),
                pl.VFill(),
                lp.Block(
                    [
                        lp.adjust_to_full_size(pl.Equation(str_eq=r'W_t = W_{t-1}  (1 + r_i) + S_t  v')),
                        pl.UnorderedList([
                            f'{pl.Equation(str_eq="S_t")}:  Salary at year {pl.Equation(str_eq="t")}',
                            f'{pl.Equation(str_eq="W_t")}:  Wealth at year {pl.Equation(str_eq="t")}',
                            f'{pl.Equation(str_eq="r_i")}:  Investment return',
                            f'{pl.Equation(str_eq="t")}:  Number of years',
                            f'{pl.Equation(str_eq="v")}:  Savings rate',
                        ])
                    ],
                    title='Calculating Wealth',
                    overlay=next_until_end_ov,
                )
            ],
            title='Building the Wealth Model'
        ),
        lp.Frame(
            [
                pl.UnorderedList([
                    "Now we've seem how to create model functionality, and make it organized and "
                    "repeatable with functions"
                ]),
                pl.VFill(),
                LabBlock(
                    pl.UnorderedList([
                        'To wrap up the model, we should have a function which takes all the model inputs, '
                        'and returns the model output.',
                        'Create a function which takes starting salary, promotions every number of years, '
                        'cost of living raise, promotion raise, investment return, savings rate, and desired cash '
                        'as inputs',
                        'The function should return the number of years until retirement'
                    ]),
                    title='Organizing a Model in Functions'
                )
            ],
            title='One Organizational Pattern'
        )
    ]


