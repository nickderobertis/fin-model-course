import time
from typing import Any

from pythoncom import com_error
import xlwings as xw


def get_range_value(cell: str, retries=10):
    while True:
        if retries < 0:
            raise ValueError(f'could not get value for {cell} after retrying')
        try:
            return xw.Range(cell).value
        except com_error:
            retries -= 1
            time.sleep(.1)


def set_range_value(value: Any, cell: str, retries=10):
    while True:
        if retries < 0:
            raise ValueError(f'could not set value for {cell} after retrying')
        try:
            xw.Range(cell).value = value
            return
        except com_error:
            retries -= 1
            time.sleep(.1)
