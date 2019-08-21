from pyexlatex.models.presentation.beamer.block import Block


class LabBlock(Block):

    def __init__(self, content, **kwargs):
        super().__init__(content, header_color='violet', **kwargs)
