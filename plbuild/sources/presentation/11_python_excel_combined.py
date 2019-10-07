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
from pltemplates.eq_with_variable_defs import EquationWithVariableDefinitions
from pltemplates.hyperlink import Hyperlink

xlwings_mono = pl.Monospace('xlwings')

AUTHORS = ['Nick DeRobertis']
SHORT_TITLE = 'Combining Tools'
SUBTITLE = f'Using {xlwings_mono} to Run Python from Excel'

SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [
    ['University of Florida', 'Department of Finance, Insurance, and Real Estate'],
]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = plbuild.paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = plbuild.paths.HANDOUTS_BUILD_PATH
TITLE = 'Combining Excel and Python'
ORDER = 11


def get_content():
    pd_mono = pl.Monospace('pandas')
    dfs_mono = pl.Monospace('DataFrames')
    next_slide = lp.Overlay([lp.UntilEnd(lp.NextWithIncrement())])
    df_to_excel_example = pl.Python("df.to_excel('data.xlsx', sheet_name='My Data', index=False)")
    df_from_excel_example = pl.Python("df = pd.read_excel('data.xlsx', sheet_name='My Data')")
    index_false_mono = pl.Monospace('index=False')
    addin_install_mono = pl.Monospace('xlwings addin install')
    addin_install_success = pl.Monospace('Successfuly installed the xlwings add-in! Please restart Excel.')
    random_seed_py = pl.Monospace('random_seed.py')
    random_seed_excel = pl.Monospace('random_seed.xlsm')
    quickstart_mono = pl.Monospace('xlwings quickstart')
    quickstart_project_mono = pl.Monospace('xlwings quickstart my_project_name')
    cd_mono = pl.Monospace('cd')
    xw_func_decorator = pl.Monospace('@xw.func')
    random_choice_mono = pl.Monospace('random_choice')
    random_choice_py = pl.Monospace('random.choices')
    return [
        pl.Section(
            [
                lp.DimRevealListFrame(
                    [
                        "We have learned how to use both Excel and Python to solve problems. Throughout this process, there "
                        "were advantages and disadvantages of each tool for each problem.",
                        "I wanted you to know both tools so you could pick whichever is best to tackle your problem",
                        "For larger problems, you'll likely find some parts are better with Excel and some with Python",
                        "After this lecture, you won't need to choose one anymore, you can use both at once."
                    ],
                    title='Leveraging the Power of Both Tools'
                ),
            ],
            title='Introduction'
        ),
        pl.Section(
            [
                lp.DimRevealListFrame(
                    [
                        [pd_mono, 'has built-in tools for working with Excel'],
                        [pd_mono, 'can read Excel workbooks into', dfs_mono, 'and it can write', dfs_mono,
                         'back to Excel workbooks'],
                        'For simple uses, this may be enough. If you just need to get data from somewhere once and put it in your '
                        'workbook, or you have your data in Excel and want to analyze it in Python, this is sufficient',
                        [
                            "If you want to manipulate your workbook from Python, or you want to run Python code from your "
                            "workbook, look to", xlwings_mono]
                    ],
                    title=f'How Far does {pd_mono} Get Us?'
                ),
                lp.Frame(
                    [
                        lp.Block(
                            [
                                df_from_excel_example,
                                pl.VSpace(-0.3),
                                pl.UnorderedList([
                                    "If you don't pass a sheet name, it will take the first sheet."
                                ])
                            ],
                            title='Reading Excel Files',
                            overlay=next_slide
                        ),
                        pl.VFill(),
                        lp.Block(
                            [
                                df_to_excel_example,
                                pl.VSpace(-0.3),
                                pl.UnorderedList([
                                    ['We are passing', index_false_mono,
                                     'because usually the 0, 1, 2 ... index is not useful'],
                                    ["If you had set your index to something useful, then don't include",
                                     index_false_mono]
                                ])
                            ],
                            title='Writing to Excel Files',
                            overlay=next_slide
                        ),
                        pl.VFill(),
                        lp.AlertBlock(
                            [
                                ['When', pd_mono,
                                 'writes to a workbook, it replaces the file. Do not write over an existing '
                                 'workbook that you want to keep!']
                            ],
                            title='Careful When Writing!',
                            overlay=next_slide
                        ),
                    ],
                    title=f'Reading and Writing to Excel Files with {pd_mono}'
                ),
            ],
            title=f'To and From Excel with {pd_mono}',
            short_title=pd_mono
        ),
        pl.Section(
            [
                lp.TwoColumnGraphicDimRevealFrame(
                    [
                        ['The easiest way to use Python from in Excel, or Excel from in Python, is', xlwings_mono],
                        "In Windows, it's based off the Microsoft COM API, which is some common tools they give for creating "
                        "plugins.",
                        "It's still in active development, but overall it works pretty well and is far beyond where we were "
                        "a few years ago"
                    ],
                    graphics=[
                        images_path('xlwings-logo.png')
                    ],
                    title=f'Introducing {xlwings_mono}'
                ),
                lp.DimRevealListFrame(
                    [
                        ['There are two main ways to use', xlwings_mono],
                        ['You can', pl.Bold('manipulate Excel from Python,'),
                         'which gives you the full power of Excel from',
                         "within Python. In this class we'll focus on reading and writing values, but you can do anything",
                         "that you would normally be able to in Excel, but by executing Python code."],
                        ['Or you can', pl.Bold('run Python from Excel'), 'using one of two approaches:',
                         pl.Underline('Python as a VBA replacement'), 'and',
                         pl.Underline('user-defined functions (UDFs)')],
                        'We will focus on UDFs first, and come back to the other two approaches.'
                    ],
                    title=f'What are the Main Ways to use {xlwings_mono}?'
                ),
                lp.TwoColumnGraphicDimRevealFrame(
                    [
                        [xlwings_mono,
                         'UDFs allow you to create your own Excel functions, that when executed, run Python code'],
                        'Not only do you gain access to all the functionality of Python, it also becomes easier to work with '
                        'arrays',
                        'You can reference a single cell to get the whole table, and you can output an entire table from '
                        'a single cell formula'
                    ],
                    graphics=[
                        images_path('python-excel-logo.png')
                    ],
                    title='All the Power of Python, In Excel'
                ),
                lp.Frame(
                    [
                        LabBlock(
                            [
                                pl.TextSize(-2),
                                pl.OrderedList([
                                    'Launch Excel and enable "Trust access to the VBA project object model" under '
                                    'File > Options > Trust Center > Trust Center Settings > Macro Settings',
                                    'After hitting OK, now close Excel. '
                                    'Hit the Windows key, type cmd. Launch the command prompt.',
                                    ['In the command prompt, type', addin_install_mono],
                                    ['After a bit, you should see', addin_install_success],
                                    'Launch Excel and ensure that you now see an xlwings tab',
                                    ['Download', random_seed_py, 'and', random_seed_excel, 'from Canvas in the folder',
                                     'Models > Random Seed. Put them both in the same folder.'],
                                    [
                                        f'Open {random_seed_excel}, and change some of the inputs. You should see the random',
                                        'numbers change and also the summary statistics.']
                                ])
                            ],
                            title=f'Setting up {xlwings_mono}'
                        )
                    ],
                    title=f"Let's Get {xlwings_mono} Working"
                ),
            ],
            title=f'Introducing Full Python-Excel Connection with {xlwings_mono}',
            short_title=f'{xlwings_mono} Intro'
        ),
        pl.Section(
            [
                lp.DimRevealListFrame(
                    [
                        [xlwings_mono, 'provides a convenient command', quickstart_mono, 'to get started.'],
                        ['We need to get a command prompt in the folder where you want your project. You',
                         'can use the', cd_mono, 'command in the terminal, but an easier way is to go to the folder,',
                         'hold shift and right click. You will see in the menu "Open command window here", click this'],
                        ['Now in the command prompt, run', quickstart_project_mono,
                         'with whatever project name you want.'],
                        [
                            'In the folder, you should a folder with the project name, and inside it an xlsm and py file also'
                            ' with the project name.'],
                        'You can open the workbook, deleting the xlwings conf sheet. You can open the .py file in Jupyter.'
                    ],
                    title=f'Creating your First {xlwings_mono} Project'
                ),
                lp.DimRevealListFrame(
                    [
                        "To define a UDF, it's nothing but a regular Python function with a little something extra",
                        ['Write the function that does what you want. Then just add', xw_func_decorator, 'on the line',
                         'immediately before the function.'],
                        'Go to the xlwings tab in Excel, and click Import Functions. You should now be able to use your '
                        'function in Excel',
                        'This is the basic usage, you can also add some additional code to specify more about what happens '
                        'when taking in the inputs and returning the outputs.'
                    ],
                    title="Creating a UDF - It's Just a Python Function!"
                ),
                lp.Frame(
                    [
                        LabBlock(
                            [
                                pl.OrderedList([
                                    ['If you have not already created your', xlwings_mono,
                                     'project, go back two slides',
                                     'and follow those steps.'],
                                    ['Edit the .py file to add a function', random_choice_mono, 'which will call',
                                     random_choice_py],
                                    'The function should accept the items to choose from, and the probabilities.',
                                    'Write out a few possible items to choose from in your workbook. Put probabilities next '
                                    'to them.',
                                    ['Call your', random_choice_mono,
                                     'function on these inputs, and see it pick a random item']
                                ])
                            ],
                            title=f'Write a Simple UDF'
                        )
                    ],
                    title=f"Getting your Feet Wet with {xlwings_mono}"
                ),
            ],
            title=f'Writing a First UDF in {xlwings_mono}',
            short_title='UDFs'
        ),
    ]

DOCUMENT_CLASS_KWARGS = dict(
    nav_header=True,
    toc_sections=True
)
OUTPUT_NAME = TITLE

