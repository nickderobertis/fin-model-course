from typing import List
import math
import pyexlatex.graphics as lg


NUM_MODEL_ROWS = 5
ALL_NODE_STYLE = [
    'rounded corners',
    'inner sep=10pt'
]


def explore_parameters_graphic() -> lg.TikZPicture:
    model_style = ['fill=orange!30'] + ALL_NODE_STYLE

    prior_input = None
    pic_contents = []
    output_nodes = []
    for i in range(NUM_MODEL_ROWS):
        if prior_input is None:
            input_position = None
        else:
            input_position = lg.Below(of=prior_input)
        input_node = lg.Node('Inputs', input_position, options=_io_style(i))
        model_node = lg.Node('Model', lg.Right(of=input_node), options=model_style)
        output_node = lg.Node('Outputs', lg.Right(of=model_node), options=_io_style(i))
        output_nodes.append(output_node)
        im_arrow = lg.Arrow(input_node, model_node)
        mo_arrow = lg.Arrow(model_node, output_node)
        pic_contents.extend([
            input_node,
            model_node,
            output_node,
            im_arrow,
            mo_arrow
        ])
        prior_input = input_node
    visualize_index = math.floor(NUM_MODEL_ROWS / 2)
    visualize_node = lg.Node('Visualization', lg.Right(of=output_nodes[visualize_index]), options=model_style)
    visualize_arrows = [lg.Arrow(out_node, visualize_node) for out_node in output_nodes]
    pic_contents.append(visualize_node)
    pic_contents.extend(visualize_arrows)
    tp = lg.TikZPicture(pic_contents)
    return tp


def _io_style(i: int) -> List[str]:
    fill_opacity = min((i + 2) * 15, 100)
    return [f'fill=green!{fill_opacity}'] + ALL_NODE_STYLE