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
from pltemplates.blocks import LabBlock
from pltemplates.frames.tvm.project_1_lab import get_project_1_lab_frame
from models.retirement import RetirementModel

pd_mono = pl.Monospace('pandas')

AUTHORS = ['Nick DeRobertis']
SHORT_TITLE = 'Visualization'
SUBTITLE = f'An Introduction to Visualization and {pd_mono}'

SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [
    ['University of Florida', 'Department of Finance, Insurance, and Real Estate'],
]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = plbuild.paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = plbuild.paths.HANDOUTS_BUILD_PATH
TITLE = 'Understanding Complex Results'
ORDER = 7


def get_content():
    ret_model = RetirementModel()
    ret_df = ret_model.get_formatted_df(num_years=12)
    ret_table = lt.Tabular.from_df(ret_df, extra_header=pl.Bold('Retirement Info'))
    plt_mono = pl.Monospace('matplotlib')
    df_mono = pl.Monospace('DataFrame')
    df_basic_example = pl.Python(
"""
>>> import pandas as pd
>>> df = pd.DataFrame()
>>> df['Sales'] = [1052, 212, 346]
>>> df['Category'] = ['Aprons', 'Apples', 'Bowties']
df
"""
    )
    plot_example_code = pl.Python(
"""
>>> %matplotlib inline
>>> ret_df.plot.line(x='Time', y='Salaries')
"""
    )

    return [
        get_project_1_lab_frame(),
        lp.DimRevealListFrame(
            [
                "So far we've had one main output from our model, number of years",
                "Salaries and wealth over time have also been outputs, but we haven't had a good way of understanding "
                "that output. It's a bunch of numbers.",
                "This is where visualization comes in. We have some complex result, and want to make it easily "
                "interpretable."
            ],
            title='Why Visualize?'
        ),
        lp.Frame(
            [
                pl.Center(ret_table)
            ],
            title='What we Have so Far'
        ),
        lp.GraphicFrame(
            images_path('excel-insert-chart.png'),
            title='Visualization in Excel'
        ),
        lp.GraphicFrame(
            lg.ModifiedPicture(
                images_path('python-visualization-landscape.jpg'),
                [
                    lg.Path('draw', [(0.52, 0.52), (0.85, 0.67)], options=['red'], draw_type='rectangle',
                            overlay=lp.Overlay([2]))
                ]
            ),
            title='An Overwhelming Number of Options in Python'
        ),
        lp.DimRevealListFrame(
            [
                ["Ultimately, we will be creating graphs using", plt_mono, "but we won't use it directly."],
                ["Instead, we will use", pd_mono],
                [pd_mono, "is actually creating its graphs using", plt_mono, "for us, but it is simpler to use."]
            ],
            title='Explaining Python Visualization in This Class'
        ),
        lp.DimRevealListFrame(
            [
                [pd_mono, "does", pl.Bold('a lot'), 'more than just graphing. We will use it throughout the '
                                                    'rest of the class.'],
                "Previously we've worked with lists, numbers, strings, and even our custom types (our model classes)",
                [pd_mono, "provides the", df_mono, "as a new type that we can use."],
                f'Before we can get to graphing, we must learn how to use the {df_mono}.'

            ],
            title='Some Setup Before we can Visualize in Python'
        ),
        lp.Frame(
            [
                ['A', df_mono, 'is essentially a table. It has rows and columns, just like in Excel.'],
                pl.VFill(),
                lp.Block(
                    [
                        pl.UnorderedList([
                            'Add or remove columns or rows',
                            'Group by and aggregate',
                            'Load in and output data from/to Excel and many other formats',
                            'Merge and join data sets',
                            'Reshape and pivot data',
                            'Time-series functionality',
                            'Slice and query your data',
                            'Handle duplicates and missing data'
                        ])
                    ],
                    title=f'Some Features of the {df_mono}'
                )

            ],
            title=f'What is a {df_mono}?'
        ),
        lp.Frame(
            [
                df_basic_example,
                pl.Graphic(images_path('df-basic-example.png'), width=0.3)

            ],
            title=f'A Basic {df_mono} Example'
        ),
        lp.Frame(
            [
                lp.Block(
                    [
                        plot_example_code,
                        pl.Graphic(images_path('python-salaries-line-graph.pdf'), width=0.5)
                    ],
                    title=f'Line Graphs using {pd_mono}'
                )
            ],
            title='A Minimal Plotting Example'
        ),
        lp.MultiGraphicFrame(
            [
                images_path('excel-salaries-line-graph.png'),
                images_path('python-salaries-line-graph.pdf'),
            ],
            vertical=False,
            title='Basic Graph Types: Line Graphs'
        ),
        lp.MultiGraphicFrame(
            [
                images_path('excel-salaries-bar-graph.png'),
                images_path('python-salaries-bar-graph.pdf'),
            ],
            vertical=False,
            title='Basic Graph Types: Bar Graphs'
        ),
        lp.MultiGraphicFrame(
            [
                images_path('excel-salaries-box-whisker-plot.png'),
                images_path('python-salaries-box-graph.pdf'),
            ],
            vertical=False,
            title='Basic Graph Types: Box and Whisker Plots'
        )
    ]


DOCUMENT_CLASS_KWARGS = {}
OUTPUT_NAME = TITLE