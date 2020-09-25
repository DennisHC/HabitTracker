from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    # path('task_list/', views.task_list, name='rest_tasks_list'),

    # [READ] 'GET' on url '/api/getTasks/' + userID
    path('getTasks/<str:pk>/', views.getTasks, name='restGetTasks'),

    # [CREATE] 'POST' on url '/api/addTask' With userID in Body
    path('addTask', views.addTask, name='restAddTask'),

    # [UPDATE] 'POST' on url '/api/updateTask'
    path('updateTask/<str:pk>/', views.updateTask, name='restUpdateTask'),

    # [DELETE] 'DELETE' on url '/api/deleteTask'
    path('deleteTask/<str:pk>/', views.deleteTask, name='restDeleteTask'),



    # [READ] 'GET' on url '/api/getHabits/' + userID
    # path('getHabits', api_views.getHabits, name='restHabits),

    # [CREATE] 'POST' on url '/api/addHabit' With userID in Body
    # path('addHabit', api_views.addHabit, name='restAddHabit'),

    # [UPDATE] 'POST' on url '/api/updateHabit'
    # path('updateHabit/<str:pk>/', views.updateHabit, name='restUpdateHabit'),
    
    # [DELETE] 'DELETE' on url '/api/deleteHabit'
    # path('deleteHabit/<str:pk>/', views.deleteHabit, name='restDeleteHabit'),


]