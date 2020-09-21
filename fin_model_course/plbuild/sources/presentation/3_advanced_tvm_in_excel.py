import random

import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll
from pyexlatex.models.sizes.textwidth import TextWidth

import plbuild
from build_tools.config import SITE_URL
from lectures.dynamic_excel.main import get_dynamic_salary_excel_lecture
from lectures.lab_exercises.notes import get_extend_dynamic_retirement_excel_lab_lecture
from plbuild.paths import images_path
from pltemplates.frames.in_class_example import InClassExampleFrame
from pltemplates.hyperlink import Hyperlink
from pltemplates.frames.model_flowchart import (
    ModelFlowchartFrame,
    real_world_style,
    model_style,
    in_out_style
)
from pltemplates.blocks import LabBlock
from pltemplates.frames.tvm.salary_eq import salary_block_content
from schedule.main import LECTURE_3_NAME

TITLE = LECTURE_3_NAME
SHORT_TITLE = 'TVM Deep Dive Excel'
SUBTITLE = 'Extending a Simple Retirement Model in Excel'
ORDER = 'S3'

AUTHORS = ['Nick DeRobertis']
SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [['University of Florida', 'Department of Finance, Insurance, and Real Estate']]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = plbuild.paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = plbuild.paths.HANDOUTS_BUILD_PATH


def get_content():
    random.seed(1000)
    next_slide = lp.Overlay([lp.NextWithIncrement()])
    site_link = Hyperlink(SITE_URL, 'the course site')

    lecture = get_dynamic_salary_excel_lecture()

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
        pl.Section(
            [
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
                                         content_offset=0.2, shape_options=model_block_options,
                                         text_options=text_options),
                            lg.Rectangle(4, 1.75, offset=(1.25, 1.75), contents='Assumptions',
                                         shape_options=model_sub_block_options, text_options=text_options),
                            lg.Rectangle(4, 1.75, offset=(1.25, 4.25), contents='Logic',
                                         shape_options=model_sub_block_options,
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
                        ]),
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
                    ],
                    title='What Did we Assume?'
                ),
            ],
            title='The Simple Model',
            short_title='Simple Model'
        ),
        pl.Section(
            [
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
                            salary_block_content,
                            title='The Equation from the New Assumption'
                        )
                    ],
                    title='Relaxing the salary assumption'
                ),
            ],
            title='Extending the Model by Relaxing Assumptions',
            short_title='Relax Assumptions'
        ),
        pl.Section(
            [
                lp.TwoColumnGraphicDimRevealFrame(
                    [
                        "We are going to build our first complex Excel model",
                        "It is important to start structuring your model so that it is navigatable",
                        "Inputs in one area, outputs in one area, sub-models in individual tabs"
                    ],
                    graphics=[
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
                InClassExampleFrame(
                    [
                        'I will now relax the assumption that salary is a fixed number in the Excel model.',
                        'As this will be quite different from the last model, I will start from scratch.',
                        [
                            'I have uploaded the finished product to', site_link,
                            'as Dynamic Salary Retirement Model'
                        ]
                    ],
                    title='Salary Growth in Excel',
                    block_title='Extending the Excel Retirement Model for Realistic Salaries'
                ),
                get_extend_dynamic_retirement_excel_lab_lecture().to_pyexlatex().presentation_frames(),
            ],
            title='Advanced Excel Modeling',
            short_title='Advanced Excel'
        ),
        pl.PresentationAppendix(
            [
                lecture.pyexlatex_resources_frame,
                get_extend_dynamic_retirement_excel_lab_lecture().to_pyexlatex().appendix_frames(),
            ]
        )
    ]


DOCUMENT_CLASS_KWARGS = dict(
    nav_header=True,
    toc_sections=True
)
OUTPUT_NAME = TITLE