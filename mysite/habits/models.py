from django.db import models

# Create your models here.
class Habit(models.Model):
    habit_text = models.CharField(max_length=200)
    difficulty_level = models.IntegerField()

    def __str__(self):
        return self.habit_text

class Task(models.Model):
    task_text = models.CharField(max_length=200)
    difficulty_level = models.IntegerField

    def __str__(self):
        return self.task_text