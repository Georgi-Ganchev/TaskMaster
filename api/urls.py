from django.urls import path

from . import views

urlpatterns = [
    path("tasks/", views.person_tasks, name="tasks"),
    path("details/<int:task_id>/", views.task_details, name="details")
]