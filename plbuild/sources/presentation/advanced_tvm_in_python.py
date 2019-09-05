import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll
from pyexlatex.models.format.breaks import OutputLineBreak

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

TITLE = 'The Depth of a Financial Model, Continued'
SHORT_TITLE = 'TVM Deep Dive Python'
SUBTITLE = 'Extending a Simple Retirement Model in Python'
ORDER = 4

AUTHORS = ['Nick DeRobertis']
SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [['University of Florida', 'Department of Finance, Insurance, and Real Estate']]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = plbuild.paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = plbuild.paths.HANDOUTS_BUILD_PATH


def get_content():
    function_example = pl.Python(
"""
def my_func(a, b, c=10):
    return a + b + c

>>> my_func(5, 6)
21
""")

    class_example = pl.Python(
"""
class MyClass:

    def __init__(self, a, b, c=10):
        self.a = a
        self.b = b
        self.c = c

    def sum_inputs(self):
        return self.a + self.b + self.c

>>> my_obj = MyClass(5, 6)
>>> type(my_obj)
__main__.MyClass
>>> my_obj.sum_inputs()
21
""")

    if_example = [pl.Python(
"""
>>> if 5 == 6:
>>>     print('not true')
>>> else:
>>>     print('else clause')
>>> 
>>> this = 'woo'
>>> that = 'woo'
>>> 
>>> if this == that:
>>>     print('yes, print me')
>>> if this == 5:
>>>     print('should not print')
"""
    ), pl.Monospace('else clause'), OutputLineBreak(), pl.Monospace('yes, print me')]

    build_list_example = pl.Python(
"""
>>> inputs = [1, 2, 3]
>>> outputs = []
>>> for inp in inputs:
>>>     outputs.append(
>>>         inp + 10
>>>     )
>>> outputs.insert(0, 'a')
>>> print(outputs)
['a', 11, 12, 13]
"""
    )

    enumerate_example = [pl.Python(
"""
>>> inputs = ['a', 'b', 'c']
>>> for i, inp in enumerate(inputs):
>>>     print(f'input number {i}: {inp}')
"""
    ),
        pl.Monospace('input number 0: a'),
        OutputLineBreak(),
        pl.Monospace('input number 1: b'),
        OutputLineBreak(),
        pl.Monospace('input number 2: c')
    ]

    list_indexing_example = pl.Python(
"""
>>> my_list = ['a', 'b', 'c', 'd']
>>> my_list[0]  # first item
'a'
>>> my_list[1]  # second item
'b'
>>> my_list[-1]  # last item
'd'
>>> my_list[:-1]  # up until last item
['a', 'b', 'c']
>>> my_list[1:]  # after the first item
['b', 'c', 'd']
>>> my_list[1:3]  # from the second to the third item
['b', 'c']
"""
    )
    return [
        lp.TwoColumnGraphicDimRevealFrame(
            [
                "Now we are going to build our first complex Python model",
                "Just as we did in Excel, we need to add structure to make the model navigatable",
                "Models should be organized in classes, logic should be organized in functions"
            ],
            graphic_filepaths=[
                images_path('python-logo.png')
            ],
            title='An Organized Structure of an Advanced Python Model'
        ),
        lp.DimRevealListFrame(
            [
                "In Python, we can group logic into functions",
                "Functions have a name, inputs, and outputs",
                "Functions are objects like everything else in Python",
                function_example,
            ],
            title='Functions - Grouping Reusable Logic'
        ),
        lp.DimRevealListFrame(
            [
                ["In Python, we can create our own custom types of objects using a ", pl.Monospace('class')],
                "This is often used to group functions together, and to represent something",
                "We will use classes to represent models, and write functions and methods for the actual model equations and logic",
            ],
            title='Classes - Representing Things and Grouping Functions'
        ),
        lp.Frame(
            [
                class_example,
            ],
            title='Classes - An Example'
        ),
        lp.Frame(
            [
                lp.Block(
                    if_example,
                    title='If Statements in Python'
                ),
            ],
            title='Python Conditionals - If Statement'
        ),
        lp.DimRevealListFrame(
            [
                'Use two equals signs to compare things (single to assign things)',
                'Else is equivalent to value if false behavior in Excel',
                'We can do a lot more than just set a single value, anything can be done in an if or else statement',
                [pl.Monospace('elif'), ' is a shorthand for else if, e.g. not the last condition, but this condition']
            ],
            title='Explaining the If-Else Statements'
        ),
        lp.Frame(
            [
                lp.Block(
                    build_list_example,
                    title='List Building'
                ),
                pl.UnorderedList([
                    lp.DimAndRevealListItems([
                        ['Use ', pl.Monospace('.append'), ' to add an item to the end of a list'],
                        ['Use ', pl.Monospace('.insert'), ' to add an item at a certain position'],
                    ])
                ])
            ],
            title='Python Patterns - Building a List'
        ),
        lp.Frame(
            [
                lp.Block(
                    enumerate_example,
                    title='Enumerate and String Formatting'
                ),
                pl.UnorderedList([
                    lp.DimAndRevealListItems([
                        ['Use ', pl.Monospace('enumerate'),
                         ' to get a counter for the loop number along with the input'],
                        ['Use ', pl.Monospace("f'\{my_input\} in a string'"), ' to place the string version of ',
                         pl.Monospace('my_input'), ' into the string " in a string"'],
                    ])
                ])
            ],
            title='More Python Iteration, and String Formatting'
        ),
        lp.Frame(
            [
                pl.UnorderedList([
                    'Index is base zero (0 means first item, 1 means second item)',
                ]),
                pl.VFill(),
                list_indexing_example,
            ],
            title='List Indexing and Slicing'
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
            title='Relaxing the Static Desired Cash in Python'
        )
    ]

