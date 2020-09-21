import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll
from pyexlatex.models.format.breaks import OutputLineBreak

import plbuild
from build_tools.config import SITE_URL
from lectures.lab_exercises.notes import get_python_basics_conditionals_lab_lecture, \
    get_python_basics_lists_lab_lecture, get_python_basics_functions_lab_lecture, \
    get_python_basics_data_types_lab_lecture, get_python_basics_classes_lab_lecture
from lectures.python_basics.main import get_python_basics_lecture
from plbuild.paths import images_path
from pltemplates.exercises.lab_exercise import LabExercise
from pltemplates.frames.in_class_example import InClassExampleFrame
from pltemplates.graphics.model_structure import get_model_structure_graphic
from pltemplates.hyperlink import Hyperlink

from pltemplates.frames.model_flowchart import (
    ModelFlowchartFrame,
    real_world_style,
    model_style,
    in_out_style
)
from pltemplates.blocks import LabBlock
from schedule.main import LECTURE_4_NAME

TITLE = LECTURE_4_NAME
SHORT_TITLE = 'Python Basics'
SUBTITLE = 'How to Structure Python Code and Common Operations'
ORDER = 'S4'

AUTHORS = ['Nick DeRobertis']
SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [['University of Florida', 'Department of Finance, Insurance, and Real Estate']]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = plbuild.paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = plbuild.paths.HANDOUTS_BUILD_PATH


