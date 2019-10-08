from copy import deepcopy
from typing import Sequence

import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

from pltemplates.frames.lab import LabFrame


class LabExercise(pl.Template):
    """
    Creates collection of related lab frames
    """

    def __init__(self, all_bullet_content: Sequence[Sequence], block_title: str, frame_title: str, label: str):
        self.all_bullet_content = all_bullet_content
        self.block_title = block_title
        self.frame_title = frame_title
        self.label = label
        self.contents = self._get_content()
        super().__init__()

    def presentation_frames(self):
        return self.contents[0]

    def appendix_frames(self):
        return self.contents[1:]

    def _get_content(self):
        all_refs = self._get_all_references()
        all_content = []
        for i, bullet_content in enumerate(self.all_bullet_content):
            refs = deepcopy(all_refs)
            refs.pop(i)  # remove reference to this item
            disp_idx = i + 1
            level_str = f', Level {disp_idx}'
            block_title = self.block_title + level_str
            frame_title = self.frame_title + level_str
            label = self._get_label_for(i)
            lab_frame = LabFrame(bullet_content, block_title, frame_title, bottom_content=refs, label=label)
            all_content.append(lab_frame)
        return all_content

    def _get_all_references(self):
        refs = []
        for i, bullet_content in enumerate(self.all_bullet_content):
            disp_idx = i + 1
            level_str = f'Level {disp_idx}'
            label = self._get_label_for(i)
            ref = pl.Ref(label)
            color_ref = f'Slide {pl.TextColor(pl.Underline(ref), "blue")}'
            full_ref = f'{level_str}: {color_ref}'
            refs.append(full_ref)
        return refs

    def _get_label_for(self, index: int):
        disp_idx = index + 1
        label_str = f'-{disp_idx}'
        return self.label + label_str