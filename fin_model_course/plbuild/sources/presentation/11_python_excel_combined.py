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
from pltemplates.blocks import LabBlock, InClassExampleBlock
from pltemplates.eq_with_variable_defs import EquationWithVariableDefinitions
from pltemplates.hyperlink import Hyperlink
from pltemplates.exercises.read_write_excel_pandas import (
    get_lab_exercise
)
from pltemplates.exercises.intro_udf import get_lab_exercise as get_intro_udf_exercise
from pltemplates.exercises.advanced_udf import get_lab_exercise as get_advanced_udf_exercise

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
    df_mono = pl.Monospace('DataFrame')
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
    xw_arg_decorator = pl.Monospace('@xw.arg')
    xw_ret_decorator = pl.Monospace('@xw.ret')
    x_mono = pl.Monospace('x')
    expand_table_mono = pl.Monospace("expand='table'")
    random_choice_mono = pl.Monospace('random_choice')
    random_choice_py = pl.Monospace('random.choices')

    pd_read_write_exercise = get_lab_exercise()
    intro_udf_exercise = get_intro_udf_exercise()
    advanced_udf_exercise = get_advanced_udf_exercise()

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
                lp.Frame(
                    [
                        InClassExampleBlock(
                            [
                                pl.UnorderedList([
                                    'Download the contents of the "Read Write Excel Pandas" folder in Examples',
                                    'Ensure that you put the Excel file and notebook in the same folder for it to work',
                                    'Follow along with the notebook'
                                ])
                            ],
                            title=f'Read and Write to Excel using {pd_mono}'
                        )
                    ],
                    title='Showcasing Reading and Writing to Excel Files'
                ),
                pd_read_write_exercise.presentation_frames(),
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
                                    'Hit the Windows key, type anaconda. Launch the Anaconda Prompt.',
                                    ['In the Anaconda Prompt, type', addin_install_mono],
                                    ['After a bit, you should see', addin_install_success],
                                    'Launch Excel and ensure that you now see an xlwings tab',
                                    ['Download', random_seed_py, 'and', random_seed_excel, 'from Canvas in the folder',
                                     'Examples > Random Seed. Put them both in the same folder.'],
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
                        InClassExampleBlock(
                            [
                                pl.UnorderedList(
                                    [
                                        'I will now complete the steps from the previous slides.',
                                        'There is also an example of this process on Canvas in Examples -> '
                                        'xlwings UDFs -> First xlwings Project.ipynb',
                                        'If you get lost along the way, just follow the steps on the prior slides',
                                        'I will go through creating a project, and implementing the functions in '
                                        'the random seed example from Canvas.'
                                    ]
                                ),
                            ],
                            title=f'Starting an {xlwings_mono} Project'
                        )
                    ],
                    title=f'Example for Creating an {xlwings_mono} Project'
                ),
                intro_udf_exercise.presentation_frames(),
            ],
            title=f'Writing a First UDF in {xlwings_mono}',
            short_title='UDFs'
        ),
        pl.Section(
            [
                lp.DimRevealListFrame(
                    [
                        "Now that we know how to write a UDF, let's explore some interesting additional power it adds "
                        "to Excel",
                        'Recall creating the project 1 model. We had to build as many rows for as many years we want '
                        'to support in the model.',
                        'What if the number of rows, columns, etc. in our model was dynamic, i.e. changing an input '
                        'changes the shape of the output?',
                        'Further, if we have input data coming into our model with different dimensions, that can be '
                        'a challenge as well.'
                    ],
                    title='Motivating Advanced UDFs'
                ),
                lp.Frame(
                    [
                        pl.TextSize(-2),
                        pl.UnorderedList([
                            lp.DimAndRevealListItems([
                                ['We can even work with', pd_mono, dfs_mono, 'when going back and forth between Excel '
                                 'and Python with UDFs.', 'To do this, we just need to control how data is transferred',
                                 'between Excel and Python with', xw_ret_decorator, 'and', xw_arg_decorator],
                            ], dim_last_item=True)
                        ]),
                        pl.VSpace(-0.1),
                        lp.Block(
                            [
                                pl.Python("@xw.arg('x', pd.DataFrame, expand='table')"),
                                pl.VSpace(-0.3),
                                pl.UnorderedList([
                                    ['This means that argument', x_mono, 'will come into the function as a', df_mono],
                                    ['The', expand_table_mono, 'portion means that a single cell can be selected as',
                                     'an input, and it will expand the selection right and down until it hits blank',
                                     'cells.'],
                                    ['This', expand_table_mono, 'allows you to accept inputs of any size without',
                                     'knowing their size in advance.']
                                ])

                            ],
                            title=f"{xw_arg_decorator}: Modifying What's Coming Into Python from Excel",
                            overlay=next_slide,
                        ),
                        lp.Block(
                            [
                                pl.Python("@xw.ret(index=False, header=False)"),
                                pl.VSpace(-0.3),
                                pl.UnorderedList([
                                    ['This means that the', df_mono, 'returned from the function will have its',
                                     'index and header stripped away before outputting to Excel']
                                ])
                            ],
                            title=f"{xw_ret_decorator}: Modifying What's Coming Into Excel from Python",
                            overlay=next_slide,
                        ),
                    ],
                    title=f'Using {pd_mono} with {xlwings_mono}'
                ),
                lp.Frame(
                    [
                        InClassExampleBlock(
                            [
                                pl.UnorderedList(
                                    [
                                        'Now I will show how to implement Array and Dynamic UDFs',
                                        'Download the Dynamic UDFs example files from the Examples folder',
                                        'Also download the random_seed example if you have not already',
                                        'We will go through both examples.'
                                    ]
                                )
                            ],
                            title=f'Implementing Array and Dynamic UDFs'
                        ),
                    ],
                    title='Example for Advanced UDFs',
                ),
                advanced_udf_exercise.presentation_frames(),
            ],
            title=f'Array and Dynamic UDFs in {xlwings_mono}',
            short_title='Advanced UDFs'
        ),

        lp.Appendix(
            [
                pd_read_write_exercise.appendix_frames(),
                intro_udf_exercise.appendix_frames(),
                advanced_udf_exercise.appendix_frames(),
            ]
        )
    ]

DOCUMENT_CLASS_KWARGS = dict(
    nav_header=True,
    toc_sections=True
)
OUTPUT_NAME = TITLE

