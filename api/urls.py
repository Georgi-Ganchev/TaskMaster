from django.urls import path

from . import views

urlpatterns = [
    path("<int:person_id>/", views.person_tasks, name="tasks"),

]