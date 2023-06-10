from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # встроенная в Django форма для легкого создания новых пользователей
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html', {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:  # POST - словарь, данные в скобках - ключи
            try:
                user = User.objects.create_user(request.POST['username'],
                                                password = request.POST['password1'])  # User объект имеет поля: username, password, first_name, last_name
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:  # Exception raised when the relational integrity of the database is affected, e.g. a foreign key check fails, duplicate key, etc. 
                return render(request, 'signupaccount.html', {'form': UserCreateForm,
                                                              'error': 'Username already take. Choose new username.'})
        else:
            return render(request, 'signupaccount.html', {'form': UserCreateForm, 
                                                         'error': 'Passwords do not match'})

@login_required      
def logoutaccount(request):
    logout(request)
    return redirect('home')

def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'loginaccount.html', {'form': AuthenticationForm(),
                                                         'error': 'username and password do not match'})
        else:
            login(request, user)
            return redirect('home')