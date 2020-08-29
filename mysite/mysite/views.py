from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import View
from . import forms

def myhomepage(request):
    return render(request, 'habits/homepage.html')

#def register(request):


def login(request):
   # user = authenticate(username=test, password=test)
   # if user is not None:
        # A backend authenticated the credentials
   #     redirect(myhomepage)
    #else:
        # No backend authenticated the credentials
    if request.method == 'POST':
        # form = forms.UserRegistrationForm(request.POST)
        #if form.is_valid():
        return HttpResponseRedirect('/success')

        #return HttpResponse('No casa.')

    dictionary_object = {'Person1': 'Dennis', 'Person2': 'Ian'}
    return render(request, 'habits/login.html', dictionary_object)

def logout(request):
    return render(request, 'habits/logout.html')

def password_reset(request):
    return render(request, 'habits/password_reset.html')

def create_account(request):
    form = UserCreationForm()
    return render(request, 'habits/create_account.html', {'form': form})

def success(request):
    return render(request, 'habits/success.html')

def about_us(request):
    return render(request, 'habits/about_us.html')

def features(request):
    return render(request, 'habits/features.html')