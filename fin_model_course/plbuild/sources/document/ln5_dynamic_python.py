import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

import plbuild
from lectures.dynamic_python.main import get_dynamic_salary_python_lecture
from lectures.python_basics.main import get_python_basics_lecture
from plbuild.paths import images_path
from schedule.main import LECTURE_4_NAME, LECTURE_5_NAME

AUTHORS = ['Nick DeRobertis']

DOCUMENT_CLASS = pl.Document
OUTPUT_LOCATION = plbuild.paths.DOCUMENTS_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = None

TITLE = LECTURE_5_NAME
ORDER = 'LN5'


def get_content():
    return [
        get_dynamic_salary_python_lecture().to_models()
    ]

DOCUMENT_CLASS_KWARGS = {}
OUTPUT_NAME = TITLE

