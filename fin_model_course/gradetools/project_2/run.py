import itertools
from typing import Dict, List

import pandas as pd

from gradetools.project_2.calculate import calculate_app_extract_irrs
from gradetools.project_2.inputs import set_inputs


def run_model_assemble_results_in_df(n_iter: int, input_dicts: List[Dict[str, float]]) -> pd.DataFrame:

    interest_rates = [i/100 for i in range(20, 41, 2)]
    init_default_probs = [0.2, 0.3]



    all_values = []
    for interest_rate, init_default in itertools.product(interest_rates, init_default_probs):
        for input_dict in input_dicts:
            set_inputs(init_default=init_default, interest_rate=interest_rate, **input_dict)
            values, ran_iter = calculate_app_extract_irrs(n_iter)
            all_values.append(
                (
                    interest_rate,
                    init_default,
                    sum(values) / len(values),
                    input_dict['p_machine'],
                    input_dict['loan_life'],
                    input_dict['decay_prob'],
                    input_dict['final_default'],
                    input_dict['recovery'],
                    len(values),
                    ran_iter
                )
            )

    df = pd.DataFrame(
        all_values,
        columns=[
            'Interest Rate',
            'Initial Default Probability',
            'IRR',
            'Price Machine',
            'Loan Life',
            'Decay Default',
            'Final Default',
            'Recovery',
            'Count',
            'Iter Count'
        ]
    )
    return df
