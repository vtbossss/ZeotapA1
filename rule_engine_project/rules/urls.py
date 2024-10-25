from django.urls import path
from .views import CreateRuleView, EvaluateRuleView,api_view

urlpatterns = [
    path('create-rule/', CreateRuleView.as_view(), name='create_rule'),
    path('evaluate-rule/', EvaluateRuleView.as_view(), name='evaluate_rule'),
    path('',api_view,name='api_view'),
]
