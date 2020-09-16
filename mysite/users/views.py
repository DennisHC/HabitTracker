from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from habits.models import TaskList, TaskItem, HabitItem, HabitList

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
            new_user_obj = User()
            new_user_obj.username = form_username
            new_user_obj.password = form_password
            new_user_obj.save()
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
        # for key, value in request.POST.items():
        #     print("Key: %s" % (key) )
        #     print("Value %s" % (value) )
        username = request.POST.get('username')
        username = username.cleaned_data
        password = request.POST.get('password')
        password = password.cleaned_data
        user = authenticate(username = username, password = password)
        if user is not None:
            print("You did it!")
            login(request, user)
            return redirect('/success')
        else:
            print("It didn't work")
            return redirect('login')
    else:
        dictionary_object = {'Person1': 'Dennis', 'Person2': 'Ian'}
        return render(request, 'users/login.html', dictionary_object)


def logout(request):
    return render(request, 'users/logout.html')

def my_habits(request):
    #if request.method == 'POST':

    #else:

    # Get the current user object
    user = User.objects.get(username='admin')

    # Get the current user's TaskList
    my_task_list_name = TaskList.objects.get(list_name='Admin Task List')

    # Get the TaskList's items
    my_task_list = my_task_list_name.task_items.all()

    # Pass all the task items into the context
    context = {} 
    context['current_user_tasklist'] = my_task_list

    return render(request, 'users/my_habits.html', context)

def profile(request):
    return render(request, 'users/profile.html')

@login_required
def password_reset(request):
    return render(request, 'users/password_reset.html')