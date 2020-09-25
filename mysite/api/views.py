from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# REST API
import json
from django.core import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# My Files
from habits.models import TaskList, TaskItem, HabitItem, HabitList
from .serializers import TaskSerializer, TaskListSerializer

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': 'N/A',
        'Detail View': '/getTasks/<str:pk>/',
        'Create': '/addTask/',
        'Update': '/updateTask/<str:pk>/',
        'Delete': '/deleteTask/<str:pk>/',
    }
    return Response(api_urls)
    
"""
@api_view(['GET'])
def task_list(request):
    # 1) Get the current user object
    user = User.objects.get(username='admin')

    # 2) Get the current user's TaskList through the Foreign Key (Retrieves first item in QuerySet)
    my_task_list_name = TaskList.objects.select_related().filter(user=user).first()

    # 3) Get the TaskList's items
    my_task_list = my_task_list_name.task_items.all()
    # print(my_task_list)

    # 4) Pass all the task items into the context
    # context['current_user_tasklist'] = my_task_list

    # Serialize the data
    # data = serializers.serialize('json', my_task_list)
    # data = json.dumps(data)
    # print(type(data))
    data = TaskListSerializer(my_task_list)
    print(my_task_list)
    
    test = {
        'my_test': 'passed'
    }
    task_lists = TaskList.objects.all()
    print(task_lists)
    serializer = TaskListSerializer(task_lists, many=True)
    return Response(serializer.data)
"""

# Handle no user or user_task_list exception
@api_view(['GET'])
def getTasks(request, pk):

    # 1) Get the current user object
    try:
        user = User.objects.get(id=pk)
    except:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    print("The current user is: ", user)

    # 2) Get the current user's TaskList through the Foreign Key (Retrieves first item in QuerySet)
    try:
        my_task_list_name = TaskList.objects.select_related().filter(user=user).first()
    except:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    # 3) Get the TaskList's items
    my_task_list = my_task_list_name.task_items.all()

    serializer = TaskSerializer(my_task_list, many=True)

    return Response(serializer.data)
 
# Figure out how to attach TaskItem to a user
@api_view(['POST'])
def addTask(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# Working
@api_view(['POST'])
def updateTask(request, pk):
    task = TaskItem.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# Test this out
@api_view(['DELETE'])
def deleteTask(request, pk):
    task = TaskItem.objects.get(id=pk)
    task.delete()

    return Response('Item successfully deleted!')