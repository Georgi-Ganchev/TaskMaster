from django.db import models

# Create your models here.
class Task(models.Model):
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
    

class Person(models.Model):
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)