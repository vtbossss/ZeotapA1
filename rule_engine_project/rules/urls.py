from django.urls import path
from .views import CreateRuleView, EvaluateRuleView,api_view,GetAllRulesView

urlpatterns = [
    path('create-rule/', CreateRuleView.as_view(), name='create_rule'),
    path('evaluate-rule/', EvaluateRuleView.as_view(), name='evaluate_rule'),
    path('',api_view,name='api_view'),
    path('get-all-rules/', GetAllRulesView.as_view(), name='get-all-rules'),
]
