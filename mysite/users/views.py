from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def create_account(request):
    form = UserCreationForm()
    return render(request, 'users/create_account.html', {'form': form})