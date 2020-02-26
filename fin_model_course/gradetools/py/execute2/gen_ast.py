import ast


def create_ast_function_call_with_numeric_values(func_name: str, **kwargs):
    """
    Creates an ast call for function name with passed numeric keyword arguments.

    :Notes:

    Will not work if a non-numeric keyword value is passed.

    :Examples:

        >>> import astor
        >>> value = create_ast_function_call_with_numeric_values('ModelInputs', n_phones=100, price_scrap=200)
        >>> astor.to_source(value)
        'ModelInputs(n_phones=100, price_scrap=200)\n'
    """
    ast_keywords = [
        ast.keyword(
            arg=kwarg_name,
            value=ast.Num(kwarg_value)
        )
        for kwarg_name, kwarg_value in kwargs.items()
    ]
    call = ast.Call(
        func=ast.Name(func_name),
        args=[],
        keywords=ast_keywords
    )
    return call
