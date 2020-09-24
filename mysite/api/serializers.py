from rest_framework import serializers
from habits.models import TaskItem, TaskList

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = '__all__'

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = '__all__'