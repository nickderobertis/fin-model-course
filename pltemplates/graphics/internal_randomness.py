from typing import List
import math
import pyexlatex.graphics as lg


NUM_MODEL_ROWS = 5
ALL_NODE_STYLE = [
    'rounded corners',
    'inner sep=10pt'
]


def internal_randomness_graphic() -> lg.TikZPicture:
    model_style = ['fill=orange!30'] + ALL_NODE_STYLE

    output_nodes = []
    input_node = lg.Node('Inputs', options=_io_style(2))
    model_node = lg.Node('Model', lg.Right(of=input_node), options=model_style)
    im_arrow = lg.Arrow(input_node, model_node)
    pic_contents = [
        input_node,
        model_node,
        im_arrow
    ]
    for i in range(NUM_MODEL_ROWS):
        if i == 2:
            output_position = lg.Right(of=model_node)
        elif i == 0:
            output_position = lg.Right(lg.Above(of=model_node))
        else:
            output_position = lg.Below(of=output_node)  # below last output node

        output_node = lg.Node('Outputs', output_position, options=_io_style(i))
        output_nodes.append(output_node)

        mo_arrow = lg.Arrow(model_node, output_node)
        pic_contents.extend([
            output_node,
            mo_arrow
        ])
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