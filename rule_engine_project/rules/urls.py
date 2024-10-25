from django.urls import path
from .views import CreateRuleView, EvaluateRuleView, api_view, GetAllRulesView

# URL patterns for the rule engine application
urlpatterns = [
    path(
        'create-rule/', 
        CreateRuleView.as_view(), 
        name='create_rule'  # Endpoint to create a new rule
    ),
    path(
        'evaluate-rule/', 
        EvaluateRuleView.as_view(), 
        name='evaluate_rule'  # Endpoint to evaluate an existing rule
    ),
    path(
        '', 
        api_view, 
        name='api_view'  # Endpoint to provide general API information
    ),
    path(
        'get-all-rules/', 
        GetAllRulesView.as_view(), 
        name='get-all-rules'  # Endpoint to retrieve all rules
    ),
]
