from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, LoginForm, TaskForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def index(request):
    return render(request, 'tasks/index.html')
def register_user(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)

            # Hash password
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('tasks:login')
    else:
        user_form = RegistrationForm()
    return render(request, 'tasks/register.html', {
        'user_form': user_form
    })

def login_user(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # Extract cleaned data from the form
            cd = login_form.cleaned_data

            # Call the provided user object
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('tasks:index')
            else:
                return HttpResponse("Invalid username or password. Please try again.")
    else:
        login_form=LoginForm()

    return render(request, 'tasks/login.html', {
        'login_form': login_form
    })
@login_required
def logout_user(request):
    logout(request)
    return redirect('tasks:login')

# Function to get task list of a user
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

# Function to create a new task
@login_required
def create_task(request):
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            new_task = task_form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks:tasks')
    else:
        task_form = TaskForm()
    return render(request, 'tasks/create_task.html', {
        'task_form': task_form
    })

# Function to update a task
@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('tasks:tasks')
    else:
        task_form = TaskForm(instance=task)
    return render(request, 'tasks/update_task.html', {
        'task_form': task_form
    })

# Function to delete a task
@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect('tasks:tasks')
    return render(request, 'tasks/delete_task.html', {
        'task': task
    })
