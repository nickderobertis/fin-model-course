from typing import List
import time

from pythoncom import com_error
import xlwings as xw

from gradetools.excel.values import get_range_value


def calculate_app_extract_irrs(n_iter: int = 3, out_cell: str = 'B15') -> List[float]:

    app = list(xw.apps)[0]
    values = []
    for i in range(n_iter):
        try:
            app.api.CalculateFull()
            values.append(get_range_value(out_cell))
        except com_error:
            continue
    return [value for value in values if value is not None]
