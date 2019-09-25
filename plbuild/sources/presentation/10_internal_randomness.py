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
from pltemplates.eq_with_variable_defs import EquationWithVariableDefinitions


AUTHORS = ['Nick DeRobertis']
SHORT_TITLE = 'Internal Randomness'
SUBTITLE = 'An Approach to Probability Modeling'

SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [
    ['University of Florida', 'Department of Finance, Insurance, and Real Estate'],
]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = plbuild.paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = plbuild.paths.HANDOUTS_BUILD_PATH
TITLE = 'Building Randomness Into Models'
ORDER = 10


def get_content():
    return [
        lp.DimRevealListFrame(
            [
                ["Using the technique of", pl.Bold('internal randomness,'),
                 'something random is added internally to the model'],
                'Instead of taking a fixed input, random values for that variable are drawn',
                'This technique can be used with both discrete and continuous variables'
            ],
            title='What is Internal Randomness?'
        )
    ]

DOCUMENT_CLASS_KWARGS = {}
OUTPUT_NAME = TITLE

