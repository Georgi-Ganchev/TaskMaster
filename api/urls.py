from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home_page, name="home"),
    path("details/<int:task_id>/", views.task_details, name="details"),
    path("login/", views.login_auth, name='login'),
    path("signup/", views.signup_form, name='signup'),
    path("login/success/", views.success_page, name='success'),
    path("welcome/", views.welcome_page, name="welcome_page"),
    path('logout/', views.logout_view, name='logout'),
    path("new_task/", views.task_creation, name='new_task')
    ]