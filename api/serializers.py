from rest_framework import serializers
from projects.models import TodoItems

# Serializer for the TodoItems model
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItems  # Specify the model to be serialized
        fields = '__all__'  # Include all fields of the model in the serialization

