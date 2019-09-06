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
from pltemplates.labblock import LabBlock


AUTHORS = ['Nick DeRobertis']
SHORT_TITLE = 'Visualization'
SUBTITLE = 'An Introduction to Visualization'

SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [
    ['University of Florida', 'Department of Finance, Insurance, and Real Estate'],
]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = plbuild.paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = plbuild.paths.HANDOUTS_BUILD_PATH
TITLE = 'Understanding Complex Results'
ORDER = 6


def get_content():
    return [
        lp.DimRevealListFrame(
            [
                'Last time we finished building the Python model, and organized it in functions',
                'I mentioned previously that organizing models in classes makes sense',
                "We were constantly passing the same arguments around before. Let's look at how classes simplify this.",
                "You'll also see how using classes gives us a single unified interface to the model",
            ],
            title='Tidying up the Python Model'
        ),
        lp.Frame(
            [
                pl.UnorderedList([
                    'We want to relax the assumption that the amount needed in retirement is given by a fixed amount of desired cash'
                ]),
                pl.VFill(),
                LabBlock(
                    pl.UnorderedList([
                        'Add new inputs to the model, "Annual Cash Spend During Retirement" and "Years in Retirement"',
                        'Calculate desired cash based on interest, cash spend, and years in retirement',
                        'Use the calculated desired cash in the model to determine years to retirement',
                        r'If annual spend is 40k for 25 years in retirement, \$563,757.78 should be the retirement cash'
                    ]),
                    title='Modeling Desired Cash'
                )
            ],
            title='Relaxing the Static Desired Cash in Python'
        ),
        lp.DimRevealListFrame(
            [
                "So far we've had one main output from our model, number of years"
            ],
            title='Why Visualize?'
        )
    ]


DOCUMENT_CLASS_KWARGS = {}
OUTPUT_NAME = TITLE