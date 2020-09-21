import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

import plbuild
from lectures.combining_excel_python.main import get_combining_excel_python_lecture
from lectures.lab_exercises.notes import get_read_write_excel_pandas_lab_lecture, get_read_write_xlwings_lab_lecture
from plbuild.paths import images_path
from pltemplates.exercises.xlwings import get_xlwings_exercise
from pltemplates.frames.in_class_example import InClassExampleFrame
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
from schedule.main import LECTURE_9_NAME

xlwings_mono = pl.Monospace('xlwings')

AUTHORS = ['Nick DeRobertis']
SHORT_TITLE = 'Combining Tools'
SUBTITLE = f'Using {xlwings_mono} to Run Excel from Python'

SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [
    ['University of Florida', 'Department of Finance, Insurance, and Real Estate'],
]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = plbuild.paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = plbuild.paths.HANDOUTS_BUILD_PATH
TITLE = LECTURE_9_NAME
ORDER = 'S9'


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

    lecture = get_combining_excel_python_lecture()
    pd_read_write_exercise = get_read_write_excel_pandas_lab_lecture().to_pyexlatex()
    xlwings_exercise = get_read_write_xlwings_lab_lecture().to_pyexlatex()

    read_from_excel_example = pl.Python("""
my_value = sht.range("G11").value  # single value
# all values in cell range
my_value = sht.range("G11:F13").value  
# expands cell range down and right getting all values
my_values = sht.range("G11").expand().value  
""")

    write_to_excel_example = pl.Python("""
sht.range("G11").value = 10
sht.range("G11").value = [10, 11]  # horizontal
sht.range("G11:G12").value = [10, 11]  # vertical
# table, DataFrame from elsewhere
sht.range("G11").value = df  
""")

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
                        'We will focus on manipulating Excel from Python in this class. I encourage you to explore '
                        'the other two approaches on your own.'
                    ],
                    title=f'What are the Main Ways to use {xlwings_mono}?'
                ),
                lp.TwoColumnGraphicDimRevealFrame(
                    [
                        pl.TextSize(-1),
                        [xlwings_mono,
                         'allows us to write Python values into Excel and fetch Excel values into Python'],
                        'There is also a complete VBA API, meaning you can do everything that you could do with VBA '
                        'from within Python, which means you have the full capabilities of Excel within Python',
                        'There are also convenient features to work with entire tables at once rather than '
                        'a single value'
                    ],
                    graphics=[
                        images_path('python-excel-logo.png')
                    ],
                    title='Using Python to Drive Excel Models'
                ),
                lp.Frame(
                    [
                        lp.Block(
                            [
                                read_from_excel_example
                            ],
                            title='Read Values from Excel'
                        ),
                        lp.Block(
                            [
                                write_to_excel_example
                            ],
                            title='Write Values to Excel'
                        )
                    ],
                    title='Write and Read Values to and from Excel'
                ),
                InClassExampleFrame(
                    [
                        'Download the contents of the "xlwings" folder in Examples',
                        'Ensure that you put the Excel file and notebook in the same folder for it to work',
                        'Follow along with the notebook'
                    ],
                    title=f'How to Use {xlwings_mono}',
                    block_title=f'Trying out {xlwings_mono}'
                ),
                xlwings_exercise.presentation_frames(),
            ],
            title=f'Introducing Full Python-Excel Connection with {xlwings_mono}',
            short_title=f'{xlwings_mono}'
        ),

        pl.PresentationAppendix(
            [
                lecture.pyexlatex_resources_frame,
                pd_read_write_exercise.appendix_frames(),
                xlwings_exercise.appendix_frames(),
            ]
        )
    ]

DOCUMENT_CLASS_KWARGS = dict(
    nav_header=True,
    toc_sections=True
)
OUTPUT_NAME = TITLE

