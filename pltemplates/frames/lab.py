from typing import Sequence, Optional

import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

from pltemplates.blocks import LabBlock


class LabFrame(pl.Template):

    def __init__(self, bullet_content: Sequence, block_title: str, frame_title: str,
                 bottom_content: Optional[Sequence] = None, label: Optional[str] = None):
        self.bullet_content = bullet_content
        self.block_title = block_title
        self.frame_title = frame_title
        self.bottom_content = bottom_content
        self.label = label
        self.contents = self._get_contents()
        super().__init__()

    def _get_contents(self):
        return lp.Frame(
            [
                LabBlock(
                    [
                        pl.OrderedList(self.bullet_content)
                    ],
                    bottom_content=self.bottom_content,
                    title=self.block_title,
                )
            ],
            title=self.frame_title,
            label=self.label
        ),