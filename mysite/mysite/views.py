from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import View
from . import forms

def myhomepage(request):
    return render(request, 'habits/homepage.html')

def success(request):
    return render(request, 'users/success.html')

def about_us(request):
    return render(request, 'habits/about_us.html')

def features(request):
    return render(request, 'habits/features.html')