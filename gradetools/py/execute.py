from typing import Optional
import papermill
from nbconvert import HTMLExporter
from IPython.display import HTML
from gradetools.py.extract import extract_cells_from_nb_node_return_nb_node
import tempfile


def execute_notebook_render_html(notebook_path: str,  parameters: dict, out_notebook_path: Optional[str] = None,
                                 slice_from: Optional[int] = None,
                                 slice_to: Optional[int] = None, slice_by: Optional[int] = None
                                 ) -> HTML:

    if out_notebook_path is None:
        f = tempfile.NamedTemporaryFile(mode='w', suffix='.ipynb')
        out_notebook_path = f.name
        close_file = True
    else:
        close_file = False

    nb_result = papermill.execute_notebook(
        notebook_path,
        out_notebook_path,
        parameters=parameters
    )

    if close_file:
        f.close()

    # Extract a portion of the result if necessary
    if any([sl is not None for sl in (slice_from, slice_to, slice_by)]):
        nb_result = extract_cells_from_nb_node_return_nb_node(
            nb_result,
            slice_from=slice_from,
            slice_to=slice_to,
            slice_by=slice_by
        )

    html_exporter = HTMLExporter()
    (body, resources) = html_exporter.from_notebook_node(nb_result)
    # TODO: what to do with resources? maybe HTML(body, metadata=resources)
    return HTML(body)
