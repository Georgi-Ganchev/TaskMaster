from django.contrib import admin
from .models import Task, Person
# Register your models here.

admin.site.register(Task)
admin.site.register(Person)