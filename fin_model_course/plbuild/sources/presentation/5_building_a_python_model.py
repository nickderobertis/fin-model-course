import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

import plbuild
from plbuild.paths import images_path
from pltemplates.exercises.lab_exercise import LabExercise
from pltemplates.frames.lab import LabFrame
from pltemplates.frames.model_flowchart import (
    ModelFlowchartFrame,
    real_world_style,
    model_style,
    in_out_style
)
from pltemplates.blocks import LabBlock
from pltemplates.frames.tvm.salary_eq import salary_block_content
from pltemplates.frames.tvm.retirement_model_structure import get_retirement_model_overview_frame
from pltemplates.hyperlink import Hyperlink

TITLE = 'The Depth of a Financial Model, Continued'
SHORT_TITLE = 'TVM Deep Dive Python'
SUBTITLE = 'Extending a Simple Retirement Model in Python'
ORDER = 5


AUTHORS = ['Nick DeRobertis']
SHORT_AUTHOR = 'DeRobertis'
INSTITUTIONS = [['University of Florida', 'Department of Finance, Insurance, and Real Estate']]
SHORT_INSTITUTION = 'UF'

DOCUMENT_CLASS = lp.Presentation
OUTPUT_LOCATION = plbuild.paths.SLIDES_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = plbuild.paths.HANDOUTS_BUILD_PATH


def get_content():

    next_until_end_ov = lp.Overlay([lp.UntilEnd(lp.NextWithIncrement())])


    return [
        pl.Section(
            [
                lp.DimRevealListFrame(
                    [
                        'We have seen how structure and organization can help the readability and maintainability of '
                        'an Excel model. The same concept exists for our Python models.',
                        ['We already learned that we should use functions to organize logic and a',
                         pl.Monospace('dataclass'),
                         'for the model inputs'],
                        "Typically you'll have functions for each step, those may be wrapped up into other functions which "
                        "perform larger steps, and ultimately you'll have one function which does everything by calling the"
                        "other functions.",
                        "Those are good ideas with any Python model, but working in Jupyter allows us some additional "
                        "organization and presentation of the model"
                    ],
                    title='How to Structure a Python Financial Model'
                ),
                lp.DimRevealListFrame(
                    [
                        'In Jupyter, we can have code, nicely formatted text, equations, sections, hyperlinks, '
                        'and graphics, all in one document',
                        ['For all you can do with these nicely formatted "Markdown" cells, see',
                         Hyperlink('https://www.markdownguide.org/basic-syntax/', 'here'), 'and',
                         Hyperlink('https://www.markdownguide.org/extended-syntax/', 'here.')],
                        'We can think of sections in Jupyter as analagous to Excel sheets/tabs. One section for each '
                        'logical part of your model. Then you can have smaller headings for subsections of the model.',
                        'Break your code up into small sections dealing with each step, with nicely formatted text '
                        'explaining it. Add comments where anything is unclear in the code.',
                    ],
                    title='Using Jupyter for Structure of a Model'
                ),
                lp.DimRevealListFrame(
                    [
                        'When I develop in Jupyter, I have lots of cells going everywhere testing things out',
                        ['When I finish a project in Jupyter, I remove these testing cells and make sure it runs and '
                         'logically flows from end to end', pl.Monospace('(restart kernel and run all cells)')],
                        "Run your model with different inputs, and make sure the outputs change in the expected fashion. This "
                        "is a good way to check your work.",
                        'There may be outputs in each section, but the final output should be at the end of the notebook',
                    ],
                    title='Workflow and Final Output'
                ),
            ],
            title='Structuring a Model in Python and Jupyter',
            short_title='Model Structure'
        ),
        pl.Section(
            [
                get_retirement_model_overview_frame(),
                lp.Frame(
                    [
                        lp.Block(
                            salary_block_content,
                            title='Salary with Promotions and Cost of Living Raises'
                        )
                    ],
                    title='Revisiting the Model Salary Equation'
                ),
                lp.Frame(
                    [
                        pl.UnorderedList([
                            'For wealths, we need to add the investment return and then the savings in each year',
                        ], overlay=next_until_end_ov),
                        pl.VFill(),
                        lp.Block(
                            [
                                lp.adjust_to_full_size_and_center(
                                    pl.Equation(str_eq=r'W_t = W_{t-1}  (1 + r_i) + S_t  v')),
                                pl.UnorderedList([
                                    f'{pl.Equation(str_eq="S_t")}:  Salary at year {pl.Equation(str_eq="t")}',
                                    f'{pl.Equation(str_eq="W_t")}:  Wealth at year {pl.Equation(str_eq="t")}',
                                    f'{pl.Equation(str_eq="r_i")}:  Investment return',
                                    f'{pl.Equation(str_eq="t")}:  Number of years',
                                    f'{pl.Equation(str_eq="v")}:  Savings rate',
                                ])
                            ],
                            title='Calculating Wealth',
                            overlay=next_until_end_ov,
                        )
                    ],
                    title='Building the Wealth Model'
                ),
                LabExercise(
                    [
                        [
                            "Usually I would try to have smaller labs but it didn't fit the format of this lecture. "
                            "Most will not be able to complete this during class.",
                            "For this lab, attempt the practice problem in Practice > Retirement > "
                            "P1 Python Retirement Savings Rate Problem.pdf",
                            'This is similar to how the projects will be assigned, so it is good preparation',
                            "I would encourage you to try it from scratch. If you are totally stuck, try working off "
                            "of the retirement model I completed today to have a lot of the structure already. If you "
                            "still are having trouble with that, check the solution and see me in office hours."
                        ]
                    ],
                    block_title='Practice Building A Model',
                    frame_title='Extending the Simple Retirement Model in a Different Way',
                    label='lab:retire-model'
                )
            ],
            title='Building the Dynamic Salary Retirement Model',
            short_title='Build the Model'
        ),
    ]


DOCUMENT_CLASS_KWARGS = dict(
    nav_header=True,
    toc_sections=True
)
OUTPUT_NAME = TITLE