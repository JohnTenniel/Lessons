from django.shortcuts import render
from .models import Main


def index(request):
    projects = Main.objects.all()
    return render(request, 'main/index.html', {'projects': projects})
