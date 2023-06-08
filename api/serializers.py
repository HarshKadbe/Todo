from rest_framework import serializers
from projects.models import TodoItems

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TodoItems
        fields = '__all__'