from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api_overview'),

    # 'GET' on url '/api/getTasks/' + userID
    path('task_list/', views.task_list, name='rest_tasks_list'),
    path('user_tasks/<str:pk>/', views.user_tasks, name='rest_user_tasks'),
    path('user_task_create/', views.user_task_create, name='rest_user_task_create'),

    # <int:id>'
    # 'GET' on url '/api/getHabits/' + userID
    # path('getHabits', api_views.get_habits, name='rest_habits),

    # 'POST' on url '/api/addTask' With userID in Body
    # path('addTask', api_views.add_task, name='rest_add_task'),
    # 'POST' on url '/api/addHabit' With userID in Body
    # path('addHabit', api_views.add_habit, name='rest_add_habit'),
]