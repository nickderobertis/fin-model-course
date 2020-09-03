import os

import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll
from jinja2 import FileSystemLoader

import plbuild
from plbuild.paths import images_path

AUTHORS = ['Nick DeRobertis']

DOCUMENT_CLASS = pl.Document
OUTPUT_LOCATION = plbuild.paths.DOCUMENTS_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = None

TITLE = 'Python Retirement Savings Rate Problem'
ORDER = 'PR1'


def get_content():
    jinja_templates_path = os.path.sep.join(['pltemplates', 'practice', 'python_retirement'])
    jinja_env = pl.JinjaEnvironment(loader=FileSystemLoader(jinja_templates_path))
    return [
        pl.Section(
            [
                pl.SubSection(
                    [
                        PythonRetirementPracticeProblemModel(template_path='prob_definition.j2', environment=jinja_env),
                    ],
                    title='Problem Definition'
                ),
                pl.SubSection(
                    [
                        pl.Center(
                            lt.Tabular(
                                [
                                    lt.TopRule(),
                                    lt.ValuesTable.from_list_of_lists([[
                                        'Input', 'Default Value',
                                    ]]),
                                    lt.MidRule(),
                                    lt.ValuesTable.from_list_of_lists(
                                        [

                                            ['Starting Salary', '\$50,000'],
                                            ['Salary Growth', '3%'],
                                            ['Mid-Salary Cutoff', r'\$80,000'],
                                            ['High-Salary Cutoff', r'\$120,000'],
                                            ['Low Savings Rate', '10%'],
                                            ['Mid Savings Rate', '25%'],
                                            ['High Savings Rate', '40%'],
                                            ['Interest Rate', '5%'],
                                            ['Desired Cash', r'\$1,500,000'],
                                        ],
                                    ),
                                    lt.BottomRule(),
                                ],
                                align='l|cc'
                            )
                        )
                    ],
                    title='Inputs'
                ),
                pl.SubSection(
                    [
                        """
                        The final answer with the default inputs should be 37 years to retirement. Try hard to get
                        there working from scratch. If you are very stuck, then try taking the Dynamic Salary
                        Retirement model and modifying it. If you are still stuck, then check the provided Jupyter 
                        notebook solution. If you have a lot of trouble with this, please see me in office hours or
                        after class, as your first project will be similar but a bit more difficult.
                        """

                    ],
                    title='Solution'
                )
            ],
            title='Capital Budgeting Probabilities with Monte Carlo Simulation'
        )
    ]


class PythonRetirementPracticeProblemModel(pl.Model):
    pass


DOCUMENT_CLASS_KWARGS = dict(
    remove_section_numbering=True,
)
OUTPUT_NAME = TITLE

