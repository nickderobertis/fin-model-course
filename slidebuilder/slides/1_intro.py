from slidebuilder.paths import images_path
from pyexlatex import OrderedList, UnorderedList
from pyexlatex.models.hyperlinks import Hyperlink
from pyexlatex.models.format.monospace import Monospace
from pyexlatex.models.layouts.multicol import MultiCol
from pyexlatex.models.format.vfill import VFill

from pyexlatex.models.presentation.beamer.overlay.overlay import Overlay
from pyexlatex.models.presentation.beamer.overlay.next import NextWithIncrement
from pyexlatex.models.presentation.beamer.overlay.until_end import UntilEnd
from pyexlatex.models.presentation.beamer.frame.frame import Frame
from pyexlatex.models.presentation.beamer.block import Block, AlertBlock
from pyexlatex.models.presentation.beamer.templates.lists.dim_reveal_items import DimAndRevealListItems
from pyexlatex.models.presentation.beamer.templates.frames.two_col import (
    TwoColumnGraphicDimRevealFrame,
    TwoColumnGraphicFrame
)
from pyexlatex.models.presentation.beamer.templates.frames.dim_reveal import DimRevealListFrame
from pyexlatex.models.presentation.beamer.templates.frames.graphic import GraphicFrame

from pyexlatex.models.graphics.tikz.picture import TikZPicture
from pyexlatex.models.graphics.tikz.node.node import Node
from pyexlatex.models.graphics.flowcharts.linear import LinearFlowchart
from pyexlatex.models.presentation.beamer.templates.frames.graphic import adjust_to_full_size
from slidebuilder.templates.labblock import LabBlock
from slidebuilder.templates.frames.model_flowchart import (
    ModelFlowchartFrame,
    real_world_style,
    model_style,
    in_out_style
)


TITLE = 'Financial Modeling with Python and Excel'
SHORT_TITLE = 'Intro'
SUBTITLE = 'An Introduction'


next_slide_ov = Overlay([NextWithIncrement()])
next_until_end_ov = Overlay([UntilEnd(NextWithIncrement())])

input_model_output_fc = TikZPicture(
    LinearFlowchart(
        [
            'Inputs',
            'Model',
            'Outputs'
        ],
        node_options=in_out_style
    )
)

anaconda_link = Hyperlink('https://www.anaconda.com/distribution/#download-section')
mono_python = Monospace('python')
interpreter_mono = Monospace('>>>')


def get_frames():
    return [
        TwoColumnGraphicDimRevealFrame(
            [
                'This is a skills-based course focused on teaching financial modeling techniques in Python and Excel',
                'The focus is not a lot of specific models, but rather general model-building techniques',
                'The focus will be simple models, but extending them in powerful ways'
            ],
            graphic_filepaths=[
                images_path('python-logo.png'),
                images_path('excel-logo.png')
            ],
            title='What is this Class?'
        ),
        GraphicFrame(
            input_model_output_fc,
            title='What is a Model?'
        ),
        ModelFlowchartFrame(
            [
                [
                    'Wages, Savings',
                    'Investment',
                    Node('Cash in the bank, person retires',
                         options=real_world_style + ['text width=2.5cm'])
                ],
                [
                    Node('Cash Flows, Savings Rate, Interest Rates',
                         options=model_style + ['text width=3.5cm']),
                    'Model',
                    Node('FV of CF, time until retirement', options=model_style + ['text width=2.5cm'])
                ]
            ],
            title='A Retirement Problem'
        ),
        ModelFlowchartFrame(
            [
                [
                    Node('Microsoft creates software', options=real_world_style + ['text width=2cm']),
                    'Sells the software',
                    Node('Generates cash for investors, stock reaches a price',
                         options=real_world_style + ['text width=3cm'])
                ],
                [
                    Node('Revenue, COGS, SG&A, growth rates, costs of capital, etc.',
                         options=model_style + ['text width=3.5cm']),
                    'Model',
                    Node('Stock price, stock returns', options=model_style + ['text width=2.5cm'])

                ]
            ],
            title='Valuing a Company (DCF Model)'
        ),
        GraphicFrame(
            images_path('xkcd-python.png'),
            title='Why Python?'
        ),
        Frame(
            [
                UnorderedList(
                    [
                        DimAndRevealListItems(
                            [
                                "The easiest to learn mainstream programming language",
                                'Heavily used in the financial industry'
                            ],
                            dim_last_item=True,
                            vertical_fill=True
                        )
                    ]
                ),
                VFill(),
                Block(
                    MultiCol([
                        UnorderedList([
                            'Modeling',
                            'Data science',
                            'Algorithmic Trading',
                            'Scripting',
                        ]),
                        UnorderedList([
                            'Devices',
                            'Web Development',
                            'Web Scraping',
                            'Even these slides',
                        ])
                    ]),
                    title='Python is the Most Flexible of the Top Languages',
                    overlay=next_slide_ov
                )
            ],
            title='Python is a Good Choice for Finance'
        ),
        GraphicFrame(
            images_path('python-popularity.PNG'),
            title='Python is the Fastest Growing Programming Lanugage'
        ),
        DimRevealListFrame(
            [
                "Open source - completely free and open",
                "Focus on readability - almost pseudo-code",
                "Take as much as you need. Easy for beginners, many features for experts.",
                "Deep integrations with Excel - VBA replacement, run Python in Excel, run Excel from Python"
            ],
            title="More Python Advantages",
        ),
        GraphicFrame(
            images_path('python-terminal.png'),
            title='Why Not use Python?'
        ),
        DimRevealListFrame(
            [
                "No graphical interface (by default)",
                "Hard to get others working with it if they don't know Python",
                "Can take more work to get started on a project"
            ],
            title="Python Disadvantages"
        ),
        GraphicFrame(
            images_path('vba-terminal.png'),
            title='Why Not use VBA?'
        ),
        TwoColumnGraphicDimRevealFrame(
            [
                "Code is not as readable as Python",
                "Power is limited to working within Microsoft Office",
                "Python has a complete VBA API built into a package - Python can do VBA and more"
            ],
            [
                images_path('vba-logo.png')
            ],
            title="VBA is Old-School"
        ),
        DimRevealListFrame(
            [
                "Excel is everywhere. Most of the world's data is in Excel spreadsheets",
                '(Nearly) everyone knows how use it',
                "You can see what you're doing (without effort)",
                "Easy introspection into a particular value"
            ],
            title="We Can't Ditch Excel Yet"
        ),
        GraphicFrame(
            images_path('excel-hell.jpg'),
            title='Escaping Excel Hell'
        ),
        DimRevealListFrame(
            [
                "Code and view are mixed together, code is hidden",
                "Both cell formulas and VBA macros - What is going on?",
                "Easy to make mistakes (one cell different)",
                "Some tasks which are very simple in Python are very complex in Excel"
            ],
            title="The Pains of Excel"
        ),
        TwoColumnGraphicFrame(
            [
                LabBlock(
                    OrderedList(
                        [
                            f'Go to {anaconda_link} to download Python 3.7',
                            'Follow the steps in the installer',
                            'Open CMD (windows key, search cmd)',
                            f'Type {mono_python} and hit enter. You should see Python 3.7 and a {interpreter_mono} come up.'
                        ]
                    ),
                    title='Install Steps',
                ),
                AlertBlock(
                    'Make sure you have selected Python 3.7 and not 2.7'
                )
            ],
            [
                images_path('anaconda-logo.png')
            ],
            title="Let's Get Python Set Up on your System"
        )



    ]