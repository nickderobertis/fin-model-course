import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

from pyexlatex.models.sizes.textwidth import TextWidth
from pyexlatex.models.format.breaks import OutputLineBreak

from slidebuilder.paths import images_path
from slidebuilder.templates.labblock import LabBlock

TITLE = 'The Depth of a Financial Model'
SHORT_TITLE = 'TVM Deep Dive'
SUBTITLE = 'Extending a Simple Retirement Model in both Excel and Python'

next_slide = lp.Overlay([lp.NextWithIncrement()])
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

def get_frames():
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
            images_path('model-assumptions-equations-logic.png'),
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
        ),
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
