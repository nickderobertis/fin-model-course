import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll


def get_dcf_graphic(include_output: bool = True, include_fcf: bool = True, include_coc: bool = True) -> lg.TikZPicture:
    all_node_options = [
        'inner sep=10pt',
        'rounded corners'
    ]

    model_node_options = all_node_options + [
        'fill=blue',
        'text=white'
    ]

    output_node_options = all_node_options + [
        'fill=green'
    ]

    input_node_options = all_node_options + [
        'fill=orange!60'
    ]


    all_nodes = []
    all_arrows = []

    if include_output:
        stock_value_node = lg.Node('Stock Value', options=output_node_options)

        value_node = lg.Node('Enterprise Value', location=lg.Above(of=stock_value_node), options=output_node_options)
        all_nodes.extend([stock_value_node, value_node])
        all_arrows.append(lg.Arrow(value_node, stock_value_node))

    if include_fcf:
        if not include_output:
            output_loc = None
        else:
            output_loc = lg.Above(lg.Right(of=value_node, by=0.1))

        fcf_node = lg.Node('Free Cash Flows', location=output_loc, options=model_node_options)
        historical_financials_node = lg.Node('Historical Financial Statements',
                                             location=lg.Above(lg.Right(of=fcf_node, by=0.1)),
                                             options=input_node_options)
        projections_node = lg.Node('Analyst Projections', location=lg.Above(lg.Left(of=fcf_node, by=0.1)),
                                   options=input_node_options)
        all_nodes.extend([fcf_node, historical_financials_node, projections_node])
        if include_output:
            all_arrows.append(lg.Arrow(fcf_node, value_node))
        all_arrows.extend([
            lg.Arrow(historical_financials_node, fcf_node),
            lg.Arrow(projections_node, fcf_node),
        ])

    if include_coc:
        if not include_output:
            output_loc = None
        else:
            output_loc = lg.Above(lg.Left(of=value_node, by=0.1))


        cost_of_capital_node = lg.Node('Cost of Capital', location=output_loc,
                                   options=model_node_options)
        debt_node = lg.Node('Current Debt Schedule', location=lg.Left(of=cost_of_capital_node), options=input_node_options)
        prices_node = lg.Node('Historical Stock Prices', location=lg.Above(lg.Left(of=cost_of_capital_node, by=0.1)),
                              options=input_node_options)
        all_nodes.extend([cost_of_capital_node, debt_node, prices_node])
        if include_output:
            all_arrows.append(lg.Arrow(cost_of_capital_node, value_node))
        all_arrows.extend([
            lg.Arrow(debt_node, cost_of_capital_node),
            lg.Arrow(prices_node, cost_of_capital_node),
        ])

    return lg.TikZPicture(
            [
                *all_nodes,
                *all_arrows
            ]
        )
