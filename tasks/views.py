from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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
