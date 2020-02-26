import os
from dataclasses import dataclass
from typing import Optional, Sequence, Union, Dict, Any

import nbformat
import pandas as pd

from gradetools.py.execute2.gen_ast import create_ast_function_call_with_numeric_values
from gradetools.py.execute2.nbsource import source_from_notebook_node
from gradetools.py.execute2.replace import replace_in_source
from gradetools.py.execute2.run import run_source_extract_globals


@dataclass
class ReplacementConfig:
    assign_name: str
    function_name: str
    kwargs: Dict[str, Union[int, float]]

    def __post_init__(self):
        self.ast_call = create_ast_function_call_with_numeric_values(self.function_name, **self.kwargs)


def read_notebook_and_run_extracting_globals(
    notebook_path: str,
    replacements: Optional[Sequence[ReplacementConfig]] = None,
    suppress_output: bool = False
) -> Dict[str, Any]:
    nb = nbformat.read(notebook_path, as_version=4)
    source = source_from_notebook_node(nb)
    if replacements is not None:
        for config in replacements:
            source = replace_in_source(source, config.assign_name, config.ast_call)
    globs = run_source_extract_globals(source, suppress_output=suppress_output)
    return globs


def execute_notebooks_by_config(notebook_folder: str,
                                all_params: Sequence[Dict[str, Any]], all_outputs: Sequence[Dict[str, Any]],
                                report_out_path: Optional[str] = None) -> pd.DataFrame:
    """

    :Examples:
        from gradetools.py.execute2.main import execute_notebooks_by_config
        from gradetools.project_1.cases import OUTPUT_CASES, INPUT_CASES

        execute_notebooks_by_config(
            'Scratch',
            INPUT_CASES,
            OUTPUT_CASES,
            'report.csv',
        )
    """
    notebooks = [file for file in next(os.walk(notebook_folder))[2] if file.casefold().endswith('ipynb')]
    noteboook_paths = [os.path.join(notebook_folder, nb) for nb in notebooks]
    out_cols = [
        'Notebook Name',
        'Case Number',
        'Successful Run',
        'Exception',
    ]
    out_cols += list(all_outputs[0].keys())
    notebook_case_report_values = []
    for nb_path in noteboook_paths:
        for i, (inputs, outputs) in enumerate(zip(all_params, all_outputs)):
            rc = ReplacementConfig('model_data', 'ModelInputs', kwargs=inputs)
            successful_run = True
            exc = None
            try:
                globs = read_notebook_and_run_extracting_globals(nb_path, [rc], suppress_output=True)
            except Exception as e:
                exc = str(e)
                successful_run = False
            if not successful_run:
                report_values = (nb_path, i, successful_run, exc) + tuple([False for _ in outputs])
                notebook_case_report_values.append(report_values)
                continue

            outputs_correct = []
            for out_name, out_value in outputs.items():
                outputs_correct.append(
                    globs[out_name] == out_value
                )
            report_values = (nb_path, i, successful_run, exc) + tuple(outputs_correct)
            notebook_case_report_values.append(report_values)
    df = pd.DataFrame(notebook_case_report_values, columns=out_cols)
    if report_out_path:
        df.to_csv(report_out_path, index=False)
    return df

