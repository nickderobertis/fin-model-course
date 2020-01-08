import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

from pltemplates.blocks import LabBlock
from pltemplates.exercises.lab_exercise import LabExercise


def get_lab_exercise() -> LabExercise:
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
    random_choices_mono = pl.Monospace('random_choices')
    random_choice_py = pl.Monospace('random.choices')
    xlwings_mono = pl.Monospace('xlwings')
    df_returns_example = pl.Monospace("df['Stock Price'].pct_change()")

    bullet_contents = [
        [
            ['In your', xlwings_mono, 'Python file, add a function which will generate 1, 2, ... N in a column for',
             'whatever N is passed.'],
            ['Add a cell in your wookbook containing the number of rows to be generated, and call your UDF in',
             'another cell.'],
            ['Change the number of rows to be generated and see the number of rows in the output change.']

        ],
        [
            ['In your', xlwings_mono, 'project workbook, add a column Stock Price which has five prices below it,',
             '100, 110, 115, 108, and 105.'],
            ['In the Python file, write a UDF, which accepts the top-left cell of this table (the one',
             'with Stock Price), and returns the stock returns.'],
            ['Call this UDF next to the stock price column so that you have the return from last period to this one',
             'next to the stock prices.'],
            ['You may find', df_returns_example, 'useful for this purpose.'],
            ['Answers should be 10%, 4.5%, -6%, -2.8%']
        ]
    ]

    return LabExercise(
        bullet_contents,
        'Advanced UDFs',
        f"Dynamic and Array UDFs with {xlwings_mono}",
        label='lab:dynamic-array-udf'
    )
