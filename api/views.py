from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.template import loader


# Create your views here.

def person_tasks(request, person_id):
    latest_tasks_list = Task.objects.order_by("-date")
    template = loader.get_template("people/person_tasks.html")
    context = {
        "latest_tasks_list": latest_tasks_list,
    }
    output = ', '.join([q.task_name for q in latest_tasks_list])
    return HttpResponse(template.render(context, request))