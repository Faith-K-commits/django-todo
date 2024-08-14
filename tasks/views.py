from django.shortcuts import render

from .forms import RegistrationForm, LoginForm

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
    else:
        user_form = RegistrationForm()
    return render(request, 'tasks/register.html', {
        'user_form': user_form
    })
