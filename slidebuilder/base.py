from typing import List, Optional
from pyexlatex.typing import ItemOrListOfItems
from pyexlatex.presentation import Presentation


class FinancialModelingPresentation(Presentation):
    author = 'Nick DeRobertis'
    short_author = 'DeRobertis'
    institutions = [['University of Florida', 'Department of Finance, Insurance, and Real Estate']]
    short_institution = 'UF'

    def __init__(self, content: ItemOrListOfItems,
                 title: Optional[str] = None, short_title: Optional[str] = None, subtitle: Optional[str] = None,
                 **presentation_kwargs):
        super().__init__(
            content,
            title=title,
            author=self.author,
            short_title=short_title,
            subtitle=subtitle,
            short_author=self.short_author,
            institutions=self.institutions,
            short_institution=self.short_institution,
            **presentation_kwargs
        )