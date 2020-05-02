from typing import Dict, List
import json

import pandas as pd

from gradetools.project_3.config import TOLERANCES, ANSWERS_OUTPUT_PATH


def score_accuracy_of_result_dicts(results: List[Dict[str, float]], answers: List[Dict[str, float]],
                                   tolerances: Dict[str, float] = TOLERANCES) -> pd.DataFrame:
    valid: List[Dict[str, float]] = []
    for case_results, answer_results in zip(results, answers):
        case_valid = {}
        for item_key, result in case_results.items():
            tolerance = _get_tolerance(item_key, tolerances)
            answer = answer_results[item_key]
            if abs(float(result) - answer) < tolerance:
                case_valid[item_key] = True
            else:
                case_valid[item_key] = False
        valid.append(case_valid)
    valid_df = pd.DataFrame(valid, index=[f'{i + 1} Valid' for i in range(len(valid))]).T
    results_df = pd.DataFrame(results, index=[f'{i + 1} Results' for i in range(len(results))]).T
    answers_df = pd.DataFrame(answers, index=[f'{i + 1} Answers' for i in range(len(answers))]).T
    df = pd.concat([valid_df, results_df, answers_df], axis=1)
    sorted_cols = sorted(list(df.columns))
    df = df[sorted_cols]
    return df


def _get_tolerance(item_key: str, tolerances: Dict[str, float]) -> float:
    try:
        tolerance = tolerances[item_key]
    except KeyError:
        tolerance = tolerances['other']
    return tolerance


def load_answers(answers_path: str = ANSWERS_OUTPUT_PATH) -> List[Dict[str, float]]:
    with open(answers_path, 'r') as f:
        answers = json.load(f)
    return answers
