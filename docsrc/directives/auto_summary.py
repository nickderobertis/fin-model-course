from sphinx.ext.autosummary import Autosummary
from typing import List, Tuple


class AutoSummaryNameOnly(Autosummary):

    def get_table(self, items: List[Tuple[str, str, str, str]]):
        new_items = []
        for name, sig, summary, real_name in items:
            name_parts = name.split('.')
            new_name = name_parts[-1]
            new_items.append((new_name, sig, summary, real_name))
        return super().get_table(new_items)
