import os

ANSWERS_MODEL_FOLDER = os.path.sep.join(['Projects', 'Project 2', 'For Answers'])
ANSWERS_OUTPUT_PATH = os.path.sep.join(['gradetools', 'project_2', 'answers.csv'])

NUM_ITERATIONS = 1000

INPUT_DICTS = [
    dict(
        price_machine=1000000,
        default_decay=0.9,
        final_default=0.4,
        recovery_rate=0.4,
    ),
    dict(
        price_machine=2000000,
        default_decay=0.8,
        final_default=0.5,
        recovery_rate=0.3,
    )
]
for inp_dict in INPUT_DICTS:
    inp_dict['num_iterations'] = NUM_ITERATIONS

EXCEL_INPUT_LOCATIONS = {
    'price_machine': 'B2',
    'default_decay': 'B5',
    'final_default': 'B6',
    'recovery_rate': 'B7',
}

EXCEL_OUTPUT_TABLE_LOCATION = 'D17'

TOLERANCE = 0.03
