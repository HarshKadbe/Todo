from django.shortcuts import render, redirect
from .models import TodoItems
from .form import TodoItemForm

# View for rendering the index page
def IndexPage(request):
    projectObj = TodoItems.objects.all()  # Retrieve all instances of TodoItems
    context = {'projectObj': projectObj}  # Create context data to pass to the template
    return render(request, 'index.html', context)  # Render the index.html template with the context data

# View for creating a new task
def createTask(request):
    projectObj = TodoItems.objects.all()  # Retrieve all instances of TodoItems
    form = TodoItemForm()  # Create an empty form instance
    
    if request.method == 'POST':
        form = TodoItemForm(request.POST)  # Bind the form with POST data
        if form.is_valid():
            form.save()  # Save the form data to create a new TodoItem
            return redirect('index')  # Redirect to the index page after successful creation
        
    return render(request, 'form1.html', {'form': form, 'projectObj':projectObj})  # Render the form1.html template with the form and projectObj

# View for updating a task
def updateTask(request, pk):
    projectObj = TodoItems.objects.get(id=pk)  # Retrieve a specific TodoItem by its id
    form = TodoItemForm(instance=projectObj)  # Create a form instance with the retrieved TodoItem
    
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=projectObj)  # Bind the form with POST data and the TodoItem instance
        if form.is_valid():
            form.save()  # Save the form data to update the TodoItem
            return redirect('index')  # Redirect to the index page after successful update
    
    context = {'projectObj':projectObj, 'form': form}  # Create context data to pass to the template
    return render(request, 'form1.html', context)  # Render the form1.html template with the context data

# View for deleting a task
def deleteTask(request, pk):
    projectObj = TodoItems.objects.get(id=pk)  # Retrieve a specific TodoItem by its id
    
    if request.method == 'POST':
        projectObj.delete()  # Delete the TodoItem
        return redirect('index')  # Redirect to the index page after successful deletion
    
    context = {'projectObj':projectObj}  # Create context data to pass to the template
    return render(request, 'delete_template.html', context)  # Render the form1.html template with the context data
