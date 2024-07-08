from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Task, CustomUser

class SignupForm(UserCreationForm):
    CHOICES = [
        ('1', 'Teacher'),
        ('0', 'Student'),
    ]
    email = forms.EmailField(max_length=100)
    school = forms.CharField(max_length=100)
    user_type = forms.ChoiceField(
        choices=CHOICES, 
        widget=forms.RadioSelect, 
        label='Select a Role'
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = self.cleaned_data['user_type']
        if commit:
            user.save()
        return user

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_giver', 'completed']
        
