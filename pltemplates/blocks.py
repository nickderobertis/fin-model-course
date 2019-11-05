from typing import Optional

import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll


class _LabBlock(lp.Block):

    def __init__(self, content, color: str = 'violet', **kwargs):
        super().__init__(content, header_color=color, **kwargs)


class LabBlock(pl.Template):

    def __init__(self, content, bottom_content: Optional = None, **kwargs):
        if not isinstance(content, (list, tuple)):
            content = [content]
        if bottom_content is None:
            bottom_content = []
        if not isinstance(bottom_content, (list, tuple)):
            bottom_content = [bottom_content]
        self.content = content
        self.bottom_content = bottom_content
        self.kwargs = kwargs
        self.contents = self._get_contents()
        super().__init__()

    def _get_contents(self):
        contents = [
            *self.content,
            pl.VFill(),
        ]
        if self.bottom_content:
            align = 'c' * len(self.all_bottom_contents)
            tab = lt.TabularStar(
                [
                    lt.TopRule(),
                    lt.ValuesTable.from_list_of_lists([self.all_bottom_contents])
                ],
                align=align
            )
            tab = self.format_contents(tab)
            contents.append(tab)
        lb = _LabBlock(
            contents,
            **self.kwargs
        )
        return lb

    @property
    def all_bottom_contents(self):
        if not self.bottom_content:
            return []
        contents = [
            pl.HFill(),
            *self.bottom_content,
            pl.HFill()
        ]
        return self.format_contents(contents)


class InClassExampleBlock(lp.Block):

    def __init__(self, content, **kwargs):
        green = pl.RGB(31, 156, 17, color_name='darkgreen')
        self.init_data()
        self.data.packages.append(green)
        super().__init__(content, header_color='darkgreen', **kwargs)
