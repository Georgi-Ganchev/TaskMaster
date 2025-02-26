from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home_page, name="home"),
    path("details/<int:task_id>/", views.task_details, name="details"),
    path("student_details/<int:student_id>/", views.student_details, name="student_details"),
    path("login/", views.login_auth, name='login'),
    path("signup/", views.signup_form, name='signup'),
    path("welcome/", views.welcome_page, name="welcome_page"),
    path('logout/', views.logout_view, name='logout'),
    path("new_task/<int:student_id>/", views.task_creation, name='new_task'),
    path("complete/<int:task_id>/", views.complete_task, name='complete'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task')

    ]