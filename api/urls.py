from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('<str:pk>/', UpdateTodo.as_view()),  # URL pattern for updating a todo item
    path('', ListTodo.as_view()),  # URL pattern for retrieving a list of todo items
    path('create/', CreateTodo.as_view()),  # URL pattern for creating a new todo item
    path('delete/<str:pk>', DeleteTodo.as_view())  # URL pattern for deleting a todo item
]

