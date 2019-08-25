from typing import Optional
from pyexlatex.models.format.textcolor import TextColor
from pyexlatex.models.format.underline import Underline
from pyexlatex.models.hyperlinks import Hyperlink as PlHyperlink
from pyexlatex.models.package import Package


class Hyperlink(PlHyperlink):

    def __init__(self, href: str, content: Optional = None, **kwargs):
        super().__init__(href, content, **kwargs)
        self.init_data()
        self.data.packages.append(Package('xcolor'))

    def __str__(self):
        base_str = super().__str__()
        return str(
            TextColor(Underline(base_str), 'blue')
        )
