import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll
from pyexlatex.models.sizes.textwidth import TextWidth

import plbuild
from plbuild.paths import images_path
from pltemplates.hyperlink import Hyperlink
from pltemplates.frames.model_flowchart import (
    ModelFlowchartFrame,
    real_world_style,
    model_style,
    in_out_style
)
from pltemplates.labblock import LabBlock

TITLE = 'The Depth of a Financial Model'
SHORT_TITLE = 'TVM Deep Dive Excel'
SUBTITLE = 'Extending a Simple Retirement Model in Excel'
ORDER = 3

AUTHOR = 'Nick DeRobertis'
SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [['University of Florida', 'Department of Finance, Insurance, and Real Estate']]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = plbuild.paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = plbuild.paths.HANDOUTS_BUILD_PATH


def get_content():
    next_slide = lp.Overlay([lp.NextWithIncrement()])

    model_block_options = [
        'fill=blue!50'
    ]

    model_sub_block_options = [
        'fill=blue!90'
    ]

    text_options = [
        'text=white'
    ]

    return [
        lp.DimRevealListFrame(
            [
                "In the last class, we built a simple retirement model",
                "Today we will see how any financial model can become complex very quickly",
                "We will continue building the model in both Excel and Python, later combining the two"
            ],
            title='From Simple to Complex'
        ),
        lp.GraphicFrame(
            [
                lg.TikZPicture([
                    lg.Rectangle(5, 8, offset=(1.25, 4), contents=pl.Bold('Model'), content_position='bottom',
                                 content_offset=0.2, shape_options=model_block_options, text_options=text_options),
                    lg.Rectangle(4, 1.75, offset=(1.25, 1.75), contents='Assumptions',
                                 shape_options=model_sub_block_options, text_options=text_options),
                    lg.Rectangle(4, 1.75, offset=(1.25, 4.25), contents='Logic', shape_options=model_sub_block_options,
                                 text_options=text_options),
                    lg.Rectangle(4, 1.75, offset=(1.25, 6.75), contents='Equations',
                                 shape_options=model_sub_block_options, text_options=text_options),
                ])
            ],
            title='The Conceptual Parts of a Model'
        ),
        lp.Frame(
            [
                pl.UnorderedList([
                    lp.DimAndRevealListItems(
                        ['We made a few assumptions last time in building a general retirement model'],
                        dim_last_item=False),
                    pl.VFill(),
                    lp.Block(
                        pl.OrderedList([
                            'The salary is constant over time',
                            'The savings rate is constant over time',
                            'Investment returns are constant over time',
                            'The amount needed in retirement is given by a fixed amount of desired cash',
                            'The amount needed in retirement does not depend on market conditions or life situations'
                        ]),
                        overlay=next_slide,
                        title='Assumptions'
                    )

                ])
            ],
            title='What Did we Assume?'
        ),
        lp.DimRevealListFrame(
            [
                "Assumptions can be relaxed to create a more realistic model",
                "Often we still need an assumption, but it can be a more realistic one",
                "We shall relax the constant salary assumption",
                [
                    pl.Bold('New assumption: '),
                    'The salary grows at a constant rate for cost of living raises, and every number of years the '
                    'salary grows at an additional rate for a promotion.'
                ]
            ],
            title='Relaxing the salary assumption'
        ),
        lp.Frame(
            [
                lp.Block(
                    [
                        lp.adjust_to_full_size(pl.Equation(str_eq=r'W_t = W_0 (1 + r_l)^t (1 + r_p)^p')),
                        pl.UnorderedList([
                            f'{pl.Equation(str_eq="W_t")}:  Wealth at year {pl.Equation(str_eq="t")}',
                            f'{pl.Equation(str_eq="W_0")}:  Starting wealth',
                            f'{pl.Equation(str_eq="r_l")}:  Return for cost of living',
                            f'{pl.Equation(str_eq="r_p")}:  Return for promotion',
                            f'{pl.Equation(str_eq="t")}:  Number of years',
                            f'{pl.Equation(str_eq="p")}:  Number of promotions',

                        ])
                    ],
                    title='The Equation from the New Assumption'
                )
            ],
            title='Relaxing the salary assumption'
        ),
        lp.TwoColumnGraphicDimRevealFrame(
            [
                "We are going to build our first complex Excel model",
                "It is important to start structuring your model so that it is navigatable",
                "Inputs in one area, outputs in one area, sub-models in individual tabs"
            ],
            graphic_filepaths=[
                images_path('excel-logo.png')
            ],
            title='An Organized Structure of an Advanced Excel Model'
        ),
        lp.DimRevealListFrame(
            [
                "We need to learn a few formulas and patterns in Excel to model the new assumption",
                pl.Graphic(images_path('excel-if.png'), width=f'0.5{TextWidth()}'),
                [pl.Monospace('=IF(5=5, "this", "that")'), '-> "this"'],
                [pl.Monospace('=IF(4=5, "this", "that")'), '-> "that"']
            ],
            title='Modeling Salary Growth in Excel - If Command'
        ),
        lp.DimRevealListFrame(
            [
                pl.Graphic(images_path('excel-mod.png'), width=f'0.3{TextWidth()}'),
                "Returns the remainder after a number is divided by a divisor",
                [pl.Monospace('=MOD(3, 4)'), '-> 3'],
                [pl.Monospace('=MOD(7, 2)'), '-> 1']
            ],
            title='Modeling Salary Growth in Excel - Modulo'
        ),
        lp.DimRevealListFrame(
            [
                pl.Graphic(images_path('excel-vlookup.png'), width=f'0.5{TextWidth()}'),
                "Use VLOOKUP when you need to find things in a table or by row",
                pl.Graphic(images_path('excel-vlookup-example-table.png'), width=f'0.2{TextWidth()}'),
                [pl.Monospace('=VLOOKUP("Celery", J3:K6, 2)'), '-> "Vegetable"'],
                'Lookup column must be first column, and must be sorted in ascending order.'
            ],
            title='Modeling Salary Growth in Excel - Table Lookup'
        ),
        lp.Frame(
            [
                pl.UnorderedList([
                    'We want to relax the assumption that the amount needed in retirement is given by a fixed amount of desired cash'
                ]),
                pl.VFill(),
                LabBlock(
                    pl.UnorderedList([
                        'Add new inputs to the model, "Annual Cash Spend During Retirement" and "Years in Retirement"',
                        'Calculate desired cash based on interest, cash spend, and years in retirement',
                        'Use the calculated desired cash in the model to determine years to retirement',
                        r'If annual spend is 40k for 25 years in retirement, \$563,757.78 should be the retirement cash'
                    ]),
                    title='Modeling Desired Cash'
                )
            ],
            title='Relaxing the Static Desired Cash in Excel'
        )
    ]


