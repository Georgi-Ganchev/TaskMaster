from django.db import models, models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):

    USER_TYPE_CHOICES = (
        ('1', 'Teacher'),
        ('0', 'Student'),
    )
    GENDER_CHOICES = (
        ('0', 'Male'),
        ('1', 'Female'),
        ('2', 'Other'),
    )
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)
    email = models.EmailField(blank=True, default='', unique=True)
    username = models.CharField(
        max_length=150,
        default='', 
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits, and spaces only.',
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )

    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)

    

class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task_name = models.CharField("Task Name", max_length=20)
    task_giver = models.CharField("Given by:", max_length=20)
    date = models.DateField("Date Published", auto_now_add=True)
    completed = models.BooleanField("Completed", default=False)

    def __str__(self):
        if self.completed:
            is_done = 'done'
        else:
            is_done = 'not done'
        return f"Task {self.task_name} from {self.task_giver} is {is_done}."
    


