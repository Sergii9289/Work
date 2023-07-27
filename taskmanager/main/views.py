from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.all() #выводит все объекты в виде списка
    # tasks = Task.objects.order_by(id)  # выводит сортированный список
    return render(request, 'main/index.html', {'title': 'Головна сторінка сайту', 'tasks': tasks})
    # через jinja передаёт значения 'title' и 'tasks' HTML документ

def about(request):
    return render(request, 'main/about.html')