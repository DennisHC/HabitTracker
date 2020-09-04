from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User

def create_account(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(request.POST['username'])
        #for key, value in request.POST.items():
        #    print("Key: %s" % (key) )
        #    print("Value %s" % (value) )
        if form.is_valid():
            print("Account successfully created!")
            form_username = form.cleaned_data.get('username')
            form_password = form.cleaned_data.get('password1')
            new_user = User(username = form_username, password = form_password)
            new_user.save()
            messages.success(request, f'Account created for {form_username}!')
        return redirect('homepage')
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
    # is_private = request.POST.get('is_private', False);
    if request.method == 'POST':
        # form = forms.UserRegistrationForm(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("You did it!")
        else:
            print("it didn't work")
        #if request.POST['username'] == 'dennis':
        #    print("YOU DID IT!!")
        for key, value in request.POST.items():
            print("Key: %s" % (key) )
            print("Value %s" % (value) )
        return HttpResponseRedirect('/success')


    dictionary_object = {'Person1': 'Dennis', 'Person2': 'Ian'}
    return render(request, 'users/login.html', dictionary_object)


def logout(request):
    return render(request, 'users/logout.html')

def my_habits(request):
    return render(request, 'users/my_habits.html')


def password_reset(request):
    return render(request, 'users/password_reset.html')