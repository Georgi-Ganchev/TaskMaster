from django.shortcuts import render, get_object_or_404
from .models import Task


# Create your views here.

def person_tasks(request):
    latest_tasks_list = Task.objects.order_by("-date")
    context = {
        "latest_tasks_list": latest_tasks_list,
    }
    return render(request, "people/person_tasks.html", context)

def task_details(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "people/task_details.html", {"task:": task})