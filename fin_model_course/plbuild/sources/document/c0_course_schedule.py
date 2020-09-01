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
ORDER = None


@dataclass
class ClassContent:
    summary: str
    lectures: Sequence[int]

    assigned_projects: Optional[Sequence[int]] = None
    projects_due: Optional[Sequence[int]] = None


def get_content():

    covered_in_each_class_tuples = [
        (
            'Introduction - What is this Class?',
            [1]
        ),
        (
            'Intro to Modeling, Python, and Excel',
            [2]
        ),
        (
            'Bulding a Full Excel Model',
            [3]
        ),
        (
            'Bulding a Basic Python Model and Python Basics, pt. 1',
            [3, 4]
        ),
        (
            'Python Basics, pt. 2',
            [4]
        ),
        (
            'Python Basics, pt. 3',
            [4]
        ),
        (
            'Python Basics, pt. 4',
            [4],
            [1]
        ),
        (
            'Bulding a Full Python Model, pt. 1',
            [5]
        ),
        (
            'Bulding a Full Python Model, pt. 2',
            [5]
        ),  # 2/4/2020
        (
            'Visualization, pt. 1',
            [6]
        ),  # 2/6/2020
        (
            'Visualization, pt. 2',
            [6],
            None,
            [1]
        ),  # 2/11/2020
        (
            'Visualization, pt. 3 and Sensitivity Analysis, pt. 1',
            [6, 7],
        ),  # 2/13/2020
        (
            'Sensitivity Analysis, pt. 2',
            [7],
        ),  # 2/18/2020
        (
            'Sensitivity Analysis, pt. 3',
            [7],
        ),  # 2/20/2020
        (
            'Probability Modeling, pt. 1',
            [8],
        ),  # 2/25/2020
        (
            'Probability Modeling, pt. 2',
            [8],
            [2],
        ),  # 2/27/2020
        (
            'Probability Modeling, pt. 3',
            [8],
        ),  # 3/10/2020
        (
            'Probability Modeling, pt. 4',
            [8],
        ),  # 3/12/2020
        (
            'Combining Excel and Python, pt. 1',
            [9],
        ),  # 3/17/2020
        (
            'Combining Excel and Python, pt. 2 and Monte Carlo Simulation, pt. 1',
            [9, 10],
        ),  # 3/19/2020
        (
            'Monte Carlo Simulation, pt. 2',
            [10],
            None,
            [2],
        ),  # 3/24/2020
        (
            'Monte Carlo Simulation, pt. 3',
            [10],
        ),  # 3/26/2020
        # NOTE: too far behind at this point, picking up the pace, need to speed up earlier
    ]

    return [

    ]

DOCUMENT_CLASS_KWARGS = dict(
    remove_section_numbering=True,
    # packages=default_packages + [pl.Package('hyperref', modifier_str='colorlinks, linkcolor=blue')]
)
OUTPUT_NAME = TITLE

