from rest_framework import serializers
from .models import Rule

class RuleSerializer(serializers.ModelSerializer):
    """
    Serializer for the Rule model.

    This serializer handles the conversion between Rule model instances
    and JSON representation for API requests and responses.
    """
    
    class Meta:
        model = Rule                      # Specify the model to serialize
        fields = '__all__'                # Include all fields from the Rule model
