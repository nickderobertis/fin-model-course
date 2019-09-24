import papermill
from nbconvert import HTMLExporter
from IPython.display import HTML


def execute_notebook_render_html(notebook_path: str, out_notebook_path: str, parameters: dict) -> HTML:
    nb_result = papermill.execute_notebook(
        notebook_path,
        out_notebook_path,
        parameters=parameters
    )
    html_exporter = HTMLExporter()
    (body, resources) = html_exporter.from_notebook_node(nb_result)
    # TODO: what to do with resources? maybe HTML(body, metadata=resources)
    return HTML(body)