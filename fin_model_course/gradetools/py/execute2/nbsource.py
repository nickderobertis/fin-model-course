from typing import List

from nbformat.notebooknode import NotebookNode


def _source_lines_from_notebook_node(nb_node: NotebookNode) -> List[str]:
    cells = _code_cells_from_notebook_note(nb_node)
    source_lines = []
    for cell in cells:
        source_lines.extend(
            _source_lines_from_notebook_cell(cell)
        )
    return source_lines


def source_from_notebook_node(nb_node: NotebookNode) -> str:
    lines = _source_lines_from_notebook_node(nb_node)
    return '\n'.join(lines)


def _code_cells_from_notebook_note(nb_node: NotebookNode) -> List[NotebookNode]:
    return [cell for cell in nb_node['cells'] if cell['cell_type'] == 'code']


def _source_lines_from_notebook_cell(cell: NotebookNode) -> List[str]:
    return cell['source'].split('\n')
