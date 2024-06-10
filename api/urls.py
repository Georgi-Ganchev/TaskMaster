from django.urls import path

from . import views

urlpatterns = [
    path("tasks/", views.person_tasks, name="tasks"),
    path("details/<int:task_id>/", views.task_details, name="details"),
    path("login/", views.login_auth, name='login'),
    path("login/success/", views.success_page, name='success')
]