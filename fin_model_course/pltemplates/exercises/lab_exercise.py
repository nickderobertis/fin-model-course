from copy import deepcopy
from enum import Enum
from typing import Sequence, Optional, List

import more_itertools
import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

from pltemplates.frames.lab import LabFrame
from pltemplates.hyperlink import Hyperlink


class LabFrameTypes(str, Enum):
    QUESTION = 'question'
    ANSWERS = 'answers'
    RESOURCES = 'resources'


class LabExercise(pl.Template):
    """
    Creates collection of related lab frames
    """

    def __init__(self, all_bullet_content: Sequence[Sequence], block_title: str, frame_title: str, label: str,
                 answers_content: Optional[Sequence[Sequence]] = None,
                 resources: Optional[Sequence[Hyperlink]] = None):
        self.all_bullet_content = all_bullet_content
        self.resources = resources

        if answers_content is None:
            answers_content = []
        self.answers_content = answers_content

        self.block_title = block_title
        self.frame_title = frame_title
        self.label = label
        self.contents = self._get_content()
        super().__init__()

    def presentation_frames(self):
        return self.contents[0]

    def appendix_frames(self):
        return self.contents[1:]

    @property
    def has_multiple_exercises(self) -> bool:
        return len(self.all_bullet_content) > 1

    def _get_content(self):
        question_refs = self._get_question_references()
        answer_refs = self._get_answers_references()
        resource_refs = self._get_resource_references()
        refs_for_resource_frame = self._get_references_for_resources()

        all_content = []
        # Handle exercise slides
        for i, bullet_content in enumerate(self.all_bullet_content):
            refs = deepcopy(question_refs)
            refs.pop(i)  # remove reference to this item
            # Add answer ref specifically for this item
            if answer_refs and answer_refs[i] is not None:
                refs.append(answer_refs[i])
            refs.extend(resource_refs)
            disp_idx = i + 1
            level_str = f', Level {disp_idx}'
            block_title = self.block_title
            frame_title = self.frame_title
            if self.has_multiple_exercises:
                block_title += level_str
                frame_title += level_str
            label = self._get_label_for(i)
            lab_frame = LabFrame(bullet_content, block_title, frame_title, bottom_content=refs, label=label)
            all_content.append(lab_frame)
        # Handle answer slides
        for i, bullet_content in enumerate(self.answers_content):
            if not bullet_content:
                continue
            refs = deepcopy(question_refs)
            refs.extend(resource_refs)
            disp_idx = i + 1
            add_str = ', Answers'
            if self.has_multiple_exercises:
                add_str += f' for Level {disp_idx}'
            block_title = self.block_title + add_str
            frame_title = self.frame_title + add_str
            label = self._get_label_for(i, frame_type=LabFrameTypes.ANSWERS)
            lab_frame = LabFrame(bullet_content, block_title, frame_title, bottom_content=refs, label=label, color='orange')
            all_content.append(lab_frame)
        # Add references slide
        if self.resources:
            block_title = self.block_title + ' Resources'
            frame_title = self.frame_title + ' Resources'
            label = self._get_label_for(0, frame_type=LabFrameTypes.RESOURCES)
            resource_chunks = list(more_itertools.chunked(self.resources, 10))
            if len(resource_chunks) > 1:
                # Multiple slides
                num_slides = len(resource_chunks)
                for i, resources in enumerate(resource_chunks):
                    count = i + 1
                    slide_position_str = f' ({count}/{num_slides})'
                    label = self._get_label_for(i, frame_type=LabFrameTypes.RESOURCES)
                    bt = block_title + slide_position_str
                    ft = block_title + slide_position_str
                    lab_frame = LabFrame(resources, bt, ft,
                                         bottom_content=refs_for_resource_frame, label=label,
                                         color='teal')
                    all_content.append(lab_frame)

            else:
                # Single slide
                lab_frame = LabFrame(self.resources, block_title, frame_title,
                                     bottom_content=refs_for_resource_frame, label=label,
                                     color='teal')
                all_content.append(lab_frame)
        return all_content

    def _get_question_references(self) -> List[str]:
        refs = []
        # Handle exercise slides
        for i, bullet_content in enumerate(self.all_bullet_content):
            disp_idx = i + 1
            if self.has_multiple_exercises:
                level_str = f'Level {disp_idx}'
            else:
                level_str = 'Exercise'
            label = self._get_label_for(i)
            ref = pl.Ref(label)
            color_ref = f'Slide {pl.TextColor(pl.Underline(ref), "blue")}'
            full_ref = f'{level_str}: {color_ref}'
            refs.append(full_ref)
        return refs

    def _get_answers_references(self) -> List[str]:
        refs = []
        for i, bullet_content in enumerate(self.answers_content):
            if not bullet_content:
                # Didn't get answers for this slide
                refs.append(None)
                continue
            disp_idx = i + 1
            level_str = f'Answers'
            if self.has_multiple_exercises:
                level_str += f' {disp_idx}'
            label = self._get_label_for(i, frame_type=LabFrameTypes.ANSWERS)
            ref = pl.Ref(label)
            color_ref = f'Slide {pl.TextColor(pl.Underline(ref), "blue")}'
            full_ref = f'{level_str}: {color_ref}'
            refs.append(full_ref)
        return refs

    def _get_resource_references(self) -> List[str]:
        refs = []
        if self.resources:
            label = self._get_label_for(0, frame_type=LabFrameTypes.RESOURCES)
            ref = pl.Ref(label)
            level_str = f'Resources'
            color_ref = f'Slide {pl.TextColor(pl.Underline(ref), "blue")}'
            full_ref = f'{level_str}: {color_ref}'
            refs.append(full_ref)
        return refs

    def _get_references_for_resources(self) -> List[str]:
        refs = self._get_question_references()
        for answer_ref in self._get_answers_references():
            if answer_ref is not None:
                refs.append(answer_ref)
        return refs

    def _get_label_for(self, index: int, frame_type: LabFrameTypes = LabFrameTypes.QUESTION):
        disp_idx = index + 1
        label_str = f'-{disp_idx}'
        if frame_type == LabFrameTypes.ANSWERS:
            label_str += '-answers'
        elif frame_type == LabFrameTypes.RESOURCES:
            label_str += '-resources'
        return self.label + label_str
