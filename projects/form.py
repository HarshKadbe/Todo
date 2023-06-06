from django.forms import ModelForm
from .models import TodoItems
from django import forms

class TodoItemForm(ModelForm):
    class Meta:
        model = TodoItems
        fields = ['title', 'description', 'due_date']