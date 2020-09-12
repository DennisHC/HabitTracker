from django.db import models
from django.contrib.auth.models import User

class HabitList(models.Model):
    list_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.list_name
    
class TaskList(models.Model):
    list_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.list_name

class HabitItem(models.Model):
    habit_list = models.ForeignKey(HabitList, on_delete=models.CASCADE)
    habit_text = models.CharField(max_length=200)
    difficulty_level = models.IntegerField()

    def __str__(self):
        return self.habit_text

class TaskItem(models.Model):
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    task_text = models.CharField(max_length=200)
    difficulty_level = models.IntegerField

    def __str__(self):
        return self.task_text