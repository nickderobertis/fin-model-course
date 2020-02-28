from typing import Any

import pandas as pd
import numpy as np


def values_are_same(val1: Any, val2: Any, tolerance: float) -> bool:
    """
    Compares whether values are the same for grading purposes. Converts arrays and series
    to lists. Uses a tolerance to allow for float/rounding errors.

    :param val1:
    :param val2:
    :param tolerance:
    :return:
    """
    val1 = _to_list(val1)
    val2 = _to_list(val2)

    if len(val1) != len(val2):
        return False

    for v1, v2 in zip(val1, val2):
        try:
            abs_diff = abs(v1 - v2)
            if abs_diff > tolerance:
                return False
        except Exception as e:
            exc = str(e)
            raise CannotCompareOutputsException(f'Could not compare {v1} to {v2} because of: {exc}')

    return True


def _to_list(val: Any) -> list:
    if isinstance(val, list):
        return val

    if isinstance(val, tuple):
        return list(val)

    if isinstance(val, (pd.Series, np.ndarray)):
        return val.tolist()

    # Not a list-like, wrap in a list and return
    return [val]


class CannotCompareOutputsException(Exception):
    pass