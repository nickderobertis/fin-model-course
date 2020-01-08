from typing import Sequence, Union

from pyexlatex import VSpace
from pyexlatex.presentation import (
    Overlay,
    NextWithIncrement,
    UntilEnd,
    Frame,
    Block,
    adjust_to_full_size_and_center,
)
from pyexlatex.graphics import (
    TikZPicture,
    Node,
    LinearFlowchart,
)


all_node_style = [
    'rounded corners',
    'inner sep=10pt'
]

in_out_style = [
    'fill=orange!30',
] + all_node_style
real_world_style = [
    'fill=blue!30',
] + all_node_style
model_style = [
    'fill=green!40',
]

next_until_end_ov = Overlay([UntilEnd(NextWithIncrement())])


class ModelFlowchartFrame(Frame):
    node_styles = [in_out_style, real_world_style, model_style]

    def __init__(self, content: Sequence[Sequence[Union[str, Node]]],
                 block_titles: Sequence[str] = ('A General Structure', 'Real-world Problem', 'A Model of the Problem'),
                 **kwargs):
        content =  [[
            'Inputs',
            'Process',
            'Outputs'
        ]] + list(content)
        self.content = content
        self.titles = block_titles
        self._validate()
        self.content = self._get_contents(content)
        super().__init__(self.content, **kwargs)

    def _get_contents(self, content):
        out_contents = []
        for i, content_list in enumerate(content):
            out_contents.append(VSpace(-0.25))
            out_contents.append(
                Block(
                    adjust_to_full_size_and_center(
                        TikZPicture(
                            LinearFlowchart(content_list, node_options=self.node_styles[i])
                        )
                    ),
                    title=self.titles[i],
                    overlay=next_until_end_ov
                )
            )

        return out_contents

    def _validate(self):
        assert len(self.content) == len(self.titles) == 3

