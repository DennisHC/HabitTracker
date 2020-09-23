from django.db import models
from django.contrib.auth.models import User
class HabitItem(models.Model):
    habit_name = models.CharField(max_length=200)
    difficulty_level = models.IntegerField(default=1)

    def __str__(self):
        return self.task_name

class TaskItem(models.Model):
    task_name = models.CharField(max_length=200)
    difficulty_level = models.IntegerField(default=1)

    def __str__(self):
        return self.task_name

class HabitList(models.Model):
    list_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habit_items = models.ManyToManyField(HabitItem)

    def __str__(self):
        return self.list_name
    
class TaskList(models.Model):
    list_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_items = models.ManyToManyField(TaskItem)

    def __str__(self):
        return self.list_name