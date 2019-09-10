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
from pltemplates.frames.tvm.retirement_model_structure import get_retirement_model_overview_frame


AUTHORS = ['Nick DeRobertis']
SHORT_TITLE = 'Model Classes'
SUBTITLE = 'A Better Structure for a Complex Python Model, And Introducing Project 1'

SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [
    ['University of Florida', 'Department of Finance, Insurance, and Real Estate'],
]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = plbuild.paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = plbuild.paths.HANDOUTS_BUILD_PATH
TITLE = 'Structuring Python Code'
ORDER = 6


def get_content():
    f_string = pl.Monospace("f''")
    f_mono = pl.Monospace('f')
    f_string_example = pl.Python(
"""
>>> my_num = 5 / 6
>>> print(my_num)
0.8333333333333334
>>> print(f'My number is {my_num:.2f}')
'My number is 0.83'
"""
    )
    numpy_mono = pl.Monospace('numpy')
    try_except_example = pl.Python(
"""
>>> my_list = ['a', 'b']
>>> try:
>>>     my_value = my_list[10]
>>> except IndexError:
>>>     print('caught the error')
caught the error
"""
    )
    list_100_5 = pl.Monospace('[100] * 5')
    next_slide = lp.Overlay([lp.NextWithIncrement()])
    annuity_example = pl.Python(
"""
>>> annuity = [100] * 5
>>> annuities = [
>>>     annuity,
>>>     [0, 0, 0] + annuity
>>> ]
>>> n_years = 10
>>> output = [0] * n_years
>>> for i in range(n_years):
>>>     for ann in annuities:
>>>         try:
>>>             output[i] += ann[i]
>>>         except IndexError:
>>>             pass
>>> print(output)   
[100, 100, 100, 200, 200, 100, 100, 100, 0, 0]
"""
    )
    return [
        lp.DimRevealListFrame(
            [
                'Last time we finished building the Python model, and organized it in functions',
                'I mentioned previously that organizing models in classes makes sense',
                "We were constantly passing the same arguments around before. Let's look at how classes simplify this.",
                "You'll also see how using classes gives us a single unified interface to the model",
            ],
            title='Tidying up the Python Model'
        ),
        get_retirement_model_overview_frame(),
        lp.Frame(
            [
                pl.UnorderedList([
                    lp.DimAndRevealListItems([
                        'You may have noticed that we can end up with a lot of decimals in Python output',
                        'Further, you may want to include your results as part of a larger output, such as a sentence.',
                        f'For these operations, we have {f_mono} strings: {f_string}'
                    ],
                        vertical_fill=True)
                ]),
                lp.Block(
                    f_string_example,
                    title='Example',
                    overlay=next_slide
                )
            ],
            title='Formatting Python Outputs'
        ),
        lp.Frame(
            [
                pl.UnorderedList([
                    'We want to relax the assumption that the amount needed in retirement is given by a fixed '
                    'amount of desired cash'
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
            title='Relaxing the Static Desired Cash in Python'
        ),
        lp.DimRevealListFrame(
            [
                'The first project is aimed at approaching a new time value of money and cash flow model',
                'It covers the same concepts as the retirement model, but in a capital budgeting setting',
                'We need to introduce some economic equations to handle this model. You should have covered these in microeconomics.'
            ],
            title='Introducing Project 1'
        ),
        lp.GraphicFrame(
            images_path('supply-demand-graph.png'),
            title='A Quick Review of Supply and Demand'
        ),
        lp.Frame(
            [
                lp.Block(
                    [
                        "There are a couple of basic economic equations we haven't talked about that "
                        "we'll need for this:",
                        pl.Equation(str_eq='R = PQ', inline=False),
                        pl.Equation(str_eq='Q = min(D, S)', inline=False),
                        pl.UnorderedList([
                            f'{pl.Equation(str_eq="R")}: Revenue',
                            f'{pl.Equation(str_eq="Q")}: Quantity Purchased',
                            f'{pl.Equation(str_eq="D")}: Quantity Demanded',
                            f'{pl.Equation(str_eq="S")}: Quantity Supplied',
                        ])
                    ],
                    title='New Required Equations'
                )
            ],
            title='Equations for Project 1'
        ),
        lp.Frame(
            [
                pl.UnorderedList([
                    lp.DimAndRevealListItems([
                        'We need to cover one more Python concept and one gotcha before you can complete the first project.',
                        "On the next slide I'll introduce error handling, and show an example of how it's useful"
                    ],
                        vertical_fill=True)
                ]),
                lp.AlertBlock(
                    [
                        pl.UnorderedList([
                            f'The NPV function in {numpy_mono} works slightly differently than the NPV function in Excel.',
                            f'Excel treats the first cash flow as period 1, while {numpy_mono} treats the first cash flow as period 0.',
                            'If taking NPV where the first cash flow is period 1, pass directly to Excel, and for Python, pass 0 as the first cash flow, then the rest.',
                            'If taking NPV where the first cash flow is period 0, pass from period 1 to end to Excel and add period 0 separately, pass directly to Python.'
                        ])
                    ],
                    title='NPV Gotcha',
                    overlay=next_slide
                )
            ],
            title='A Couple More Things on the Python Side'
        ),
        lp.Frame(
            [
                pl.UnorderedList([
                    lp.DimAndRevealListItems([
                        "You have certainly already seen errors coming from your Python code. When they have come up, the code doesn't run.",
                        'Sometimes you actually expect to get an error, and want to handle it in some way, rather than having your program fail.'
                    ],
                        vertical_fill=True)
                ]),
                lp.Block(
                    try_except_example,
                    title='Example',
                    overlay=next_slide
                )
            ],
            title='Python Error Handling'
        ),
        lp.DimRevealListFrame(
            [
                "Let's say you're receiving annuities. There is a single annuity which produces \$100 for 5 years. You receive this annuity in year 0 and in year 3.",
                f"You might define the annuity cash flows as a list of 100, 5 times ({list_100_5})",
                'Then you want to come up with your overall cash flows, going out to 15 years'
            ],
            title='An Example where Error Handling is Useful'
        ),
        lp.Frame(
            [
                lp.Block(
                    annuity_example,
                    title='Calculating the Sum of Unaligned Annuity Cash-Flows'
                )
            ],
            title='Applying Error Handling'
        ),
        lp.Frame(
            [
                LabBlock(
                    pl.UnorderedList([
                        'Download and open the Project 1 document from Canvas',
                        "It is up to you whether you want to attempt the Excel or Python model first",
                        "If you feel comfortable with the Excel model, you may want to start with Python so I "
                        "can give help on that today."
                    ]),
                    title='Project 1'
                )
            ],
            title='Some Time to Work on the First Project'
        )
    ]

DOCUMENT_CLASS_KWARGS = {}
OUTPUT_NAME = TITLE

