from pyexlatex import (
    OrderedList,
    UnorderedList,
    Hyperlink,
    Monospace,
    VFill,
    Python,
    Graphic,
)
from pyexlatex.layouts import MultiCol
from pyexlatex.presentation import (
    Overlay,
    NextWithIncrement,
    TwoColumnGraphicDimRevealFrame,
    TwoColumnGraphicFrame,
    BasicTwoColumnFrame,
    TwoColumnFrame,
    UntilEnd,
    Frame,
    Block,
    AlertBlock,
    DimAndRevealListItems,
    DimRevealListFrame,
    GraphicFrame,
)

from pyexlatex.graphics import (
    TikZPicture,
    Node,
    LinearFlowchart,
)

from slidebuilder.base import FinancialModelingPresentation
from slidebuilder.paths import images_path
from slidebuilder.builder import create_all_presentations
from slidebuilder.templates.labblock import LabBlock
from slidebuilder.templates.frames.model_flowchart import (
    ModelFlowchartFrame,
    real_world_style,
    model_style,
    in_out_style
)
from slidebuilder.templates.hyperlink import Hyperlink

TITLE = 'Getting Started with Python and Excel'
SHORT_TITLE = 'Getting Started'
SUBTITLE = 'Building a Basic Model in Both Excel and Python'

full_fix = Monospace('\$A\$2')
col_fix = Monospace('\$A2')
row_fix = Monospace('A\$2')
notebook = Monospace('jupyter notebook')
lab = Monospace('jupyter lab')
list_ = Monospace('list')
for_ = Monospace('for')
append = Monospace('append')
numpy = Monospace('numpy')
cmd = Monospace('cmd')
terminal = Monospace('terminal')
in_block = Monospace('In [ ]:')

example_python_iteration = Block(
    Python("""
inputs = [5, 10, 15]
for item in inputs:
    new_value = item + 2
    print(new_value)

7
12
17
    """),
    title='Python Iteration'
)


