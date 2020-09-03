from dataclasses import dataclass
from typing import List, Sequence, Optional

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

TITLE = 'Course Schedule'
ORDER = 'C2'


@dataclass
class ClassContent:
    summary: str
    lectures: Sequence[int]

    assigned_projects: Optional[Sequence[int]] = None
    projects_due: Optional[Sequence[int]] = None


def get_content():
    weeks = [
        ClassContent(  # week 1
            'Introduction to the Class, Modeling, Python, and Excel',
            [1, 2],
        ),
        ClassContent(  # week 2
            'Building a Full Excel Model and Python Basics',
            [3, 4],
            [1],
        ),
        ClassContent(  # week 3
            'Python Basics, Continued',
            [4],
        ),
        ClassContent(  # week 4
            'Wrapping up Python Basics, and Building a Full Python Model',
            [4, 5]
        ),
        ClassContent(  # week 5
            'Building a Full Python Model and Visualization',
            [5, 6]
        ),
        ClassContent(  # week 6
            'Visualization and Sensitivity Analysis',
            [6, 7],
            None,
            [1]
        ),
        ClassContent(  # week 7
            'Sensitivity Analysis',
            [7],
            [2]
        ),
        ClassContent(  # week 8
            'Probability Modeling',
            [8],
        ),
        ClassContent(  # week 9
            'Probability Modeling and Combining Excel and Python',
            [8, 9]
        ),
        ClassContent(  # week 10
            'Monte Carlo Simulation',
            [10],
            [3],
            [2]
        ),
        ClassContent(  # week 11
            'Introduction to DCF Valuation and Cost of Capital Estimation',
            [11],
        ),
        ClassContent(  # week 12
            'Cost of Capital Estimation and Free Cash Flow Estimation',
            [11, 12],
            [4],
            [3],
        ),
        ClassContent(  # week 13
            'Forecasting Free Cash Flows',
            [12],
        ),
        ClassContent(  # week 14
            'Advanced Financial Modeling Roadmap',
            [13],
        )
    ]


    return [

    ]

DOCUMENT_CLASS_KWARGS = dict(
    remove_section_numbering=True,
    # packages=default_packages + [pl.Package('hyperref', modifier_str='colorlinks, linkcolor=blue')]
)
OUTPUT_NAME = TITLE

