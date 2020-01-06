from typing import Optional

import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll


class SingleBlockDimRevealListFrame(pl.Template):

    def __init__(self, contents, block_contents, title: Optional[str] = None, block_title: Optional[str] = None,
                 **kwargs):
        self.main_contents = contents
        self.block_contents = block_contents
        self.title = title
        self.block_title = block_title
        self.kwargs = kwargs
        self.contents = self._get_contents()
        super().__init__()

    def _get_contents(self):
        return lp.Frame(
            [
                lp.Block(self.block_contents, title=self.block_title),
                pl.VFill(),
                pl.UnorderedList([
                    lp.DimAndRevealListItems(
                        self.main_contents,
                        vertical_fill=True,
                    )
                ])
            ],
            title=self.title,
            **self.kwargs
        )