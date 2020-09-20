import pyexlatex as pl
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg


def get_retirement_model_overview_frame():
    darker_green_def = pl.RGB(15, 82, 13, color_name='darkergreen')

    model_block_options = [
        'fill=darkergreen!60'
    ]

    model_sub_block_options = [
        'fill=darkergreen'
    ]

    text_options = [
        'text=white'
    ]

    model_node = lg.Rectangle(
        5, 8, offset=(1.25, 4), contents=pl.Bold('Model'), content_position='bottom', content_offset=0.2,
        shape_options=model_block_options, text_options=text_options
    )
    salary_node = lg.Rectangle(
        4, 1.75, offset=(1.25, 6.75), contents='Salary', shape_options=model_sub_block_options,
        text_options=text_options
    )
    wealth_node = lg.Rectangle(
        4, 1.75, offset=(1.25, 4.25), contents='Wealths', shape_options=model_sub_block_options,
        text_options=text_options
    )
    retirement_node = lg.Rectangle(
        4, 1.75, offset=(1.25, 1.75), contents='Retirement', shape_options=model_sub_block_options,
        text_options=text_options
    )

    return lp.GraphicFrame(
        [
            lg.TikZPicture([
                model_node,
                salary_node,
                wealth_node,
                retirement_node,
                lg.Arrow(salary_node, wealth_node),
                lg.Arrow(wealth_node, retirement_node)
            ])
        ],
        title='The Structure of the Retirement Model',
        pre_env_contents=darker_green_def
    )