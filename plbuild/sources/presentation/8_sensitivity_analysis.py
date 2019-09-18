import itertools
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
from pltemplates.graphics.explore_params import explore_parameters_graphic
from pltemplates.frames.sensitivity_example import get_sensitivity_analysis_example_frames

AUTHORS = ['Nick DeRobertis']
SHORT_TITLE = 'Sensitivity Analysis'
SUBTITLE = 'Pt. 1: Sensitivity Analysis'

SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [
    ['University of Florida', 'Department of Finance, Insurance, and Real Estate'],
]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = plbuild.paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = plbuild.paths.HANDOUTS_BUILD_PATH
TITLE = 'Exploring the Parameter Space'
ORDER = 8


def get_content():
    pd_mono = pl.Monospace('pandas')
    series_mono = pl.Monospace('Series')
    df_mono = pl.Monospace('DataFrame')
    apply_mono = pl.Monospace('apply')
    import_mono = pl.Monospace('import')
    for_mono = pl.Monospace('for')
    dict_mono = pl.Monospace('dict')
    np_mono = pl.Monospace('numpy')
    pd_mono = pl.Monospace('pandas')
    import_something_mono = pl.Monospace('import something')
    something_file = pl.Monospace('something.py')
    numpy_file = pl.Monospace('numpy.py')
    def_mono = pl.Monospace('def')
    class_mono = pl.Monospace('class')
    sensitivity_file_mono = pl.Monospace('sensitivity.py')
    sensitivity_import = pl.Monospace('import sensitivity')
    sensitivity_func_mono = pl.Monospace('sensitivity.sensitivity_hex_plots?')

    series_ex_1 = pl.Python(
"""
>>> df = pd.DataFrame()
>>> df['Numbers'] = [1, 2, 3]
>>> df['Categories'] = ['apple', 'apple', 'orange']
>>> df
"""
    )
    series_ex_2 = pl.Python(
"""
>>> df['Categories']
0     apple
1     apple
2    orange
Name: Categories, dtype: object
>>> type(df['Categories'])
pandas.core.series.Series
"""
    )
    series_ex_3 = pl.Python(
"""
>>> cats = df['Categories']
>>> cats
0     apple
1     apple
2    orange
Name: Categories, dtype: object
>>> cats[2]
'orange'
>>> cats.index = ['a', 'b', 'c']
>>> cats
a     apple
b     apple
c    orange
Name: Categories, dtype: object
>>> cats['b']
'apple'
"""
    )

    list_comprehension_ex_1 = pl.Python(
"""
>>> out_values = []
>>> for i in range(5):
>>>     out_values.append(i + 10)
>>> out_values
[10, 11, 12, 13, 14]
"""
    )

    list_comprehension_ex_2 = pl.Python(
"""
>>> out_values = [i + 10 for i in range(5)]
>>> out_values
[10, 11, 12, 13, 14]
"""
    )
    dict_example = pl.Python(
"""
>>> coffee_levels_emotions = {
>>>     'high': 'happy',
>>>     'pretty high': 'happy',
>>>     'medium': 'neutral',
>>>     'low': 'sad',
>>>     'empty': 'desparate'
>>> }
>>> coffee_levels_emotions['pretty high']
'happy'
>>> for coffee_level, emotion in coffee_levels_emotions.items():
>>>     print(f"I'm {emotion} when my coffee is {coffee_level}")
"""
    )

    dict_printout = """
I'm happy when my coffee is high
I'm happy when my coffee is pretty high
I'm neutral when my coffee is medium
I'm sad when my coffee is low
I'm desparate when my coffee is empty
    """

    dict_printouts_mono = [pl.Monospace(item) for item in dict_printout.split('\n') if item]
    dict_printout_output = []
    for po in dict_printouts_mono:
        dict_printout_output.append(po)
        dict_printout_output.append('')

    dict_example_2 = pl.Python(
"""
>>> coffee_levels_emotions.update({'overflowing': 'burned'})
>>> coffee_levels_emotions['negative'] = 'confused'
>>> high_value = coffee_levels_emotions.pop('high')
>>> coffee_levels_emotions
{'pretty high': 'happy',
 'medium': 'neutral',
 'low': 'sad',
 'empty': 'desparate',
 'overflowing': 'burned',
 'negative': 'confused'}
>>> high_value
'happy'
"""
    )

    return [
        lp.DimRevealListFrame(
            [
                'So far, I have given you some inputs to use and you have been getting one or more outputs from '
                'those inputs',
                'We have not considered how those inputs may change, and how that affects the outputs',
                'This is where building a model vs. doing a calculation really starts to pay off'
            ],
            title='Moving from a Static Model'
        ),
        lp.GraphicFrame(
            explore_parameters_graphic(),
            title='How to Explore Inputs and their Affect on Outputs'
        ),
        lp.DimRevealListFrame(
            [
                'In this lecture, we will be discussing sensitivity analysis as an approach to exploring the '
                'parameter space.',
                'After we cover probabilistic modeling, we will revisit exploring the parameter space with a '
                'method called Monte Carlo Simulation.',
                'In sensitivity analysis, a fixed set of values for the parameters are chosen, while in Monte Carlo '
                'Simulation, each parameter is assigned a distribution.',
                'Both methods may be used together to fully understand a model.'
            ],
            title='Methods of Parameter Exploration'
        ),
        lp.Frame(
            [
                'For the model given by:',
                pl.Equation(str_eq='y = f(X)', inline=False),
                pl.Equation(str_eq='X = [x_1, x_2, ..., x_n]', inline=False),
                pl.UnorderedList([
                    [pl.Equation(str_eq='y:'), 'Model output'],
                    [pl.Equation(str_eq='X:'), 'Model input matrix'],
                    [pl.Equation(str_eq='x_i:'), 'Value of $i$th $x$ variable']

                ]),
                'Follow the following steps:',
                pl.OrderedList([
                    ['Choose a set of values for each', pl.Equation(str_eq='x_i')],
                    ['Take the cartesian product of these values as', pl.Equation(str_eq='[X_1, X_2, ..., X_m]')],
                    ['For each', pl.Equation(str_eq='X_i'), 'calculate', pl.Equation(str_eq='y_i = f(X_i)')],
                    ['Store the values of', pl.Equation(str_eq='X_i'), 'mapped to', pl.Equation(str_eq='y_i')],
                    ['Visualize', pl.Equation(str_eq='y_i'), 'versus', pl.Equation(str_eq='X_i')]
                ])
            ],
            title='Sensitivity Analysis, Formally'
        ),
        get_sensitivity_analysis_example_frames(),
        lp.GraphicFrame(
            images_path('excel-data-table.png'),
            title='Sensitivity Analysis in Excel'
        ),
        lp.DimRevealListFrame(
            [
                'There are two main ways to visualize sensitivity analysis results in Excel: graphing and '
                'conditional formatting.',
                'Graphing is usually appropriate for one-way data tables',
                'Conditional formatting is usually appropriate for two-way data tables'
            ],
            title='Visualizing Sensitivity Analysis in Excel'
        ),
        lp.GraphicFrame(
            images_path('excel-conditional-formatting.png'),
            title='Conditional Formatting in Excel'
        ),
        lp.GraphicFrame(
            images_path('python-sensitivity-hex-bins.pdf'),
            title='Sensitivity Analysis in Python'
        ),
        lp.Frame(
            [
                "We'll cover a couple more Python patterns and a new data type before jumping into sensitivity analysis",
                pl.UnorderedList([
                    'Dictionaries',
                    'List comprehensions',
                    ['Python', import_mono, 'system and custom code']
                ])
            ],
            title=f'Going Deeper into Python Code Structure'
        ),
        lp.Frame(
            [
                lp.Block(
                    [
                        list_comprehension_ex_1
                    ],
                    title=f'The Original Way'
                ),
                lp.Block(
                    [
                        list_comprehension_ex_2
                    ],
                    title=f'With List Comprehension'
                ),
                lp.Block(
                    ['You', pl.Bold('never'),
                     'need to use list comprehension, it is just for convenience. The original', for_mono,
                     'loop syntax will always work fine.'],
                    title='Notice'
                )
            ],
            title=f"An Easier way to Build Simple Lists from Loops"
        ),
        lp.TwoColumnGraphicDimRevealFrame(
            [
                ['A dictionary, or', dict_mono,
                 'for short, is another basic Python data type like lists, numbers, and strings.'],
                'Like a list, it is a collection: it holds other objects.',
                ['Unlike a list, a', dict_mono,
                 'is composed of key-value pairs. It holds relationships between objects.']
            ],
            graphics=[
                lg.ModifiedPicture(
                    images_path('dictionary-book.jpg'),
                    draw_items=[
                        lg.Path('draw', [(0.5, 0.5)], draw_type='circle',
                                options=['radius=0.4', 'red', 'line width=5mm']),
                        lg.Path('draw', [(0.2, 0.75), (0.8, 0.2)], draw_type='--', options=['red', 'line width=5mm'])
                    ]
                )
            ],
            title='What is a Dictionary?'
        ),
        lp.Frame(
            [
                lp.Block(
                    [
                        pl.TextSize(-1),
                        dict_example,
                        *dict_printout_output
                    ],
                    title='Basic Dictionary Example'
                )
            ],
            title='How to Use Dictionaries'
        ),
        lp.Frame(
            [
                lp.Block(
                    [
                        dict_example_2,
                    ],
                    title='Add and Delete Items from Dictionaries'
                )
            ],
            title='How to Modify Dictionaries'
        ),
        lp.DimRevealListFrame(
            [
                ['In the past we have used', import_mono, 'to load packages such as', np_mono, 'and', pd_mono],
                ['These packages are just Python files. We can also write our own Python files and', import_mono,
                 'them the same way'],
                [f'When you {import_something_mono}, Python first searches the current directory for a file',
                 something_file, "and if it doesn't find it, it searches your installed packages"],
                ['In fact if you added a', numpy_file, 'in the current directory and tried to', import_mono, np_mono,
                 'it would', import_mono, 'the contents of that file rather than the', np_mono, 'package.']
            ],
            title=f'Understanding Python {import_mono}s'
        ),
        lp.DimRevealListFrame(
            [
                ['You can write your own functions and classes, then put them in a Python file and', import_mono,
                 'them into your notebook.'],
                ['When you', import_mono, 'a file, it executes the contents of that file. So you generally want just '
                 'function and class definitions, and not really anything outside of', def_mono, 'or', class_mono,
                 'statements.'],
                'Using Python files is a more maintainable structure for building complex models and apps versus '
                'Jupyter notebooks only.'
            ],
            title='Importing Custom Code'
        ),
        lp.Frame(
            [
                LabBlock(
                    pl.UnorderedList(
                        [
                            ['Go to Canvas and download', sensitivity_file_mono, 'from the Python Modules folder'],
                            'Place this Python file in the same folder as your Jupyter notebook',
                            ['In the notebook, run', sensitivity_import],
                            ['Then run a cell with', sensitivity_func_mono,
                             'to ensure it is loaded properly. You should see the docstring.']
                        ]
                    ),
                    title='Import Custom Code for Sensitivity Analysis'
                ),
            ],
            title='Some Final Setup for Python Sensitivity Analysis'
        )

    ]

DOCUMENT_CLASS_KWARGS = {}
OUTPUT_NAME = TITLE

