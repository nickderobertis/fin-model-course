import pyexlatex as pl
import pyexlatex.presentation as lp
from pltemplates.blocks import LabBlock


def get_project_1_lab_frame():
    return lp.Frame(
        [
            LabBlock(
                pl.UnorderedList([
                    'Download and open the Project 1 document from Canvas',
                    "It is up to you whether you want to attempt the Excel or Python model first",
                    "If you feel comfortable with the Excel model, you may want to start with Python so I "
                    "can give help on that today."
                ]),
                title='Project 1'
            )
        ],
        title='Some Time to Work on the First Project'
    )