import os
import tempfile
from typing import Dict, Any

import nbformat
import runpy

from gradetools.py.execute2.nbsource import source_from_notebook_node
from gradetools.py.execute2.output import suppress_stdout


def run_source_extract_globals(source: str, suppress_output: bool = False) -> Dict[str, Any]:
    f = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
    f.write(source)
    f.close()
    if suppress_output:
        with suppress_stdout():
            globs = runpy.run_path(f.name)
    else:
        globs = runpy.run_path(f.name)
    os.remove(f.name)
    return globs


def run_notebook_extract_globals(notebook_path: str, suppress_output: bool = False) -> Dict[str, Any]:
    nb = nbformat.read(notebook_path, as_version=4)
    source = source_from_notebook_node(nb)
    globs = run_source_extract_globals(source, suppress_output=suppress_output)
    return globs