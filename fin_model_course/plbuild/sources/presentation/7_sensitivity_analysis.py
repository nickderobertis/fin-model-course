import itertools
import random

import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

import plbuild
from lectures.lab_exercises.notes import get_sensitivity_analysis_excel_lab_lecture, get_dictionaries_lab_lecture, \
    get_list_comprehensions_lab_lecture, get_sensitivity_analysis_python_lab_lecture
from lectures.sensitivity_analysis.main import get_sensitivity_analysis_lecture
from plbuild.paths import images_path
from pltemplates.exercises.lab_exercise import LabExercise
from pltemplates.frames.in_class_example import InClassExampleFrame
from pltemplates.frames.model_flowchart import (
    ModelFlowchartFrame,
    real_world_style,
    model_style,
    in_out_style
)
from pltemplates.blocks import LabBlock
from pltemplates.graphics.explore_params import explore_parameters_graphic
from pltemplates.frames.sensitivity_example import get_sensitivity_analysis_example_frames
from schedule.main import LECTURE_7_NAME

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
TITLE = LECTURE_7_NAME
ORDER = 'S7'


def get_content():
    random.seed(1000)

    lecture = get_sensitivity_analysis_lecture()
    sensitivity_excel_lab = get_sensitivity_analysis_excel_lab_lecture().to_pyexlatex()
    dictionaries_lab = get_dictionaries_lab_lecture().to_pyexlatex()
    list_comp_lab = get_list_comprehensions_lab_lecture().to_pyexlatex()
    sensitivity_python_lab = get_sensitivity_analysis_python_lab_lecture().to_pyexlatex()
    appendix_frames = [
        lecture.pyexlatex_resources_frame,
        sensitivity_excel_lab.appendix_frames(),
        dictionaries_lab.appendix_frames(),
        list_comp_lab.appendix_frames(),
        sensitivity_python_lab.appendix_frames(),
    ]

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
    pip_install_mypackage = pl.Monospace('pip install mypackage')
    jupyter_install_mypackage = pl.Monospace('!pip install mypackage')
    itertools_product = pl.Monospace('itertools.product')
    sensitivity = pl.Monospace('sensitivity')

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

    plain_sensitivity_example = pl.Python(
"""
inp1_values = [1, 2]
inp2_values = [4, 5]
results = []
for inp1 in inp1_values:
    for inp2 in inp2_values:
        result = model(inp1, inp2,)
        results.append(
            (inp1, inp2, result)
        )
pd.DataFrame(results, columns=['inp1', 'inp2',  'Result'])
"""
    )

    easy_sensitivity_example = pl.Python(
"""
from sensitivity import SensitivityAnalyzer

sensitivity_values = {
    'inp1': [1, 2],
    'inp2': [4, 5],
}
sa = SensitivityAnalyzer(sensitivity_values, model)
sa.df
"""
    )

    return [
        pl.Section(
            [
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
                        pl.TextSize(-1),
                        'In this lecture, we will be discussing sensitivity analysis as an approach to exploring the '
                        'parameter space.',
                        'After we cover probabilistic modeling, we will revisit exploring the parameter space with other '
                        'methods: scenario analysis and Monte Carlo Simulation.',
                        'In sensitivity analysis, a fixed set of values for the parameters are chosen, while in Monte Carlo '
                        'Simulation, each parameter is assigned a distribution.',
                        'In scenario analysis, several realistic cases of the inputs are chosen which represent '
                        'possible real-world situations',
                        'All three methods may be used together to fully understand a model.'
                    ],
                    title='Methods of Parameter Exploration'
                ),
            ],
            title='Introduction to Parameter Exploration',
            short_title='Explore Parameters'
        ),
        pl.Section(
            [
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
                            ['Take the cartesian product of these values as',
                             pl.Equation(str_eq='[X_1, X_2, ..., X_m]')],
                            ['For each', pl.Equation(str_eq='X_i'), 'calculate', pl.Equation(str_eq='y_i = f(X_i)')],
                            ['Store the values of', pl.Equation(str_eq='X_i'), 'mapped to', pl.Equation(str_eq='y_i')],
                            ['Visualize', pl.Equation(str_eq='y_i'), 'versus', pl.Equation(str_eq='X_i')]
                        ])
                    ],
                    title='Sensitivity Analysis, Formally'
                ),
                get_sensitivity_analysis_example_frames(),
            ],
            title='Sensitivity Analysis Theory',
            short_title='SA Theory'
        ),
        pl.Section(
            [
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
                InClassExampleFrame(
                    [
                        'I will now go through adding sensitivity analysis to the Dynamic Salary Retirement Model '
                        'in Excel',
                        'The completed exercise on the course site, '
                        '"Dynamic Salary Retirement Model Sensitivity.xlsx"'
                    ],
                    title='Sensitivity Analysis in Excel',
                    block_title='Adding Sensitivity Analysis to the Dynamic Retirement Excel Model'
                ),
                sensitivity_excel_lab.presentation_frames(),
            ],
            title='Sensitivity Analysis in Excel with Data Tables',
            short_title='SA Excel'
        ),
        pl.Section(
            [
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
                                lg.Path('draw', [(0.2, 0.75), (0.8, 0.2)], draw_type='--',
                                        options=['red', 'line width=5mm'])
                            ]
                        )
                    ],
                    title='What is a Dictionary?'
                ),
                lp.Frame(
                    [
                        lp.Block(
                            [
                                pl.TextSize(-2),
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
                InClassExampleFrame(
                    [
                        'I will now start going through the example notebook called '
                        '"Python Dicts, List comprehensions, and Imports.ipynb"',
                        'I will go through the Dictionaries section for now'
                    ],
                    title='More About Dictionaries in Python',
                    block_title='Using Dictionaries'
                ),
                dictionaries_lab.presentation_frames(),
                lp.Frame(
                    [
                        pl.TextSize(-1),
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
                InClassExampleFrame(
                    [
                        'I will continue going through the example notebook '
                        '"Python Dicts, List comprehensions, and Imports.ipynb"',
                        'I will go through the List Comprehensions section for now'
                    ],
                    title='Easier Loops in Python',
                    block_title='Using List Comprehensions'
                ),
                list_comp_lab.presentation_frames(),
                lp.DimRevealListFrame(
                    [
                        ['In the past we have used', import_mono, 'to load packages such as', np_mono, 'and', pd_mono],
                        ['These packages are just Python files. We can also write our own Python files and',
                         import_mono,
                         'them the same way'],
                        [f'When you {import_something_mono}, Python first searches the current directory for a file',
                         something_file, "and if it doesn't find it, it searches your installed packages"],
                        ['In fact if you added a', numpy_file, 'in the current directory and tried to', import_mono,
                         np_mono,
                         'it would', import_mono, 'the contents of that file rather than the', np_mono, 'package.']
                    ],
                    title=f'Understanding Python {import_mono}s'
                ),
                lp.DimRevealListFrame(
                    [
                        ['You can write your own functions and classes, then put them in a Python file and',
                         import_mono,
                         'them into your notebook.'],
                        ['When you', import_mono,
                         'a file, it executes the contents of that file. So you generally want just '
                         'function and class definitions, and not really anything outside of', def_mono, 'or',
                         class_mono,
                         'statements.'],
                        'Using Python files is a more maintainable structure for building complex models and apps versus '
                        'Jupyter notebooks only.'
                    ],
                    title='Importing Custom Code'
                ),
                lp.DimRevealListFrame(
                    [
                        'Sometimes you will need a package which does not already come installed with Anaconda',
                        ['The general way to do this is with', pip_install_mypackage, 'replacing mypackage with',
                         'the package you want to install'],
                        ['You would run this in Anaconda Prompt, or in Jupyter you can run it but you need to put an '
                        'exclaimation mark before it to say you want to run it in a terminal. So in Jupyter it would be',
                        jupyter_install_mypackage]
                    ],
                    title='Installing Packages'
                ),
                InClassExampleFrame(
                    [
                        'I will continue going through the example notebook '
                        '"Python Dicts, List comprehensions, and Imports.ipynb"',
                        'I will go through the Imports and Installing Packages section for now'
                    ],
                    title='Installing Packages in Python',
                    block_title='How to Install Packages'
                ),

            ],
            title='Python List Comprehensions, Installing Packages, and More on Dictionaries',
            short_title='Extra Python Basics'
        ),
        pl.Section(
            [
                lp.GraphicFrame(
                    images_path('python-sensitivity-hex-bins.pdf'),
                    title='Sensitivity Analysis in Python - Hex-Bin'
                ),
                lp.GraphicFrame(
                    images_path('sensitivity-analysis-styled-df.png'),
                    title='Sensitivity Analysis in Python - Styled DataFrame'
                ),
                lp.DimRevealListFrame(
                    [
                        'Generally, to do sensitivity analysis in Python without any special tools, you would just '
                        'create one nested for loop for each input, and finally within all the loops, run your model '
                        'with the inputs from the loops',
                        'This will work fine, but you will have many nested loops which can become hard to read. Also '
                        'it is a fair bit of setup involved.',
                        ['You can avoid the nested loops with', itertools_product, 'but then this becomes more '
                         'difficult to use and read']

                    ],
                    title='How to Do Sensitivity Analysis in Python (The Hard Way)'
                ),
                lp.Frame(
                    [
                        pl.TextSize(-3),
                        pl.UnorderedList([
                            'Say you have a function which runs your model, called model, which takes inputs of '
                            'inp1 and inp2'
                        ]),
                        lp.Block(
                            [
                                plain_sensitivity_example,
                                pl.Graphic(images_path('plain-sensitivity-result.png'), width=0.2),
                            ],
                            title='Sensitivity Analysis in Python with No Libraries'
                        )
                    ],
                    title='Sensitivity Analysis Example (Hard Way)'
                ),
                lp.DimRevealListFrame(
                    [
                        "When I first created this course, I thought there should be a good sensitivity analysis "
                        "tool in Python and I couldn't find it",
                        "The beauty of Python is if you want a tool that doesn't exist, you can create it, and "
                        "share it with others so that nobody else has to deal with the problem.",
                        ['So I created', sensitivity, 'a package for sensitivity analysis in Python, '
                                                      'which makes it very easy']

                    ],
                    title='How to Do Sensitivity Analysis in Python (The Easy Way)'
                ),
                lp.Frame(
                    [
                        pl.TextSize(-3),
                        pl.UnorderedList([
                            'Say you have a function which runs your model, called model, which takes inputs of '
                            'inp1 and inp2'
                        ]),
                        lp.Block(
                            [
                                easy_sensitivity_example,
                                pl.Graphic(images_path('plain-sensitivity-result.png'), width=0.2),
                            ],
                            title=f'Sensitivity Analysis in Python with {sensitivity}'
                        )
                    ],
                    title='Sensitivity Analysis Example (Easy Way)'
                ),
                InClassExampleFrame(
                    [
                        'I will now go through Sensitivity Analysis example Jupyter notebook',
                        'This notebook shows both the standard approach and using the sensitivity package',
                    ],
                    title='Intro to Sensitivity Analysis in Python',
                    block_title='An Overview of the Manual and Automated Approaches'
                ),
                InClassExampleFrame(
                    [
                        'I will now go through adding sensitivity analysis to the Dynamic Salary Retirement Model '
                        'in Python',
                        'The completed exercise available on the course site is called '
                        '"Dynamic Salary Retirement Model Sensitivity.ipynb"'
                    ],
                    title='Applying Sensitivity Analysis in Python',
                    block_title='Adding Sensitivity Analysis to the Dynamic Retirement Python Model'
                ),
                sensitivity_python_lab.presentation_frames(),
            ],
            title='Sensitivity Analysis in Python',
            short_title='SA Python'
        ),
        pl.PresentationAppendix(appendix_frames),
    ]

DOCUMENT_CLASS_KWARGS = dict(
    nav_header=True,
    toc_sections=True
)
OUTPUT_NAME = TITLE

