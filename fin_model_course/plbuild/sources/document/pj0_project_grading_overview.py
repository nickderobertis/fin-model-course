import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll

import plbuild
from plbuild.paths import images_path
from pltemplates.hyperlink import Hyperlink


AUTHORS = ['Nick DeRobertis']

DOCUMENT_CLASS = pl.Document
OUTPUT_LOCATION = plbuild.paths.DOCUMENTS_BUILD_PATH
HANDOUTS_OUTPUT_LOCATION = None

TITLE = 'Project Grading Overview'
ORDER = 'PJ0'


def get_content():
    return [
        pl.Section(
            [
                'You will be graded across several dimensions in completing projects. These dimensions include, but '
                'are not limited to: ',
                pl.UnorderedList([
                    'Model Accuracy',
                    'Model Readability',
                    'Model Formatting',
                    'Following the Template',
                ]),
                'Some projects may have their own specific categories. If so, the criteria for that category will '
                "be defined in that project's description."
            ],
            title='The Grading Categories'
        ),
        pl.Section(
            [
                'I will first look at all the models before grading any of them. This is how I will establish what '
                'to expect. The grading is somewhat absolute and somewhat relative. For example, if your model is '
                'completely accurate, you will receive a 100% for model accuracy. But, you could also receive a high '
                'grade for model accuracy even if there are errors, if the rest of the class made similar errors. '
                'Partial credit will be given in every category. The amount of points given will be proportional '
                'to how well you completed the category, on an absolute basis if applicable and also relative to '
                'other students.'
            ],
            title='The Score in a Category'
        ),
        pl.Section(
            [
                'The weights of each category will be specific to the project. Generally, Model Accuracy will '
                'carry the highest weight, and Model Formatting will carry the lowest weight. Look '
                'to the project description for a breakdown of the weights.'
            ],
            title='The Grading Weights of the Categories'
        ),
        pl.Section(
            [
                pl.UnorderedList([
                    'Does the model obtain the correct results?',
                    'When inputs are changed, does the output change appropriately?',
                    'Can the model handle the full range of possible values?'
                ])
            ],
            title='Model Accuracy'
        ),
        pl.Section(
            [
                "Model readability is all about how easily can I understand what you're doing in the model, "
                "and how easily I can navigate through it.",
                pl.SubSection(
                    [
                        pl.UnorderedList([
                            'Is the model organized into sections using tabs?',
                            'Are there clear names for inputs, outputs, and table headers?',
                            'Is each tab organized to separate inputs, outputs, and calculation?',
                            'Are there any comments explaining complex parts of the model?'
                        ])
                    ],
                    title='Excel'
                ),
                pl.SubSection(
                    [
                        pl.UnorderedList([
                            'Is the model organized into functions and sections?',
                            'Are all inputs at the top and main outputs at the bottom?',
                            'Are there docstrings, comments, or Jupyter markdown explaining things?',
                            'Does the submitted notebook or Python script have clear sections?',
                            'Are the length of code lines limited to the size of Jupyter cells (no long lines)?',
                            'Are the results of intermediate calculations shown? Should not be just one answer at end.',
                            [
                                'Do variable, function, and class names follow conventions? See',
                                Hyperlink('https://realpython.com/python-pep8/#naming-conventions', 'Naming Conventions')
                            ],
                        ])
                    ],
                    title='Python'
                )
            ],
            title='Model Readability'
        ),
        pl.Section(
            [
                "Model formatting is about the visual representation of the model.",
                pl.SubSection(
                    [
                        pl.UnorderedList([
                            'Are tables formatted nicely?',
                            'Are inputs and outputs sections formatted to separate them from calculations?'
                        ])
                    ],
                    title='Excel'
                ),
                pl.SubSection(
                    [
                        pl.UnorderedList([
                            'Are model outputs displayed with nice formatting?',
                            pl.UnorderedList([
                                'Number formatting (percentages are percentages, '
                                'currency has dollar sign, commas, and two decimals, etc.)',
                                'Sentence explaining results is printed',
                                'Tables are used where appropriate and are well formatted',
                                'Plots have axis names and are appropriately sized'
                            ])
                        ])
                    ],
                    title='Python'
                )
            ],
            title='Model Formatting'
        ),
        pl.Section(
            [
                "Following the template is about conforming to the requested structure of the project "
                "such that it can be graded in a uniform way.",
                pl.SubSection(
                    [
                        pl.UnorderedList([
                            'Use any provided template to start from',
                            'Do not move any of the inputs or outputs from the template',
                            'It is fine to change formatting of the inputs and outputs so long as the cell '
                            'reference location stay the same'
                        ])
                    ],
                    title='Excel'
                ),
                pl.SubSection(
                    [
                        pl.UnorderedList([
                            'Use any provided template to start from',
                            'Do not change the name of the ModelInputs class and be sure to use model_data as '
                            'the name of the variable containing the inputs',
                            'Do not rename variables in the ModelInputs dataclass. You may add additional variables '
                            'if you wish.',
                            'Keep the inputs at the top and outputs at the bottom',
                            'The instructions for a project may ask you to define certain variables and that they '
                            'should conform to certain data structures. Ensure that you do this and do not use '
                            'a different name or data structure.',
                            'For example, it may ask for cash_flows as a list of numbers. Ensure that you actually '
                            'have numbers in it and not formatted strings. However when you show the output '
                            'you should format it.'
                        ])
                    ],
                    title='Python'
                )
            ],
            title='Following the Template'
        ),
    ]

DOCUMENT_CLASS_KWARGS = dict(
    remove_section_numbering=True
)
OUTPUT_NAME = TITLE

