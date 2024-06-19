from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, TaskForm
from .models import Task


# Create your views here.

def signup_form(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request, "tasks/people/person_tasks.html")
    else:
            form = SignupForm()
    return render(request, 'tasks/signup.html', {'form': form})

@login_required(redirect_field_name='login')
def home_page(request):
    user_tasks_list = Task.objects.order_by("-date").filter(user=request.user)
    context = {
        "latest_tasks_list": user_tasks_list,
    }
    return render(request, "tasks/home_screen.html", context)

# @login_required(redirect_field_name='login')
# def person_tasks(request):
#     latest_tasks_list = Task.objects.order_by("-date").filter(user=request.user)
#     context = {
#         "latest_tasks_list": latest_tasks_list,
    # }
    # return render(request, "tasks/people/person_tasks.html", context)

def task_details(request, task_id):
    task_info = Task.objects.get(pk=task_id)
    return render(request, "tasks/people/task_details.html", {"task_info" : task_info })

def login_auth(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, 'tasks/login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'tasks/login.html')
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

@login_required(redirect_field_name="login")
def task_creation(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_addition.html', {'form': form})
    
        
def success_page(request):
    return render(request, "tasks/success.html")

def welcome_page(request):
    return render(request, "tasks/welcome_screen.html")
