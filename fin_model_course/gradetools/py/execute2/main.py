import os
from dataclasses import dataclass
from typing import Optional, Sequence, Union, Dict, Any

import pandas as pd

from gradetools.case_config import CaseConfig
from gradetools.py.execute2.compare import values_are_same, CannotCompareOutputsException
from gradetools.py.execute2.gen_ast import create_ast_function_call_with_numeric_values
from gradetools.py.execute2.insert import insert_lines_in_source, InsertConfig
from gradetools.py.execute2.nbsource import source_from_notebook_path
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
    inserts: Optional[Sequence[InsertConfig]] = None,
    suppress_output: bool = False,
    remove_magics: bool = True
) -> Dict[str, Any]:
    source = source_from_notebook_path(notebook_path, remove_magics=remove_magics)
    if inserts is not None:
        source = insert_lines_in_source(source, inserts)
    if replacements is not None:
        for config in replacements:
            source = replace_in_source(source, config.assign_name, config.ast_call)
    globs = run_source_extract_globals(source, suppress_output=suppress_output)
    return globs


def execute_notebooks_by_config(notebook_folder: str, case_configs: Sequence[CaseConfig],
                                all_outputs: Sequence[Dict[str, Any]],
                                report_out_path: Optional[str] = None) -> pd.DataFrame:
    """

    :Examples:
        from gradetools.py.execute2.main import execute_notebooks_by_config
        from gradetools.project_1.cases import OUTPUT_CASES, INPUT_CASE_CONFIGS

        execute_notebooks_by_config(
            'Scratch',
            INPUT_CASE_CONFIGS,
            OUTPUT_CASES,
            'report.csv',
        )
    """
    notebooks = [file for file in next(os.walk(notebook_folder))[2] if file.casefold().endswith('ipynb')]
    noteboook_paths = [os.path.join(notebook_folder, nb) for nb in notebooks]
    out_cols = [
        'Notebook Name',
        'Case Number',
        'Case Name',
        'Successful Run',
        'Exception',
    ]
    out_cols += list(all_outputs[0].keys())
    notebook_case_report_values = []
    for nb_path in noteboook_paths:
        print(f'Evaluating notebook {nb_path}')
        for i, (input_config, outputs) in enumerate(zip(case_configs, all_outputs)):
            inputs = input_config.input_dict
            name = input_config.case_name
            case_num = i + 1
            print(f'Running case {case_num}: {name}')
            rc = ReplacementConfig('model_data', 'ModelInputs', kwargs=inputs)
            successful_run = True
            exc = None
            try:
                globs = read_notebook_and_run_extracting_globals(nb_path, [rc], suppress_output=True)
            except Exception as e:
                exc = str(e)
                successful_run = False
            if not successful_run:
                print(f'Could not run case {case_num}')
                report_values = (nb_path, case_num, name, successful_run, exc) + tuple([False for _ in outputs])
                notebook_case_report_values.append(report_values)
                continue

            outputs_correct = []
            for out_name, out_value in outputs.items():
                try:
                    same = values_are_same(globs[out_name], out_value, input_config.tolerances[out_name])
                except CannotCompareOutputsException as e:
                    exc = str(e)
                    same = False
                outputs_correct.append(same)
            report_values = (nb_path, case_num, name, successful_run, exc) + tuple(outputs_correct)
            notebook_case_report_values.append(report_values)
    df = pd.DataFrame(notebook_case_report_values, columns=out_cols)
    if report_out_path:
        df.to_csv(report_out_path, index=False)
    return df


