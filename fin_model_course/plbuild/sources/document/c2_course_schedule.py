import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll
from pyexlatex.models.landscape import Landscape

import plbuild
from plbuild.paths import images_path
from schedule.main import get_course_schedule

AUTHORS = ['Nick DeRobertis']

DOCUMENT_CLASS = pl.Document
OUTPUT_LOCATION = plbuild.paths.DOCUMENTS_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = None

TITLE = 'Course Schedule'
ORDER = 'C2'


def get_content():
    schedule = get_course_schedule()
    return schedule.to_pyexlatex()

DOCUMENT_CLASS_KWARGS = dict(
    remove_section_numbering=True,
    skip_title_page=True,
    page_modifier_str='margin=0.3in, bottom=0.9in'
    # packages=default_packages + [pl.Package('hyperref', modifier_str='colorlinks, linkcolor=blue')]
)
OUTPUT_NAME = TITLE

