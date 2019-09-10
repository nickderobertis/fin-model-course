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
ORDER = 7


def get_content():
    return [
        lp.DimRevealListFrame(
            [
                "So far we've had one main output from our model, number of years"
            ],
            title='Why Visualize?'
        )
    ]


DOCUMENT_CLASS_KWARGS = {}
OUTPUT_NAME = TITLE