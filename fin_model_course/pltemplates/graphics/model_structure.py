import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll


def get_model_structure_graphic() -> lg.TikZPicture:
    inputs_block_options = [
        'fill=orange!30'
    ]

    model_block_options = [
        'fill=blue!50'
    ]

    sub_model_block_options = [
        'fill=blue!90'
    ]

    step_block_options = [
        'fill=cyan!20'
    ]

    outputs_block_options = [
        'fill=green!20'
    ]

    text_options = [
        'text=white'
    ]

    step_text_options = [
        'text=black'
    ]

    inputs_text_options = outputs_text_options = step_text_options

    arrow_options = [
        'line width=0.75mm',
    ]

    inputs_rectangle = lg.Rectangle(2, 8, offset=(-3.35, 4), contents=pl.Bold('Inputs'),
                                    shape_options=inputs_block_options,
                                    text_options=inputs_text_options)

    model_rectangle = lg.Rectangle(5, 8, offset=(1.25, 4), contents=pl.Bold('Model'), content_position='bottom',
                                   content_offset=0.2, shape_options=model_block_options,
                                   text_options=text_options)

    outputs_rectangle = lg.Rectangle(2, 8, offset=(5.85, 4), contents=pl.Bold('Outputs'),
                                     shape_options=outputs_block_options,
                                     text_options=outputs_text_options)

    sub_model_rectangles = []
    step_rectangles = []
    for i in range(3):
        y_offset = 1.75 + i * 2.5
        sub_model_rectangles.append(
            lg.Rectangle(4, 1.75, offset=(1.25, y_offset), contents='Sub-Model',
                         shape_options=sub_model_block_options, text_options=text_options,
                         content_position='bottom'),
        )
        for j in range(3):
            x_offset = j * 1.25
            step_rectangles.append(
                lg.Rectangle(1.1, 1, offset=(x_offset, y_offset + 0.2), contents='Step',
                             shape_options=step_block_options, text_options=step_text_options,
                             )
            )

    arrows = [
        lg.Arrow((-2.3, 4), (-1.3, 4), options=arrow_options),
        lg.Arrow((3.8, 4), (4.8, 4), options=arrow_options),
    ]

    return lg.TikZPicture([
        inputs_rectangle,
        model_rectangle,
        *sub_model_rectangles,
        *step_rectangles,
        outputs_rectangle,
        *arrows,
    ])
