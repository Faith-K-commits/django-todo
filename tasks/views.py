from django.shortcuts import render

def task(request):
    return render(request, 'tasks/index.html')
