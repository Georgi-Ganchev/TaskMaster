from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import SignupForm, TaskForm
from .models import Task, CustomUser


# 0 -> Student
# 1 -> Teacher
def signup_form(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            role = form.cleaned_data['user_type']
            if role == '0':
                student_group, created = Group.objects.get_or_create(name='Student Group')
                student_group.user_set.add(user)
                messages.success(request, 'Student account created successfully!')
            else:
                teacher_group, created = Group.objects.get_or_create(name='Teachers waiting list')
                teacher_group.user_set.add(user)
                messages.info(request, 'Teacher account created. Please contact admin for group assignment.')


            login(request,user)
            return redirect('home')
    else:
            form = SignupForm()

    return render(request, 'tasks/signup.html', {'form': form})


@login_required(redirect_field_name='login')
def home_page(request):
    if request.user.user_type == '1':
        if request.user.groups.filter(name='Teacher Group').exists():
            students_list = CustomUser.objects.order_by("-id").filter(user_type = '0')
            return render(request, "tasks/teacher_home.html", {'students_list' : students_list} )
        else:
            return render(request, "tasks/teacher_waiting_list.html")
    
    else:
        user_tasks_list = Task.objects.order_by("-date").filter(user=request.user)
        ongoing_tasks = user_tasks_list.filter(completed=False)
        done_tasks = user_tasks_list.filter(completed=True)
        context = {
            "ongoing_tasks_list": ongoing_tasks,
            "done_tasks_list": done_tasks,
        }
        return render(request, "tasks/home_screen.html", context)


@login_required(redirect_field_name='login')
def task_details(request, task_id):
    task_id = int(task_id)
    task_info = get_object_or_404(Task, pk=task_id)
    return render(request, "tasks/task_details.html", {"task_info" : task_info })


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
@permission_required('api.add_task', raise_exception=True)
def task_creation(request, student_id):
    student = get_object_or_404(CustomUser, pk=student_id)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_giver=request.user
            task.user=student
            task.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_addition.html', {'form': form, 'student': student})


@login_required(redirect_field_name='login')
@permission_required('api.change_task', raise_exception=True)
def complete_task(request, task_id):
    current_task = get_object_or_404(Task, id=task_id)
    current_task.completed = True
    current_task.save()
    return redirect('home')

def welcome_page(request):
    return render(request, "tasks/welcome_screen.html")


@login_required(redirect_field_name='login')
@permission_required('api.change_task', raise_exception=True)
def student_details(request, student_id):
    student = get_object_or_404(CustomUser, id=student_id)
    tasks = Task.objects.filter(user=student)
    return render(request, 'tasks/student_info.html', {'student': student, 'tasks': tasks})