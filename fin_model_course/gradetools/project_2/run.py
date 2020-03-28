import itertools
from typing import Dict, List

import pandas as pd

from gradetools.model_type import ModelType
from gradetools.project_2.calculate import run_model_extract_irr_df
from gradetools.project_2.inputs import set_inputs


def run_model_assemble_results_in_df(input_dicts: List[Dict[str, float]], model_type: ModelType,
                                     model_file: str) -> pd.DataFrame:
    all_dfs = []
    for input_dict in input_dicts:
        set_inputs(model_type, model_file, **input_dict)
        df = run_model_extract_irr_df(model_file, model_type, input_dict)
        for inp_name, inp_value in input_dict.items():
            df[inp_name] = inp_value
        all_dfs.append(df)

    df = pd.concat(all_dfs, axis=0)
    return df
