from django.db import models

class Rule(models.Model):
    """
    Model representing a rule in the rule engine.

    Attributes:
    - rule_name: The name of the rule.
    - ast_structure: The Abstract Syntax Tree (AST) structure represented as JSON.
    - created_at: Timestamp indicating when the rule was created.
    - modified_at: Timestamp indicating when the rule was last modified.
    """
    
    rule_name = models.CharField(max_length=255)  # Name of the rule
    ast_structure = models.JSONField()              # JSON field to store the AST structure
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when the rule is created
    modified_at = models.DateTimeField(auto_now=True)      # Automatically update the timestamp when the rule is modified

    def __str__(self):
        """
        String representation of the Rule instance.

        Returns:
        The name of the rule.
        """
        return self.rule_name  # Return the rule name for easy identification
