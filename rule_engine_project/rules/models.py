from django.db import models


class Rule(models.Model):
    rule_name = models.CharField(max_length=255)
    ast_structure = models.JSONField()  # JSON field to store the AST
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rule_name
