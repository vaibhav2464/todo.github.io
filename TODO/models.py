from django.db import models

# Create your models here.
class Todo(models.Model):
    taskname=models.CharField(max_length=300)
    deadline=models.DateField()
    description=models.CharField(max_length=3000)
    

    def __str__(self):
        return self.task 