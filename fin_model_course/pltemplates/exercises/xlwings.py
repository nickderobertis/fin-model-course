import pyexlatex as pl

from pltemplates.exercises.lab_exercise import LabExercise


def get_xlwings_exercise() -> LabExercise:
    xlwings_mono = pl.Monospace('xlwings')
    bullet_contents = [
        [
            ['For all of the', xlwings_mono, 'lab exercises, work with "xlwings Lab.xlsx".'],
            ['Use', xlwings_mono, 'to read the values in the column A and then write them beside',
             'the initial values in column B']
        ],
        [
            'Get the value in C9 and multiply it by 2.5 in Python',
        ],
        [
            'Read the table which starts in E4 into Python. Multiply the prices by 2.5, and then output '
            'back into Excel starting in cell H5.',
            'Ensure that the outputted table appears in the same format as the original (pay attention to '
            'index and header)'
        ],
        [
            'In column L, write 5, 10, 15 ... 100 spaced two cells apart, so L1 would have 5, L4 would have 10, '
            'and so on.'
        ]

    ]
    return LabExercise(
        bullet_contents,
        'Dynamically Reading and Writing to Excel',
        f"Reading and Writing to Excel with {xlwings_mono}",
        label='lab:xlwings'
    )
