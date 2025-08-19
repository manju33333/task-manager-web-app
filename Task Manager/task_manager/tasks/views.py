'''from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Home Page: View all tasks
def home(request):
    tasks = Task.objects.all()  # Fetch all tasks from the database
    return render(request, 'tasks/home.html', {'tasks': tasks})  # Pass tasks to the template for rendering

# Add Task: Show a form to add a new task
def add_task(request):
    if request.method == 'POST':  # If the form is submitted (POST request)
        form = TaskForm(request.POST)  # Create a form instance with the submitted data
        if form.is_valid():  # Check if the form data is valid
            form.save()  # Save the new task to the database
            return redirect('home')  # After saving, redirect to the home page (task list)
    else:
        form = TaskForm()  # If it's a GET request (initial page load), show an empty form
    return render(request, 'tasks/add_task.html', {'form': form})  # Render the form in the template

# Edit Task: Show a form to edit an existing task
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)  # Fetch the task by ID
    if request.method == 'POST':  # If the form is submitted (POST request)
        form = TaskForm(request.POST, instance=task)  # Bind the form with the task instance
        if form.is_valid():  # Check if the form data is valid
            form.save()  # Save the edited task to the database
            return redirect('home')  # After saving, redirect to the home page (task list)
    else:
        form = TaskForm(instance=task)  # If it's a GET request, show the form with existing task data
    return render(request, 'tasks/edit_task.html', {'form': form})  # Render the form to edit task

# Delete Task: Delete a specific task
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)  # Fetch the task by ID
    task.delete()  # Delete the task from the database
    return redirect('home')  # After deleting, redirect to the home page (task list)
'''

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Task
from .forms import TaskForm

@login_required
def home(request):
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')

    tasks = Task.objects.all()

    if search_query:
        tasks = tasks.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    
    if status_filter:
        tasks = tasks.filter(status=status_filter)

    tasks = tasks.order_by('due_date')

    return render(request, 'tasks/home.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')
