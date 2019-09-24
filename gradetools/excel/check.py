from typing import Union, List, Optional


def check_output_dict(output_dict: dict, correct_dict: dict, tolerance: float = 0.001):
    for output_name, value in output_dict.items():
        correct_value = correct_dict[output_name]
        _check_value(value, correct_value, value_name=output_name, tolerance=tolerance)


def _check_value(value: Union[float, List[float]], correct_value: Union[float, List[float]],
                 value_name: Optional[str] = None,
                 tolerance: float = 0.001):
    if isinstance(value, list):
        return [_check_value(val, correct_val) for val, correct_val in zip(value, correct_value)]

    # Assumed to be float
    if abs(float(value) - correct_value) > tolerance:
        print(f'got incorrect value {value} for {value_name}. Should be {correct_value}')
