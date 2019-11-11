from typing import List
import time

from pythoncom import com_error
import xlwings as xw

from gradetools.excel.values import get_range_value


def calculate_app_extract_irrs(n_iter: int = 3, out_cell: str = 'B15') -> List[float]:

    app = list(xw.apps)[0]
    values = []
    iter_count = 0
    while len(values) < n_iter:
        iter_count += 1
        try:
            app.api.CalculateFull()
            value = get_range_value(out_cell)
        except com_error:
            continue
        if value is None:
            continue
        values.append(value)
        if iter_count > n_iter * 10:
            # With 10x as many iterations as should be needed, still haven't extracted enough values, must have issue
            raise ValueError(f'could not get enough results from {out_cell}. Have {len(values)} results '
                             f'after {iter_count} iterations')
    return values
