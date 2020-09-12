from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import View
from habits.models import TaskList

def index(request, id):
    profile_name = TaskList.objects.get(id = id)
    context = {}
    context[profile_name] = str(id)
    print(context)
    return render(request, 'user_profiles/my_profile.html', context)