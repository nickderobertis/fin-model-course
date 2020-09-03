import os

import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll
from jinja2 import FileSystemLoader

import plbuild
from plbuild.paths import images_path
from schedule.main import PROJECT_4_NAME

AUTHORS = ['Nick DeRobertis']

DOCUMENT_CLASS = pl.Document
OUTPUT_LOCATION = plbuild.paths.DOCUMENTS_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = None

TITLE = PROJECT_4_NAME
ORDER = 'PJ4'


def get_content():
    jinja_templates_path = os.path.sep.join(['pltemplates', 'projects', 'p4'])
    jinja_env = pl.JinjaEnvironment(loader=FileSystemLoader(jinja_templates_path))

    return [
        pl.Section(
            [
                pl.SubSection(
                    [
                        Project4ProblemModel(template_path='prob_definition.j2', environment=jinja_env),
                    ],
                    title='Problem Definition'
                ),
                pl.SubSection(
                    [
                        Project4ProblemModel(template_path='notes.j2', environment=jinja_env),
                    ],
                    title='Notes'
                ),
                pl.SubSection(
                    [
                        Project4ProblemModel(template_path='bonus.j2', environment=jinja_env),
                    ],
                    title='Bonus'
                )
            ],
            title='Overview'
        ),
        pl.Section(
            [
                pl.SubSection(
                    [
                        Project4ProblemModel(template_path='submission.j2', environment=jinja_env),
                    ],
                    title='Submission'
                ),
                pl.SubSection(
                    [
                        pl.Center(
                            lt.Tabular(
                                [

                                    pl.MultiColumnLabel('Grading Breakdown', span=2),
                                    lt.TopRule(),
                                    lt.ValuesTable.from_list_of_lists(
                                        [
                                            ['Category', 'Percentage']
                                        ]
                                    ),
                                    lt.TableLineSegment(0, 1),
                                    lt.ValuesTable.from_list_of_lists(
                                        [
                                            ['Model Accuracy', '60%'],
                                            ['Model Readability', '30%'],
                                            ['Model Formatting', '10%'],
                                            ['Bonus', '5%']
                                        ]
                                    ),
                                    lt.MidRule(),
                                    lt.ValuesTable.from_list_of_lists(
                                        [
                                            ['Total Possible', '105%']
                                        ]
                                    ),
                                    lt.BottomRule()

                                ],
                                align='l|c'
                            )
                        )
                    ],
                    title='Grading'
                ),
            ],
            title='Submission & Grading'
        )
    ]

class Project4ProblemModel(pl.Model):
    model_requirements = [
        'WACC estimation',
        'FCF estimation and forecasting (must forecast financial statements, not only FCFs directly, though that can be an extra check)',
        'A written justification for why statements were forecasted as they were',
        'Terminal value estimation using both perpetuity growth and various exit multiples',
        'Monte carlo simulation',
        'Sensitivity analysis',
        'Scenario analysis',
        'Visualization'
    ]


DOCUMENT_CLASS_KWARGS = dict(
    remove_section_numbering=True,
)
OUTPUT_NAME = TITLE

