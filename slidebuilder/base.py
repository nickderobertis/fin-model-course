from typing import List, Optional
from pyexlatex.models.package import Package
from pyexlatex.typing import ItemOrListOfItems
from pyexlatex.models.presentation.presentation import Presentation


class FinancialModelingPresentation(Presentation):
    author = 'Nick DeRobertis'
    short_author = 'DeRobertis'
    institutions = [['University of Florida', 'Department of Finance, Insurance, and Real Estate']]
    short_institution = 'UF'

    def __init__(self, content: ItemOrListOfItems, packages: List[Package] = None,
                 pre_env_contents: Optional[ItemOrListOfItems] = None,
                 title: Optional[str] = None, short_title: Optional[str] = None, subtitle: Optional[str] = None,
                 font_size: Optional[float] = 11, theme: str = 'Madrid', backend: str = 'beamer'):
        super().__init__(
            content,
            packages=packages,
            pre_env_contents=pre_env_contents,
            title=title,
            author=self.author,
            short_title=short_title,
            subtitle=subtitle,
            short_author=self.short_author,
            institutions=self.institutions,
            short_institution=self.short_institution,
            font_size=font_size,
            theme=theme,
            backend=backend
        )