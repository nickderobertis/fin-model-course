import xlwings as xw
from pythoncom import com_error
import time


class CannotCollectOutputsException(Exception):
    pass


def run_workbook_collect_outputs():
    wb = xw.Book.caller()
    wb.sheets['Trials'].range('A:A').clear()
    n_iter = wb.sheets['Inputs and Outputs'].range('B11').value
    for i in range(int(n_iter)):
        output_row = i + 1
        finished = False
        retries = 0
        while not finished:
            try:
                result = wb.sheets['Inputs and Outputs'].range('B15').value
                wb.sheets['Trials'].range(f'A{output_row}').value = result
                wb.app.api.CalculateFull()
                finished = True
            except com_error:
                # Expected to hit these issues when running too fast for Excel to keep up
                time.sleep(.5)
                retries += 1
                if retries > 3:
                    # Something is really wrong, cannot calculate at all anymore, exit the loop
                    raise CannotCollectOutputsException('could not calculate workbook after trying 3 times over 1.5s')
                
