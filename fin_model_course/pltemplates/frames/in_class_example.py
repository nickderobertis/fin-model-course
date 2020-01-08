import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

from pltemplates.blocks import InClassExampleBlock


class InClassExampleFrame(pl.Template):

    def __init__(self, contents, title: str, block_title: str):
        self.block_contents = contents
        self.title = title
        self.block_title = block_title
        self.contents = self._get_contents()
        super().__init__()

    def _get_contents(self):
        return lp.Frame(
            [
                InClassExampleBlock(
                    [
                        pl.UnorderedList(self.block_contents)
                    ],
                    title=self.block_title
                )
            ],
            title=self.title
        )