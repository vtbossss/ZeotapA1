import ast
import logging
from .ast_helper import Node

# Initialize the logger for this module
logger = logging.getLogger(__name__)

def create_rule(rule_string):
    """Parses the rule string and builds an AST representation.
    
    Args:
        rule_string (str): The rule condition as a string.

    Returns:
        Node: The root node of the AST representing the rule.
    """
    parsed_expr = ast.parse(rule_string, mode='eval').body
    return build_ast(parsed_expr)

def build_ast(expr):
    """Recursively builds an AST from the parsed expression.
    
    Args:
        expr: The parsed expression.

    Returns:
        Node: The corresponding AST node.
    """
    if isinstance(expr, ast.BoolOp):  # Handle AND/OR operations
        left = build_ast(expr.values[0])
        right = build_ast(expr.values[1])
        operator = 'AND' if isinstance(expr.op, ast.And) else 'OR'
        return Node('operator', left, right, operator)

    elif isinstance(expr, ast.Compare):  # Handle comparisons
        left = expr.left.id  # Assuming left is always an identifier
        op = get_operator_string(expr.ops[0])
        
        # Handle right-side comparison values properly
        if isinstance(expr.comparators[0], ast.Constant):
            right = expr.comparators[0].value  # Use .value for both numbers and strings
            if isinstance(right, str):
                right = f"'{right}'"  # Wrap strings in single quotes
        else:
            right = expr.comparators[0].id  # In case of an identifier
        
        # Construct the comparison expression
        condition = f"{left} {op} {right}"
        return Node('operand', value=condition)

    # Log a warning for unsupported expression types
    logger.warning(f"Unsupported expression type: {type(expr)}")
    return None  # Return None for unsupported types

def get_operator_string(op):
    """Maps AST comparison operators to their string equivalents.
    
    Args:
        op: The operator from the AST.

    Returns:
        str: The string representation of the operator.

    Raises:
        ValueError: If the operator is unsupported.
    """
    if isinstance(op, ast.Eq):
        return "=="
    elif isinstance(op, ast.NotEq):
        return "!="
    elif isinstance(op, ast.Lt):
        return "<"
    elif isinstance(op, ast.LtE):
        return "<="
    elif isinstance(op, ast.Gt):
        return ">"
    elif isinstance(op, ast.GtE):
        return ">="
    else:
        raise ValueError("Unsupported comparison operator")

def evaluate_rule(ast_node, data):
    """Evaluates the AST node based on user data.
    
    Args:
        ast_node (Node): The AST node to evaluate.
        data (dict): The user data for evaluation.

    Returns:
        bool: The result of the evaluation.
    """
    if ast_node.node_type == 'operator':
        left_eval = evaluate_rule(ast_node.left, data)
        right_eval = evaluate_rule(ast_node.right, data)
        if ast_node.value == 'AND':
            return left_eval and right_eval
        elif ast_node.value == 'OR':
            return left_eval or right_eval
    
    elif ast_node.node_type == 'operand':
        condition = ast_node.value
        try:
            # Ensure the eval statement is safe
            return eval(condition, {}, data)
        except KeyError as e:
            print(f"KeyError: {e} - Missing key in user data")
            return False  # Return False for any missing keys
        except Exception as e:
            print(f"Error evaluating condition '{condition}': {e}")
            return False

def safe_eval(condition, data):
    """Safely evaluates a condition using provided data.
    
    Args:
        condition (str): The condition to evaluate.
        data (dict): The user data for evaluation.

    Returns:
        bool: The result of the evaluation, or False on failure.
    """
    try:
        # Create a local environment with the data
        local_env = {key: value for key, value in data.items() if key.isidentifier()}
        return eval(condition, {"__builtins__": None}, local_env)
    except Exception as e:
        logger.error(f"Safe eval failed for condition '{condition}': {e}")
        return False

def combine_rules(rules):
    """Combines multiple AST nodes into a single AST.
    
    Args:
        rules (list): List of AST nodes to combine.

    Returns:
        Node: The combined AST node, or None if no rules are provided.
    """
    if not rules:
        return None

    combined_ast = rules[0]
    for rule_ast in rules[1:]:
        combined_ast = Node('operator', combined_ast, rule_ast, 'AND')
    return combined_ast
