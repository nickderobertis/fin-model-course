from typing import Optional, Union, List
from copy import deepcopy
import nbformat


def extract_cells_from_nb_node_return_nb_node(nb_node: nbformat.NotebookNode, slice_from: Optional[int] = None,
                                              slice_to: Optional[int] = None, slice_by: Optional[int] = None,
                                              remove_input_cells: bool = False,
                                              ) -> nbformat.NotebookNode:
    sl = slice(slice_from, slice_to, slice_by)
    cells = nb_node['cells'][sl]

    if remove_input_cells:
        cells = _remove_cell_inputs_leaving_outputs(cells)

    new_nb_node = _nb_node_from_nb_node_and_cells(nb_node, cells)
    return new_nb_node


def _nb_node_from_nb_node_and_cells(nb_node: nbformat.NotebookNode,
                                    cells: Union[nbformat.NotebookNode, List[nbformat.NotebookNode]]
                                    ) -> nbformat.NotebookNode:

    if not isinstance(cells, list):
        cells = [cells]

    # get other data from original notebook
    nb_dict = dict(
        cells=cells,
        metadata=nb_node['metadata'],
        nbformat=nb_node['nbformat'],
        nbformat_minor=nb_node['nbformat_minor']
    )

    nbformat.validate(nb_dict)
    small_nb = nbformat.from_dict(nb_dict)
    return small_nb


def _remove_cell_inputs_leaving_outputs(cells: Union[nbformat.NotebookNode, List[nbformat.NotebookNode]]):
    if not isinstance(cells, list):
        cells = [cells]

    out_cells = []
    for cell in cells:
        out_cell = deepcopy(cell)
        out_cell['source'] = ''
        out_cells.append(out_cell)

    return out_cells