from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import View
from django.contrib import messages

def create_account(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
    else:
        form = UserCreationForm()
    return render(request, 'users/create_account.html', {'form': form})

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


    dictionary_object = {'Person1': 'Dennis', 'Person2': 'Ian'}
    return render(request, 'users/login.html', dictionary_object)


def logout(request):
    return render(request, 'users/logout.html')

def my_habits(request):
    return render(request, 'users/my_habits.html')


def password_reset(request):
    return render(request, 'users/password_reset.html')