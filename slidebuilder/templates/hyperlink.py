from typing import Optional
import pyexlatex as pl


class Hyperlink(pl.Hyperlink):

    def __init__(self, href: str, content: Optional = None, **kwargs):
        super().__init__(href, content, **kwargs)
        self.init_data()
        self.data.packages.append(pl.Package('xcolor'))

    def __str__(self):
        base_str = super().__str__()
        return str(
            pl.TextColor(pl.Underline(base_str), 'blue')
        )
