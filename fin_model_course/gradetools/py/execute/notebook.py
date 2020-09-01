import os
import tempfile
from typing import Optional

import papermill
from IPython.core.display import HTML
from nbconvert import HTMLExporter

from gradetools.py.extract import extract_cells_from_nb_node_return_nb_node


def execute_notebook_render_html(notebook_path: str,  parameters: dict, out_notebook_path: Optional[str] = None,
                                 slice_from: Optional[int] = None,
                                 slice_to: Optional[int] = None, slice_by: Optional[int] = None,
                                 remove_input_cells: bool = False,
                                 ) -> HTML:

    if out_notebook_path is None:
        f = tempfile.NamedTemporaryFile(mode='w', suffix='.ipynb', delete=False)
        out_notebook_path = f.name
        f.close()
        delete_file = True
    else:
        delete_file = False

    nb_result = papermill.execute_notebook(
        notebook_path,
        out_notebook_path,
        parameters=parameters
    )

    if delete_file:
        os.remove(out_notebook_path)

    # Extract a portion of the result if necessary
    if any([sl is not None for sl in (slice_from, slice_to, slice_by)]):
        nb_result = extract_cells_from_nb_node_return_nb_node(
            nb_result,
            slice_from=slice_from,
            slice_to=slice_to,
            slice_by=slice_by,
            remove_input_cells=remove_input_cells
        )

    html_exporter = HTMLExporter()
    (body, resources) = html_exporter.from_notebook_node(nb_result)
    # TODO [#9]: what to do with resources? maybe HTML(body, metadata=resources)
    return HTML(body)