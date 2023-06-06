from django.db import models
from django.utils import timezone

# Create a function to calculate the default due date, one week from the current time
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

# Create a table of TodoItems in the database
class TodoItems(models.Model):
    title = models.CharField(max_length=80)  # Title of the table
    description = models.TextField(max_length=200)  # Description of the table
    created_on = models.DateTimeField(auto_now_add=True)  # Automatically set the created_on field to the current time when an object is created
    due_date = models.DateTimeField(default=one_week_hence)  # Set the default value for the due_date field to one week from the current time

    def __str__(self):
        return self.title
