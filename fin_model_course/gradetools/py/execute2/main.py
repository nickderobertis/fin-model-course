from dataclasses import dataclass
from typing import Optional, Sequence, Union, Dict, Any

import nbformat

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