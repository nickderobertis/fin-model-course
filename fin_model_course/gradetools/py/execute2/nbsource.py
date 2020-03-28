from typing import List

from nbformat.notebooknode import NotebookNode
import nbformat


def source_from_notebook_path(notebook_path: str, remove_magics: bool = True) -> str:
    nb = nbformat.read(notebook_path, as_version=4)
    source = source_from_notebook_node(nb, remove_magics=remove_magics)
    return source


def _source_lines_from_notebook_node(nb_node: NotebookNode) -> List[str]:
    cells = _code_cells_from_notebook_note(nb_node)
    source_lines = []
    for cell in cells:
        source_lines.extend(
            _source_lines_from_notebook_cell(cell)
        )
    return source_lines


def source_from_notebook_node(nb_node: NotebookNode, remove_magics: bool = True) -> str:
    lines = _source_lines_from_notebook_node(nb_node)
    if remove_magics:
        lines = [line for line in lines if not line.startswith('%')]
    return '\n'.join(lines)


def _code_cells_from_notebook_note(nb_node: NotebookNode) -> List[NotebookNode]:
    return [cell for cell in nb_node['cells'] if cell['cell_type'] == 'code']


def _source_lines_from_notebook_cell(cell: NotebookNode) -> List[str]:
    return cell['source'].split('\n')
