from typing import List

import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll


def get_wacc_graphics():

    equal_graphic = EquityDebtWACCGraphicForHalfAndHalf(
        0.16,
        0.08,
        0.5,
        0.5,
        0.35
    )

    seventy_five_percent_equity_graphic = EquityDebtWACCGraphicForSeventyFivePercentEquity(
        0.16,
        0.08,
        0.75,
        0.25,
        0.35
    )

    return [
        equal_graphic,
        seventy_five_percent_equity_graphic
    ]

# TODO [#15]: this whole thing is a mess. Tried to make one reusable class for creating this graphic, but was having issues
# TODO [#16]: actually getting it to work. It seems the graphics sizes are not working as expected. Therefore I made a
# TODO [#17]: separate class for each version of the graphic, with some values hard-coded, and these classes are not
# TODO [#18]: reusable at all.

class EquityDebtWACCGraphicForSeventyFivePercentEquity(pl.Template):

    def __init__(self, cost_of_equity: float, cost_of_debt: float, weight_of_equity: float, weight_of_debt: float, tax_rate: float):
        self.cost_of_equity = cost_of_equity
        self.cost_of_debt = cost_of_debt
        self.weight_of_equity = weight_of_equity
        self.weight_of_debt = weight_of_debt
        self.tax_rate = tax_rate
        self.contents = self._get_contents()
        super().__init__()

    @property
    def wacc(self):
        return self.cost_of_equity * self.weight_of_equity + self.after_tax_cost_of_debt * self.weight_of_debt

    @property
    def after_tax_cost_of_debt(self):
        return self.cost_of_debt * (1 - self.tax_rate)

    def _get_contents(self):
        all_node_options = [
            'every text node part/.style={align=center}'
        ]

        debt_options = all_node_options + [
            'fill=blue'
        ]

        debt_text_options = all_node_options + [
            'text=white'
        ]

        equity_options = all_node_options + [
            'fill=orange'
        ]

        wacc_options = all_node_options + [
            'fill=violet!80'
        ]

        debt_equity_width = 3

        total_height = 4
        debt_height = self.weight_of_debt * total_height
        equity_height = self.weight_of_equity * total_height

        debt_contents = [
            'Debt',
            pl.OutputLineBreak(),
            f'Pre-tax: {self.cost_of_debt:.2%}',
            pl.OutputLineBreak(),
            f'After: {self.after_tax_cost_of_debt:.2%}',
        ]

        equity_contents = [
            'Equity',
            pl.OutputLineBreak(),
            f'{self.cost_of_equity:.2%}'
        ]

        wacc_contents = ['WACC', pl.OutputLineBreak(), f'{self.wacc:.2%}']

        debt_rect = lg.Rectangle(debt_equity_width, debt_height, debt_contents, shape_options=debt_options, text_options=debt_text_options)
        equity_rect = lg.Rectangle(debt_equity_width, equity_height, equity_contents, offset=(0, 2.15), shape_options=equity_options)
        wacc_rect = lg.Rectangle(2, 4.3, wacc_contents, offset=(3, 1.5), shape_options=wacc_options)


        contents = lg.TikZPicture(
            [
                pl.TextSize(-1),
                debt_rect,
                equity_rect,
                wacc_rect,
                lg.Arrow(debt_rect, wacc_rect),
                lg.Arrow(equity_rect, wacc_rect)
            ]
        )

        return contents


class EquityDebtWACCGraphicForHalfAndHalf(pl.Template):

    def __init__(self, cost_of_equity: float, cost_of_debt: float, weight_of_equity: float, weight_of_debt: float,
                 tax_rate: float):
        self.cost_of_equity = cost_of_equity
        self.cost_of_debt = cost_of_debt
        self.weight_of_equity = weight_of_equity
        self.weight_of_debt = weight_of_debt
        self.tax_rate = tax_rate
        self.contents = self._get_contents()
        super().__init__()

    @property
    def wacc(self):
        return self.cost_of_equity * self.weight_of_equity + self.after_tax_cost_of_debt * self.weight_of_debt

    @property
    def after_tax_cost_of_debt(self):
        return self.cost_of_debt * (1 - self.tax_rate)

    def _get_contents(self):
        all_node_options = [
            'every text node part/.style={align=center}'
        ]

        debt_options = all_node_options + [
            'fill=blue'
        ]

        debt_text_options = all_node_options + [
            'text=white'
        ]

        equity_options = all_node_options + [
            'fill=orange'
        ]

        wacc_options = all_node_options + [
            'fill=violet!80'
        ]

        debt_equity_width = 3

        total_height = 4
        debt_height = self.weight_of_debt * total_height
        equity_height = self.weight_of_equity * total_height

        debt_contents = [
            'Debt',
            pl.OutputLineBreak(),
            f'Pre-tax: {self.cost_of_debt:.2%}',
            pl.OutputLineBreak(),
            f'After: {self.after_tax_cost_of_debt:.2%}',
        ]

        equity_contents = [
            'Equity',
            pl.OutputLineBreak(),
            f'{self.cost_of_equity:.2%}'
        ]

        wacc_contents = ['WACC', pl.OutputLineBreak(), f'{self.wacc:.2%}']

        debt_rect = lg.Rectangle(debt_equity_width, debt_height, debt_contents, shape_options=debt_options,
                                 text_options=debt_text_options)
        equity_rect = lg.Rectangle(debt_equity_width, equity_height, equity_contents, offset=(0, debt_height),
                                   shape_options=equity_options)
        wacc_rect = lg.Rectangle(2, total_height, wacc_contents, offset=(3, 1), shape_options=wacc_options)

        contents = lg.TikZPicture(
            [
                debt_rect,
                equity_rect,
                wacc_rect,
                lg.Arrow(debt_rect, wacc_rect),
                lg.Arrow(equity_rect, wacc_rect)
            ]
        )

        return contents