from typing import Dict, Any, Sequence


def get_params_dict_from_values_dict_and_possible_names_dict(values_dict: Dict[str, Any],
                                                             possible_names_dict: Dict[str, Sequence[str]]):
    """
    Gets a dictionary of parameters including all the possible names of each parameter

    :param values_dict: keys are names of inputs and values are values of those inputs
    :param possible_names_dict: keys are names of inputs and values are lists of possible other names for those inputs
    :return:
    """

    params = {}
    for var_key, possible_names in possible_names_dict.items():
        for name in possible_names:
            params[name] = values_dict[var_key]
    return params