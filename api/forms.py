from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import Task

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=100) #required=True)
    school = forms.CharField(max_length=100)
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_giver', 'completed']
        #exclude = ["user"]
        