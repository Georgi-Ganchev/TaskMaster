from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField("User Name", max_length=20, blank=True)

class Task(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    task_name = models.CharField("Task Name", max_length=20)
    task_giver = models.CharField("Given by:", max_length=20)
    date = models.DateField("Date Published")
    completed = models.BooleanField("Completed", default=False)

    def __str__(self):
        if self.completed:
            is_done = 'done'
        else:
            is_done = 'not done'
        return f"Task {self.task_name} from {self.task_giver} is {is_done}."
    