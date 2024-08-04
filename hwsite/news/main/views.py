from django.shortcuts import render, redirect, get_object_or_404
from .models import Main
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def index(request):
    projects = Main.objects.all()
    return render(request, 'main/index.html', {'projects': projects})



def reg(request):
    if request.method == "GET":
        return render(request, 'main/reg.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('reg')
            except IntegrityError:
                return render(request, 'main/reg.html',
                              {'form': UserCreationForm(), 'error': 'Такое имя пользователя уже существует'
                                                                    ', задайте другое'})
        else:
            return render(request, 'main/reg.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


def log(request):
    if request.method == "GET":
        return render(request, 'main/log.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'main/log.html', {'form': AuthenticationForm(),
                                                     'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('perk')


def unlog(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')

@login_required
def perk(request):
    return render(request, 'main/perk.html')
