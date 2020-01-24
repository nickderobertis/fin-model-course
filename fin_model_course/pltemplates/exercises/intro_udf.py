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

    bullet_contents = [
        [
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
        ],
        [
            ['Work off the existing', xlwings_mono, 'project from the Level 1 exercise'],
            ['Now add an additional function', random_choices_mono, 'which will accept the items to',
             'choose from, the probabilities, and the number of random choices to generate.'],
            ['The function should return multiple random choices. In Excel, you should see multiple cells of output,'
             'with each cell containing a random choice.'],
            ['If you return a list from the Python function, it should create this behavior.']
        ]
    ]

    return LabExercise(
        bullet_contents,
        'Write a Simple UDF',
        f"Getting your Feet Wet with {xlwings_mono}",
        label='lab:intro-udf'
    )
