from typing import Union, Dict, Sequence

from gradetools.project_1.config import PROJECT_1_NOTEBOOK_PATH
from gradetools.py.execute2.main import read_notebook_and_run_extracting_globals, ReplacementConfig

INPUT_CASES = [
    dict(
        n_phones=100000,
        n_machines=5,
        n_life=10,
        price_phone=500,
        price_scrap=50000,
        d_1=100000,
        g_d=0.2,
        interest=0.05,
        cost_machine_adv=1000000,
        cogs_phone=250,
    ),
    dict(
        n_phones=1000000,
        n_machines=3,
        n_life=5,
        price_phone=200,
        price_scrap=30000,
        d_1=1000000,
        g_d=0.25,
        interest=0.04,
        cost_machine_adv=2000000,
        cogs_phone=200,
    ),
    dict(
        n_phones=10000,
        n_machines=1,
        n_life=18,
        price_phone=2000,
        price_scrap=300000,
        d_1=100000,
        g_d=0.15,
        interest=0.06,
        cost_machine_adv=500000,
        cogs_phone=10,
    ),
    dict(
        n_phones=1000,
        n_machines=1,
        n_life=2,
        price_phone=20,
        price_scrap=300000,
        d_1=100000,
        g_d=0.1,
        interest=0.1,
        cost_machine_adv=10000,
        cogs_phone=500,
    )
]

def output_dict_from_input_dict(input_dict: Dict[str, Union[int, float]]):
    rc = ReplacementConfig('model_data', 'ModelInputs', kwargs=input_dict)
    globs = read_notebook_and_run_extracting_globals(PROJECT_1_NOTEBOOK_PATH, replacements=[rc], suppress_output=True)
    correct_values = dict(
        npv=globs['npv'],
        cash_flows=globs['cash_flows']
    )
    return correct_values


OUTPUT_CASES = [output_dict_from_input_dict(input_dict) for input_dict in INPUT_CASES]
