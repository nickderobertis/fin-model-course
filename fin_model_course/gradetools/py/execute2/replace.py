import ast
import astor


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
        main_target = node.targets[0]
        if hasattr(main_target, 'id') and main_target.id == self.target_assign_name:
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
