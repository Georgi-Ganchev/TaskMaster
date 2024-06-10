from django.urls import path

from . import views

urlpatterns = [
    path("tasks/", views.person_tasks, name="tasks"),
    path("details/<int:task_id>/", views.task_details, name="details"),
    path("login/", views.login_auth, name='login'),
    path("signup/", views.signup_form, name='signup'),
    path("login/success/", views.success_page, name='success'),
    path("home/", views.home_page, name="homepage")
]