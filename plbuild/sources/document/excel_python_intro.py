import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

import plbuild
from plbuild.paths import images_path


AUTHORS = ['Nick DeRobertis']

DOCUMENT_CLASS = pl.Document
OUTPUT_LOCATION = plbuild.paths.DOCUMENTS_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = None

TITLE = 'Project 1 - Excel and Python TVM'
ORDER = None


def get_content():
    return [
        'something'
    ]


