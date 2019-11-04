import pyexlatex as pl
import pyexlatex.table as lt
import pyexlatex.presentation as lp
import pyexlatex.graphics as lg
import pyexlatex.layouts as ll


def get_dcf_overview_graphic() -> lg.TikZPicture:
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

    stock_value_node = lg.Node('Stock Value', options=output_node_options)

    value_node = lg.Node('Enterprise Value', location=lg.Above(of=stock_value_node), options=output_node_options)

    fcf_node = lg.Node('Free Cash Flows', location=lg.Above(lg.Right(of=value_node, by=0.1)), options=model_node_options)
    cost_of_capital_node = lg.Node('Cost of Capital', location=lg.Above(lg.Left(of=value_node, by=0.1)),
                                   options=model_node_options)

    historical_financials_node = lg.Node('Historical Financial Statements',
                                         location=lg.Above(lg.Right(of=fcf_node, by=0.1)), options=input_node_options)
    projections_node = lg.Node('Analyst Projections', location=lg.Above(lg.Left(of=fcf_node, by=0.1)),
                               options=input_node_options)

    debt_node = lg.Node('Current Debt Schedule', location=lg.Left(of=cost_of_capital_node), options=input_node_options)
    prices_node = lg.Node('Historical Stock Prices', location=lg.Above(lg.Left(of=cost_of_capital_node, by=0.1)),
                          options=input_node_options)

    return lg.TikZPicture(
            [
                stock_value_node,
                value_node,
                fcf_node,
                cost_of_capital_node,
                historical_financials_node,
                projections_node,
                debt_node,
                prices_node,
                lg.Arrow(cost_of_capital_node, value_node),
                lg.Arrow(fcf_node, value_node),
                lg.Arrow(historical_financials_node, fcf_node),
                lg.Arrow(projections_node, fcf_node),
                lg.Arrow(debt_node, cost_of_capital_node),
                lg.Arrow(prices_node, cost_of_capital_node),
                lg.Arrow(value_node, stock_value_node),
            ]
        )
