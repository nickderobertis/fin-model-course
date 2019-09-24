from typing import Sequence
import pyexlatex as pl


class EquationWithVariableDefinitions(pl.Template):

    def __init__(self, equation: str, definitions: Sequence, space_adjustment: float = -0.3):
        self.equation_str = equation
        self.definitions = definitions
        self.space_adjustment = space_adjustment
        self.contents = self._get_contents()
        super().__init__()

    def _get_contents(self):
        return [
            pl.Equation(str_eq=self.equation_str, inline=False),
            pl.VSpace(self.space_adjustment),
            pl.UnorderedList(self.definitions)
        ]