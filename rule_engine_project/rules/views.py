from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rule
from .serializers import RuleSerializer
from .utils import create_rule, evaluate_rule
from .ast_helper import Node

class CreateRuleView(APIView):
    """Handles creation of rules."""

    def post(self, request):
        """Creates a new rule based on the provided rule string and name.
        
        Args:
            request: The request object containing the rule data.

        Returns:
            Response: The response object with the created rule or an error message.
        """
        rule_string = request.data.get('rule_string')
        rule_name = request.data.get('rule_name')
        
        if not rule_string or not rule_name:
            return Response({"error": "Rule string and rule name are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure proper quoting in the rule string
        rule_string = rule_string.replace("'", "\"")  # Converts single quotes to double quotes for safety

        try:
            ast_structure = create_rule(rule_string).to_dict()
            rule = Rule.objects.create(rule_name=rule_name, ast_structure=ast_structure)
            return Response(RuleSerializer(rule).data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class EvaluateRuleView(APIView):
    """Handles evaluation of existing rules."""

    def post(self, request):
        """Evaluates a rule based on the provided user data.
        
        Args:
            request: The request object containing the rule ID and user data.

        Returns:
            Response: The response object with the evaluation result or an error message.
        """
        rule_id = request.data.get('rule_id')
        user_data = request.data.get('user_data')
        
        if not rule_id or not user_data:
            return Response({"error": "Rule ID and user data are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            rule = Rule.objects.get(id=rule_id)
            ast_structure_dict = rule.ast_structure
            
            # Reconstruct the AST Node from the dictionary
            ast_structure = reconstruct_node(ast_structure_dict)
            result = evaluate_rule(ast_structure, user_data)
            return Response({"result": result})
        except Rule.DoesNotExist:
            return Response({"error": "Rule not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def reconstruct_node(node_dict):
    """Reconstructs the Node from a dictionary representation.
    
    Args:
        node_dict (dict): The dictionary representation of a node.

    Returns:
        Node: The reconstructed Node or None for unsupported types.
    """
    node_type = node_dict.get('node_type')
    
    if node_type == 'operator':
        left = reconstruct_node(node_dict['left'])
        right = reconstruct_node(node_dict['right'])
        operator = node_dict['value']
        return Node(node_type, left, right, operator)
    
    elif node_type == 'operand':
        value = node_dict['value']
        return Node(node_type, value=value)
    
    return None  # Handle unsupported types or errors

def api_view(request):
    """Renders the API documentation page."""
    return render(request, 'api.html')

def home_view(request):
    """Renders the home page."""
    return render(request, 'index.html')


class GetAllRulesView(APIView):
    """Handles retrieval of all rules."""

    def get(self, request):
        """Retrieves all existing rules.
        
        Args:
            request: The request object.

        Returns:
            Response: The response object with all rules or an error message.
        """
        rules = Rule.objects.all()  # Get all rules
        serializer = RuleSerializer(rules, many=True)  # Serialize the rules
        return Response(serializer.data, status=status.HTTP_200_OK)
