from rest_framework import generics
from .serializers import *
from projects.models import *

# View for listing TodoItems
class ListTodo(generics.ListAPIView):
    queryset = TodoItems.objects.all()  # Retrieve all instances of TodoItems model
    serializer_class = TodoSerializer  # Use TodoSerializer for serialization

# View for updating TodoItems
class UpdateTodo(generics.RetrieveUpdateAPIView):
    queryset = TodoItems.objects.all()  # Retrieve all instances of TodoItems model
    serializer_class = TodoSerializer  # Use TodoSerializer for serialization

# View for creating TodoItems
class CreateTodo(generics.CreateAPIView):
    queryset = TodoItems.objects.all()  # Retrieve all instances of TodoItems model
    serializer_class = TodoSerializer  # Use TodoSerializer for serialization

# View for deleting TodoItems
class DeleteTodo(generics.DestroyAPIView):
    queryset = TodoItems.objects.all()  # Retrieve all instances of TodoItems model
    serializer_class = TodoSerializer  # Use TodoSerializer for serialization