def get_content():
    lecture = get_python_basics_lecture()
    conditionals_lab = get_python_basics_conditionals_lab_lecture().to_pyexlatex()
    lists_lab = get_python_basics_lists_lab_lecture().to_pyexlatex()
    functions_lab = get_python_basics_functions_lab_lecture().to_pyexlatex()
    data_types_lab = get_python_basics_data_types_lab_lecture().to_pyexlatex()
    classes_lab = get_python_basics_classes_lab_lecture().to_pyexlatex()
    appendix_frames = [
        *conditionals_lab.appendix_frames(),
        *lists_lab.appendix_frames(),
        *functions_lab.appendix_frames(),
        *data_types_lab.appendix_frames(),
        *classes_lab.appendix_frames()
    ]


    next_slide = lp.Overlay([lp.NextWithIncrement()])
    function_example = pl.Python(
"""
def my_func(a, b, c=10):
    return a + b + c

>>> my_func(5, 6)
21
""")

    use_class_example = pl.Python(
"""
from car_example import Car

>>> my_car = Car('Honda', 'Civic')
>>> print(my_car)
Car(make='Honda', model='Civic')
>>> type(my_car)
car_example.Car
>>> my_car.make
'Honda'
>>> my_car.drive()
'The Honda Civic is driving away!'
""")

    dataclass_example = pl.Python(
"""
from dataclasses import dataclass

@dataclass
class ModelInputs:
    interest_rates: tuple = (0.05, 0.06, 0.07)
    pmt: float = 1000

>>> inputs = ModelInputs(pmt=2000)
>>> print(inputs)
ModelInputs(interest_rates=(0.05, 0.06, 0.07), pmt=2000)
>>> type(inputs)
__main__.ModelInputs
>>> inputs.interest_rates
(0.05, 0.06, 0.07)
>>> inputs.pmt
2000
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
    f_string_example = pl.Python(
"""
>>> my_num = 5 / 6
>>> print(my_num)
0.8333333333333334
>>> print(f'My number is {my_num:.2f}')
'My number is 0.83'
"""
    )
    f_string = pl.Monospace("f''")
    f_mono = pl.Monospace('f')
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

    site_link = Hyperlink(SITE_URL, 'the course site')

    return [
        pl.Section(
            [
                lp.TwoColumnGraphicDimRevealFrame(
                    [
                        "Now we are going to build our first complex Python model",
                        "We will also learn a bit more Python before we can get there",
                        "Just as we did in Excel, we need to add structure to make the model navigatable",
                        "Logic should be organized in functions and be documented",
                    ],
                    graphics=[
                        images_path('python-logo.png')
                    ],
                    title='An Organized Structure of an Advanced Python Model'
                ),
                lp.GraphicFrame(
                    [
                        get_model_structure_graphic()
                    ],
                    title='The Structure of a Complex Model'
                ),
            ],
            title='Introduction',
            short_title='Intro'
        ),
        pl.Section(
            [
                lp.Frame(
                    [
                        lp.Block(
                            [
                                pl.TextSize(-1),
                                if_example,
                            ],
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
                        [pl.Monospace('elif'),
                         ' is a shorthand for else if, e.g. not the last condition, but this condition']
                    ],
                    title='Explaining the If-Else Statements'
                ),
                InClassExampleFrame(
                    [
                        f"On {site_link}, there is a Jupyter notebook called Python Basics containing all "
                        f"of the examples for today's lecture",
                        'Now I will go through the example material under "Conditionals"'
                    ],
                    title='Conditionals Example',
                    block_title='Trying out Conditionals'
                ),
                conditionals_lab.presentation_frames(),
            ],
            title='Conditionals'
        ),
        pl.Section(
            [
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
                        pl.UnorderedList([
                            'Index is base zero (0 means first item, 1 means second item)',
                        ]),
                        pl.VFill(),
                        list_indexing_example,
                    ],
                    title='List Indexing and Slicing'
                ),
                InClassExampleFrame(
                    [
                        "We will keep working off of Python Basics.ipynb",
                        'Now I will go through the example material under "Working more with Lists"'
                    ],
                    title='Lists Example',
                    block_title='Doing More with Lists'
                ),
                lists_lab.presentation_frames(),
            ],
            title='More with Lists',
            short_title='Lists'
        ),
        pl.Section(
            [
                lp.DimRevealListFrame(
                    [
                        "In Python, we can group logic into functions",
                        "Functions have a name, inputs, and outputs",
                        "Functions are objects like everything else in Python",
                        function_example,
                    ],
                    title='Functions - Grouping Reusable Logic'
                ),
                InClassExampleFrame(
                    [
                        "We will keep working off of Python Basics.ipynb",
                        'Now I will go through the example material under "Functions"'
                    ],
                    title='Functions Example',
                    block_title='Structuring Code using Functions'
                ),
                functions_lab.presentation_frames(),
            ],
            title='Functions'
        ),
        pl.Section(
            [
                lp.DimRevealListFrame(
                    [
                        'In Python, everything is an object except for variable names, which are references to objects',
                        'Every object has a type. We have learned about strings, numbers, lists, and booleans (True, False)',
                        'In the next section on classes, we will learn more about the relationship between the type '
                        'and the object'
                    ],
                    title='What are Types?'
                ),
                # TODO [#12]: add f-strings to Jupyter example
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
                    title='Formatting Python Strings'
                ),
                lp.DimRevealListFrame(
                    [
                        'So far I have just said that numbers are a type in Python, but this is a simplification',
                        ['There are two main types of numbers in python:', pl.Monospace('float'), 'and',
                         pl.Monospace('int'), 'corresponding to a floating point number and an integer, respectively'],
                        ['An', pl.Monospace('int'), 'is a number without decimals, while a', pl.Monospace('float'),
                         'has decimals, regardless of whether they are zero'],
                        ['For example,', pl.Monospace('3.5'), 'and', pl.Monospace('3.0'), 'are floats, while',
                         pl.Monospace('3'), 'is an int, even though', pl.Monospace('3.0 == 3 is True')],
                        ["Usually, this doesn't matter. But to loop a number of times, you must pass an",
                         pl.Monospace('int')]
                    ],
                    title='Numeric Types'
                ),
                lp.DimRevealListFrame(
                    [
                        ['A', pl.Monospace('tuple'), 'is like a', pl.Monospace('list'), "but you can't change it after "
                         "it has been created (it is immutable)"],
                        ['Tuples are in parentheses instead of brackets, e.g.', pl.Monospace('("a", "b")')],
                        ['A', pl.Monospace('dict'), 'short for dictionary, stores a mapping. Use them if you want '
                         'to store values associated to other values'],
                        ['We will come back to', pl.Monospace('dicts'), 'later in the course, but I wanted to',
                         'introduce them now as they are a very fundamental data type']
                    ],
                    title='Additional Built-In Types'
                ),
                InClassExampleFrame(
                    [
                        "We will keep working off of Python Basics.ipynb",
                        'Now I will go through the example material under "Exploring Data Types"'
                    ],
                    title='Data Types Example',
                    block_title='Understanding the Different Data Types'
                ),
                data_types_lab.presentation_frames(),
            ],
            title='More about Data Types',
            short_title='Data Types'
        ),
        pl.Section(
            [
                lp.GraphicFrame(
                    images_path('class-object.pdf'),
                    title='Overview of Classes and Objects'
                ),
                lp.DimRevealListFrame(
                    [
                        'In Python, everything is an object except for variable names, which are references to objects',
                        'Strings, floats, ints, lists, and tuples are types of objects. There are many more types of '
                        'objects and users can define their own types of objects',
                        'A class is a definition for a type of object. It defines how it is created, the data '
                        'stored in it, and the functions attached to it',
                        'We can write our own classes to create new types of objects to work with'
                    ],
                    title='Everything is an Object. Every Object has a Class'
                ),
                lp.DimRevealListFrame(
                    [
                        'From a single class definition, an unlimited number of objects can be created',
                        'Typically the class definition says it should accept some data to create the object',
                        'Then when you have multiple objects of the same type (created from the same class), '
                        'they will have the same functions (methods) attached to them, but different data stored within',
                        ['For example, we can create two different lists. They will have different contents, but we can',
                        'do', pl.Monospace('.append'), 'on either of the lists']
                    ],
                    title='Many Objects to One Class'
                ),
                lp.MultiGraphicFrame(
                    [
                        images_path('class-object.pdf'),
                        images_path('list-object.pdf')
                    ],
                    title='Lists are Objects',
                    vertical=False
                ),
                lp.MultiGraphicFrame(
                    [
                        images_path('class-object.pdf'),
                        images_path('car-object.pdf')
                    ],
                    title='We can Make Custom Objects Too',
                    vertical=False
                ),
                lp.Frame(
                    [
                        pl.UnorderedList(['Constructing an object from a class looks like calling a function:']),
                        lp.Block(
                            [
                                pl.TextSize(-1),
                                use_class_example,
                            ],
                            title='Using Custom Classes in Python'
                        ),
                    ],
                    title='Creating and Using Objects'
                ),
                lp.DimRevealListFrame(
                    [
                        'I will not be teaching you about creating general classes in this course. It is very useful '
                        'but is generally more advanced. I encourage you to learn them outside the course.',
                        "We covered this material for two reasons:",
                        ['To give a better understanding of how Python works in general, and why sometimes we '
                        'call functions as', pl.Monospace('something.my_func()'), 'rather than',
                         pl.Monospace('my_func()')],
                        ['We are going to use', pl.Monospace('dataclasses'), 'to store our model data. They are',
                         'a simplified version of classes used mainly for storing data.']
                    ],
                    title='Where we Will Focus in This Course'
                ),
                lp.Frame(
                    [
                        pl.UnorderedList(['An organized way to store our model input data:']),
                        lp.Block(
                            [
                                pl.TextSize(-3),
                                dataclass_example,
                            ],
                            title='Using Dataclasses in Python'
                        ),
                    ],
                    title='Dataclass Intro'
                ),
                lp.DimRevealListFrame(
                    [
                        ['A', pl.Monospace('dataclass'), 'is just a class which is more convenient to create, and',
                         'is typically used to group data together'],
                        ['If you need to pass around multiple variables together, they make sense. For our models, we '
                        'will want to pass around all the inputs, so one', pl.Monospace('dataclass'), 'for all the',
                         'inputs to the model makes sense'],
                        'This way instead of having to pass around every input individually to every function, just '
                        'pass all the input data as one argument',
                        ['Also enables easy tab-completion. What were the names of my inputs? Just hit tab after',
                         pl.Monospace('data.')]
                    ],
                    title='What, When and Why Dataclasses?'
                ),
                InClassExampleFrame(
                    [
                        "We will keep working off of Python Basics.ipynb",
                        'For this example, also go and download car_example.py and put it in the same folder',
                        'Now I will go through the example material under "Working with Classes"'
                    ],
                    title='Classes Example',
                    block_title='Working with Classes and Creating Dataclasses'
                ),
                classes_lab.presentation_frames(),
            ],
            title='Classes and Dataclasses',
            short_title='Classes'
        ),
        pl.Section(
            [
                # TODO [#13]: add error handling to Jupyter example
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
                            [
                                pl.TextSize(-1),
                                annuity_example,
                            ],
                            title='Calculating the Sum of Unaligned Annuity Cash-Flows'
                        )
                    ],
                    title='Applying Error Handling'
                ),
            ],
            title='Error Handling',
            short_title='Errors'
        ),
        pl.PresentationAppendix(
            [
                lecture.pyexlatex_resources_frame,
                *appendix_frames
            ]
        )
    ]

DOCUMENT_CLASS_KWARGS = dict(
    nav_header=True,
    toc_sections=True
)
OUTPUT_NAME = TITLE

# lp.Frame(
#     [
#         lp.Block(
#             enumerate_example,
#             title='Enumerate and String Formatting'
#         ),
#         pl.UnorderedList([
#             lp.DimAndRevealListItems([
#                 ['Use ', pl.Monospace('enumerate'),
#                  ' to get a counter for the loop number along with the input'],
#                 ['Use ', pl.Monospace("f'\{my_input\} in a string'"), ' to place the string version of ',
#                  pl.Monospace('my_input'), ' into the string " in a string"'],
#             ])
#         ])
#     ],
#     title='More Python Iteration, and String Formatting'
# ),

# lp.DimRevealListFrame(
#     [
#         ["In Python, we can create our own custom types of objects using a ", pl.Monospace('class')],
#         "This is often used to group functions together, and to represent something",
#         "We will use classes to represent models, and write functions and methods for the actual model equations and logic",
#     ],
#     title='Classes - Representing Things and Grouping Functions'
# ),
# lp.Frame(
#     [
#         class_example,
#     ],
#     title='Classes - An Example'
# ),

# lp.Frame(
#     [
#         pl.UnorderedList([
#             'We covered a lot today, so the lab session is straightforward.'
#         ]),
#         pl.VFill(),
#         LabBlock(
#             pl.UnorderedList([
#                 "Make sure that you're able to reproduce all the exercises we completed in class",
#                 "Also ensure that you understand what we're doing and why"
#             ]),
#             title='Getting the Basics'
#         )
#     ],
#     title="Let's Make Sure you Have the Basics Before Doing Something Hard"
# )

#     class_example = pl.Python(
# """
# class MyClass:
#
#     def __init__(self, a, b, c=10):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def sum_inputs(self):
#         return self.a + self.b + self.c
#
# >>> my_obj = MyClass(5, 6)
# >>> type(my_obj)
# __main__.MyClass
# >>> my_obj.sum_inputs()
# 21
# """)