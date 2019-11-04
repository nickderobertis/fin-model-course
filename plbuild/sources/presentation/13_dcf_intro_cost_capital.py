import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

import plbuild
from plbuild.paths import images_path
from pltemplates.frames.model_flowchart import (
    ModelFlowchartFrame,
    real_world_style,
    model_style,
    in_out_style
)
from pltemplates.blocks import LabBlock, InClassExampleBlock
from pltemplates.eq_with_variable_defs import EquationWithVariableDefinitions
from pltemplates.graphics.dcf import get_dcf_overview_graphic
from pltemplates.hyperlink import Hyperlink


AUTHORS = ['Nick DeRobertis']
SHORT_TITLE = 'Intro DCF and Cost of Capital'
SUBTITLE = 'A Primer on DCF Valuation and Exploring the Cost of Capital Section of the Model'

SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [
    ['University of Florida', 'Department of Finance, Insurance, and Real Estate'],
]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = plbuild.paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = plbuild.paths.HANDOUTS_BUILD_PATH
TITLE = 'Introduction to DCF Valuation and Cost of Capital Estimation'
ORDER = 13


def get_content():
    dcf_overview_graphic = get_dcf_overview_graphic()

    return [
        pl.Section(
            [
                lp.DimRevealListFrame(
                    [
                        pl.JinjaTemplate('A {{ "discounted cash flow valuation (DCF)" | Bold }} is a method of '
                                         'determining the value of a stock.').render(),
                        'Other ways include the dividend discount model and approaches based on comparables',
                        'The dividend discount model only works well for stable companies that pay dividends with '
                        'constant growth.',
                        'Comparable approaches can give a rough idea of a valuation but never take into account the '
                        'specifics of the company',
                        'DCF valuation can be applied to any company and is based on the particulars of the company'
                    ],
                    title='What is a DCF?'
                ),
                lp.GraphicFrame(
                    dcf_overview_graphic,
                    title='The DCF in One Picture'
                ),
                lp.Frame(
                    [
                        lp.Block(
                            [
                                pl.Equation(str_eq=r'V = \sum_{t=0}^T \frac{CF^t}{(1 + r)^t}')
                            ],
                            title='Financial Asset Value'
                        ),
                        pl.UnorderedList([lp.DimAndRevealListItems([
                            'The value of any financial asset is the present value of its future cash flows',
                            'The cash flows for a stock are dividends. The dividend discount model takes the present '
                            'value of future dividends.',
                            'To find the value of a business, find the present value of its future free cash flows'
                        ])]),
                    ],
                    title='Motivating the DCF'
                ),
                lp.DimRevealListFrame(
                    [
                        'The enterprise value of the business is the asset value or the cost to purchase the '
                        'entire company',
                        pl.Equation(
                            str_eq=f'{pl.Text("Enterprise Value")} = {pl.Text("Equity Value")} + '
                                   f'{pl.Text("Debt Value")} - {pl.Text("Cash")}'
                        ),
                        'A stock represents only the equity value or market capitalization of a business',
                        'By determining the enterprise value, we can back into the equity value to get the stock price'
                    ],
                    title='Enterprise Value vs. Equity Value'
                )
            ],
            title='Introduction to Discounted Cash Flow (DCF) Valuation',
            short_title='DCF Intro'

        )

    ]

DOCUMENT_CLASS_KWARGS = dict(
    nav_header=True,
    toc_sections=True
)
OUTPUT_NAME = TITLE

