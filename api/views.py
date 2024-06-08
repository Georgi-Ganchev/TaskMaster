from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Task


# Create your views here.

def person_tasks(request):
    latest_tasks_list = Task.objects.order_by("-date")
    context = {
        "latest_tasks_list": latest_tasks_list,
    }
    return render(request, "people/person_tasks.html", context)

def task_details(request, task_id):
    task_info = Task.objects.get(pk=task_id)
    return render(request, "people/task_details.html", {"task_info" : task_info })

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('success.html')
            ...
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')