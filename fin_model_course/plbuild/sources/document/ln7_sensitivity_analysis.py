import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

import plbuild
from lectures.sensitivity_analysis.main import get_sensitivity_analysis_lecture
from plbuild.paths import images_path
from schedule.main import LECTURE_7_NAME

AUTHORS = ['Nick DeRobertis']

DOCUMENT_CLASS = pl.Document
OUTPUT_LOCATION = plbuild.paths.DOCUMENTS_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = None

TITLE = LECTURE_7_NAME
ORDER = 'LN7'


def get_content():
    return [
        get_sensitivity_analysis_lecture().to_models()
    ]

DOCUMENT_CLASS_KWARGS = {}
OUTPUT_NAME = TITLE

