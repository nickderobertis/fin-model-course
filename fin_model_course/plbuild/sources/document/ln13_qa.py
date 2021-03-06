import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

import plbuild
from lectures.basic_qa.main import get_basic_q_and_a_lecture
from plbuild.paths import images_path
from schedule.main import LECTURE_13_NAME

AUTHORS = ['Nick DeRobertis']

DOCUMENT_CLASS = pl.Document
OUTPUT_LOCATION = plbuild.paths.DOCUMENTS_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = None

TITLE = LECTURE_13_NAME
ORDER = 'LN13'


def get_content():
    return [
        get_basic_q_and_a_lecture().to_models()
    ]

DOCUMENT_CLASS_KWARGS = {}
OUTPUT_NAME = TITLE

