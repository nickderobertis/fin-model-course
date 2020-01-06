from typing import List, Tuple
import time

from pythoncom import com_error
import xlwings as xw

from gradetools.excel.values import get_non_none_range_value


def calculate_app_extract_irrs(n_iter: int = 3, out_cell: str = 'B15') -> Tuple[List[float], int]:

    app = list(xw.apps)[0]
    values = []
    iter_count = 0
    while len(values) < n_iter:
        iter_count += 1
        if iter_count > n_iter * 5:
            # With 5x as many iterations as should be needed, still haven't extracted enough values, must have issue
            raise ValueError(f'could not get enough results from {out_cell}. Have {len(values)} results '
                             f'after {iter_count} iterations')
        try:
            app.api.CalculateFull()
        except com_error:
            time.sleep(.1)
            continue
        value = get_non_none_range_value(out_cell, retries=1000)
        values.append(value)

    return values, iter_count
