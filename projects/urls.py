from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage, name='index'),  # URL pattern for the index page
    path('createtask', views.createTask, name="create-task"),  # URL pattern for creating a task
    path('updatetask/<int:pk>/', views.updateTask, name="update-task"),  # URL pattern for updating a task
    path('deletetask/<int:pk>/', views.deleteTask, name="delete-task"),  # URL pattern for deleting a task
]

