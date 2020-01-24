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
    middle_index = math.floor(NUM_MODEL_ROWS / 2)

    output_nodes = []
    pic_contents = []
    for i in range(NUM_MODEL_ROWS):
        if i == 0:
            output_position = None
        else:
            output_position = lg.Below(of=output_node)  # below last output node

        output_node = lg.Node('Outputs', output_position, options=_io_style(i))
        output_nodes.append(output_node)
        pic_contents.append(output_node)

    center_output = output_nodes[middle_index]
    model_node = lg.Node('Model', lg.Left(of=center_output), options=model_style)
    input_node = lg.Node('Inputs', lg.Left(of=model_node), options=_io_style(middle_index))

    im_arrow = lg.Arrow(input_node, model_node)
    output_arrows = [lg.Arrow(model_node, out_node) for out_node in output_nodes]
    pic_contents.extend([
        model_node,
        input_node,
        im_arrow,
        *output_arrows
    ])

    tp = lg.TikZPicture(pic_contents)
    return tp


def _io_style(i: int) -> List[str]:
    fill_opacity = min((i + 2) * 15, 100)
    return [f'fill=green!{fill_opacity}'] + ALL_NODE_STYLE