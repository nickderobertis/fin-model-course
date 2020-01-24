from gradetools.excel.values import set_range_value


def set_inputs(p_machine: int = 1000000, loan_life: int = 5, init_default: float = 0.3,
              decay_prob: float = 0.9, final_default: float = 0.4, recovery: float = 0.4,
              interest_rate: float = 0.2):
    input_cell_dict = {
        'B2': p_machine,
        'B3': loan_life,
        'B4': init_default,
        'B5': decay_prob,
        'B6': final_default,
        'B7': recovery,
        'B8': interest_rate
    }
    for cell, inp in input_cell_dict.items():
        set_range_value(inp, cell)
