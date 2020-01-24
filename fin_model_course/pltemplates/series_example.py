import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

from plbuild.paths import images_path


def get_series_example_frames():
    pd_mono = pl.Monospace('pandas')
    series_mono = pl.Monospace('Series')
    df_mono = pl.Monospace('DataFrame')

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
    return [
        lp.DimRevealListFrame(
            [
                ['A', series_mono, 'is the other main', pd_mono, 'data type besides a', df_mono],
                ['A single column or row of a', df_mono, 'is a', series_mono],
                ['A', series_mono, 'has a name, an index, and one value per index']
            ],
            title=f'What is a {series_mono}?'
        ),
        lp.Frame(
            [
                lp.Block(
                    [
                        series_ex_1,
                        pl.Graphic(images_path('series-example-df.png'), width=0.2),
                        series_ex_2
                    ],
                    title=f'{series_mono} Example'
                )
            ],
            title=f"{df_mono}s are Made up of {series_mono}'"
        ),
        lp.Frame(
            [
                lp.Block(
                    [
                        pl.TextSize(-1),
                        series_ex_3,
                    ],
                    title=f'Working with {series_mono} Example'
                )
            ],
            title=f"Access {series_mono} Values Just Like {df_mono} Columns"
        )
    ]