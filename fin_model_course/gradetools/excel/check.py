from typing import Union, List, Optional


def check_output_dict(output_dict: dict, correct_dict: dict, tolerance: float = 0.001
                      ) -> List['IncorrectModelOutputException']:
    errors = []
    for output_name, value in output_dict.items():
        correct_value = correct_dict[output_name]
        _check_value(value, correct_value, value_name=output_name, tolerance=tolerance, errors=errors)
    return errors


def _check_value(value: Union[float, List[float]], correct_value: Union[float, List[float]],
                 value_name: Optional[str] = None,
                 tolerance: float = 0.001, errors: Optional[List[Exception]] = None):

    def add_error(message: str):
        error = IncorrectModelOutputException(
            message, item=value_name, incorrect_value=value, correct_value=correct_value
        )
        errors.append(error)
        print(error)

    if errors is None:
        errors = []

    if isinstance(value, list):
        return [
            _check_value(val, correct_val, value_name=f'{value_name}[{i}]', tolerance=tolerance, errors=errors)
            for i, (val, correct_val) in enumerate(zip(value, correct_value))
        ]


    if value is None:
        if correct_value is None:
            pass
        else:
            add_error(f'got None for {value_name}. Should be {correct_value}')
        return

    # Assumed to be float
    value = float(value)
    if abs(value - correct_value) > tolerance:
        add_error(f'got incorrect value {value} for {value_name}. Should be {correct_value}')


class IncorrectModelOutputException(Exception):

    def __init__(self, *args, item: Optional[str] = None, incorrect_value: Optional[float] = None,
                 correct_value: Optional[float] = None,
                 **kwargs):
        self.item = item
        self.incorrect_value = incorrect_value
        self.correct_value = correct_value
        super().__init__(*args, **kwargs)
