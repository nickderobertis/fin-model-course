import pyexlatex.presentation as lp


class LabBlock(lp.Block):

    def __init__(self, content, **kwargs):
        super().__init__(content, header_color='violet', **kwargs)