def get_frames():
    return [
        TwoColumnGraphicDimRevealFrame(
            [
                'The focus today is to get familiar working in both Excel and Python',
                'We will approach this by building a simple model with both tools',
                'In later lectures, we will move to combining the tools'
            ],
            graphic_filepaths=[
                images_path('equations-chalkboard.jpg')
            ],
            title='Approaching a Problem with Two Tools'
        ),
        DimRevealListFrame(
            [
                "Let's take what is perhaps the simplest finance problem, which everyone should understand",
                "While you may have approached such a problem with a calculator before, we will build models for it instead",
                "Martha is saving for retirement. She earns \$60,000 per year and is able to save 25% of that. If she invests "
                "her savings, earning 5% per year, and she needs \$1,500,000 to retire, how soon can she retire?"
            ],
            title='A Simple Retirement Problem'
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
            title='Breaking Down the Retirement Problem'
        ),
        TwoColumnGraphicDimRevealFrame(
            [
                "It is easy to use Excel as a calculator and just type the math in directly. But we want to build a model.",
                "Changing inputs should result in a change to outputs. The way to do this in Excel is cell references",
                rf"Fixed references become important when trying to drag formulas, e.g. {full_fix} (fully fixed), {col_fix} (fixed on "
                rf"column), or {row_fix} (fixed on row)."
            ],
            graphic_filepaths=[
                images_path('excel-logo.png')
            ],
            title='Solving the Problem in Excel'
        ),
        TwoColumnGraphicDimRevealFrame(
            [
                "Using Python in the terminal is kind of a pain. And so, tools were born.",
                "Jupyter is a graphical interface we can use for Python. It also supports over 40 other "
                "languages such as R, SAS, Julia, and Scala",
                f"You can use {notebook} or {lab}. The latter has a lot more features outside of the notebook"
            ],
            graphic_filepaths=[
                images_path('jupyter-notebook.png')
            ],
            title="How We'll Work in Python"
        ),
        Frame(
            [
                LabBlock(
                    [
                        OrderedList([
                            "Launch Anaconda Navigator",
                            "Find Jupyter Notebook on the main screen, and click launch",
                            "You should see a list of folders and files. Click New and then Python 3",
                            f"Now you should see a code cell with {in_block} next to it"
                        ])
                    ],
                    title='Launch Jupyter Notebook'
                ),
                AlertBlock(
                    f"If you don't have Anaconda Navigator, just open a terminal (search {cmd} on Windows, {terminal} on Mac). Then in the "
                    f"terminal, type {notebook} and enter. Then continue with the third step."
                )
            ],
            title="Let's Get Set up with Jupyter"

        ),
        DimRevealListFrame(
            [
                "In Excel, the basic unit is a cell. In Python, the basic unit is an object.",
                "In Excel, content in a cell is either a number (123) or a string (ABC)",
                "In Python, all objects have types. They might also be a number or a string, or something else.",
                f"Rather than using a cell reference like {full_fix}, we assign names to objects in Python",
                Python("""
                my_number = 6
                my_string = 'ABC'
                """)
            ],
            title='Some Python Basics'
        ),
        TwoColumnGraphicFrame(
            [
                UnorderedList([
                    DimAndRevealListItems(
                        [
                            "Basic operations in Python are straightforward",
                            Python('2 + 5 = 7'),
                            Python('6 - 2 = 4'),
                            Python('2 * 3 = 6'),
                            Python('5 / 2 = 2.5'),
                            f'A lot more is available using the {numpy} package',
                            Python("np.pv, np.nper,\nnp.fv, np.pmt"),
                            Hyperlink('https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.financial.html',
                                      f'All numpy financial functions')
                        ],
                        dim_earlier_items=False
                    )
                ])
            ],
            graphic_filepaths=[
                images_path('numpy-logo.png')
            ],
            graphics_on_right=False,
            title='Doing Some Math in Python'
        ),
        DimRevealListFrame(
            [
                "Now we've got basic models to determine how long it will take Martha to retire.",
                "We've got a few assumptions built into the model. One is that Martha will earn 5% on her investments",
                "Rates of return are volatile, so we want to see how long it would take her to retire if her return was different"
            ],
            title='Extending the Model - Multiple Interest Rates'
        ),
        DimRevealListFrame(
            [
                "In programming, for model building or otherwise, you often need to repeat the same process for multiple different things",
                "In Excel, you would do this by dragging formulas.",
                f"In Python, as in most other programming languages, we would use a {for_} loop",
                "This says, do something, for each value I pass into the loop"
            ],
            title='Programming Fundamentals - Iteration'
        ),
        BasicTwoColumnFrame(
            [
                example_python_iteration
            ],
            [
                Block(
                    Graphic(
                        images_path('excel-iteration.png')
                    ),
                    title='Excel Iteration'
                )
            ],
            title='Iteration - Python vs. Excel'
        ),
        TwoColumnFrame(
            [
                UnorderedList([
                    DimAndRevealListItems([
                        "There's a few things to unpack here",
                        f"Here's another type of object: not a number or a string, but a {list_}",
                        f"A {list_} holds multiple objects, and you can add or remove items from {list_}s",
                    ])
                ])
            ],
            [
                example_python_iteration
            ],
            title='Explaining Python Iteration'
        ),
        TwoColumnFrame(
            [
                UnorderedList([
                    DimAndRevealListItems([
                        "Here we define a list of three numbers as inputs",
                        f"Then we use a {for_} loop to get each input out of the list, and add 2 to it to create the new value",
                        "Finally we print each value as it is generated"
                    ])
                ])
            ],
            [
                example_python_iteration
            ],
            title='Explaining Python Iteration (pt. 2)'
        ),
        Frame(
            [
                LabBlock(
                    [
                        UnorderedList([
                            "Now we want to see the effect of savings rate on time until retirement, in addition to interest rate",
                            "In both Excel and Python, calculate the years to retirement for savings rates of 10%, 25%, and 40%, "
                            "and each of these cases with each of the interest rate cases, 4%, 5%, and 6%",
                            f"Be sure that you drag formulas in Excel and use {for_} loops in Python to accomplish this"
                        ])
                    ],
                    title="Let's Vary the Savings Rate, Too"
                ),
                Block(
                    "In total you should have 9 calculated years to retirement numbers, in each of the two models.",
                    title='Note'
                )
            ],
            title="Putting it All Together - A Basic Model with Iteration"

        )
    ]
