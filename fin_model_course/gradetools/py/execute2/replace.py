import ast
import astor

# TEMP - test script
"""
from gradetools.py.execute2.replace import replace_in_source
from gradetools.py.execute2.nbsource import source_from_notebook_node
from gradetools.py.execute2.gen_ast import create_ast_function_call_with_numeric_values
import nbformat
import ast

value = create_ast_function_call_with_numeric_values('ModelInputs', n_phones=100, price_scrap=200)
nb = nbformat.read(notebook_path, as_version=4)
source = source_from_notebook_node(nb)
new_source = replace_in_source(source, 'model_data', value)
print(new_source)
"""


def replace_in_source(source: str, target_assign_name: str, replace_with: ast.AST):
    mod = ast.parse(source)
    aar = AstAssignReplacer(target_assign_name, replace_with)
    new_mod = aar.visit(mod)
    return astor.to_source(new_mod)


class AstAssignReplacer(ast.NodeTransformer):

    def __init__(self, target_assign_name: str, replace_with):
        self.target_assign_name = target_assign_name
        self.replace_with = replace_with

    def visit_Assign(self, node: ast.Assign):
        if node.targets[0] == self.target_assign_name:
            # Got the targeted assign, replace
            return ast.copy_location(
                ast.Assign(
                    targets=[ast.Name(self.target_assign_name)],
                    value=self.replace_with
                ),
                node
            )

        # not the correct assign, default behavior
        self.generic_visit(node)
        return node
