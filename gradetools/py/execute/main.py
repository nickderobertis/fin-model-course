from typing import Optional, Dict, Sequence, Any, Tuple
import os
from IPython.core.display import HTML
from IPython.display import display, clear_output
import pandas as pd
from gradetools.py.execute.notebook import execute_notebook_render_html
from gradetools.py.execute.inputs import get_params_dict_from_values_dict_and_possible_names_dict

CASES_RUN = {}
INCORRECT_CASES = {}

def execute_notebooks_by_config(notebook_slice_configs: Dict[str, Tuple[Optional[int], Optional[int]]],
                                notebook_folder: str,
                                all_params: Sequence[Dict[str, Any]], all_outputs: Sequence[Dict[str, Any]],
                                possible_names_dict: Optional[Dict[str, Sequence[str]]] = None,
                                remove_input_cells: bool = False,
                                report_out_path: Optional[str] = None, wipe_globals: bool = False
                                ) -> pd.DataFrame:
    global CASES_RUN
    global INCORRECT_CASES
    if not CASES_RUN or wipe_globals:
        CASES_RUN = {notebook_name: [] for notebook_name in notebook_slice_configs}
    if not INCORRECT_CASES or wipe_globals:
        INCORRECT_CASES = {notebook_name: [] for notebook_name in notebook_slice_configs}
    for i, input_case in enumerate(all_params):
        case_num = i + 1
        for notebook_name, slice_config in notebook_slice_configs.items():
            if (case_num) in CASES_RUN[notebook_name]:
                print(f'Skipping {notebook_name} case {case_num}')
                continue
            clear_output()
            notebook_path = os.path.join(notebook_folder, notebook_name)
            display(
                execute_notebook_render_html_with_all_possible_input_names(
                    notebook_path,
                    input_case,
                    possible_names_dict=possible_names_dict,
                    slice_from=slice_config[0],
                    slice_to=slice_config[1],
                    remove_input_cells=remove_input_cells
                )
            )
            print(f'Grading {notebook_name} case {case_num}')
            print(f'Correct output: {all_outputs[i]}')
            raw_accurate_int = input('Accurate? 1 for yes, 0 for no:')
            is_accurate = bool(int(raw_accurate_int))
            if not is_accurate:
                INCORRECT_CASES[notebook_name].append(i + 1)
            CASES_RUN[notebook_name].append(i + 1)

    df = pd.DataFrame(pd.Series(INCORRECT_CASES)).rename(columns={0: 'Problem Cases'})

    if report_out_path:
        df.to_csv(report_out_path)

    return df






def execute_notebook_render_html_with_all_possible_input_names(notebook_path: str,  parameters: Dict[str, Any],
                                                               possible_names_dict: Optional[Dict[str, Sequence[str]]] = None,
                                                               out_notebook_path: Optional[str] = None,
                                                               slice_from: Optional[int] = None,
                                                               slice_to: Optional[int] = None,
                                                               slice_by: Optional[int] = None,
                                                               remove_input_cells: bool = False,
                                                               ) -> HTML:
    if possible_names_dict:
        parameters = get_params_dict_from_values_dict_and_possible_names_dict(parameters, possible_names_dict)

    return execute_notebook_render_html(
        notebook_path,
        parameters,
        out_notebook_path=out_notebook_path,
        slice_from=slice_from,
        slice_to=slice_to,
        slice_by=slice_by,
        remove_input_cells=remove_input_cells
    )

