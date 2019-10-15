import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

from pltemplates.blocks import LabBlock
from pltemplates.exercises.lab_exercise import LabExercise


def get_lab_exercise() -> LabExercise:
    pd_mono = pl.Monospace('pandas')
    to_excel_mono = pl.Monospace('to_excel')
    bullet_contents = [
        [
            'Download "MSFT Financials.xls" from Canvas in Lab Exercises -> Read Write Excel Pandas',
            'Read the sheet "Income Statement" into a DataFrame',
            'Write the DataFrame to a new workbook, "My Data.xlsx", with the sheet '
            'name "Income Statement"'
        ],
        [
            ['Use the same "MSFT Financials.xls" from the first exercise on Slide',
             pl.Ref('lab:read-write-excel-pandas-1')],
            'Output to five separate workbooks, named "My Data1.xlsx", "My Data2.xlsx", and so on.',
            ['Do this', pl.Underline('without'), 'writing the', to_excel_mono, 'command multiple times']
        ],
        [
            'Note: this exercise uses the Advanced material covered in Examples -> Read Write Excel Pandas',
            ['Use the same "MSFT Financials.xls" from the first exercise on Slide',
             pl.Ref('lab:read-write-excel-pandas-1')],
            'Output to five separate sheets in the same workbook "My Data.xlsx". The sheets should '
            'be named "Income Statement 1", "Income Statement 2", and so on.',
            ['Do this', pl.Underline('without'), 'writing the', to_excel_mono, 'command multiple times']
        ]

    ]
    return LabExercise(
        bullet_contents,
        'Reading and Writing to Excel',
        f"Reading and Writing to Excel with {pd_mono}",
        label='lab:read-write-excel-pandas'
    )
