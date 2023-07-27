from django.shortcuts import render
from .models import Task

def index(request):
    # tasks = Task.objects.all() # выводит все объекты в виде списка
    tasks = Task.objects.order_by('-id')[:2] # выводит сортированный список (если поставить '-', то сортировка в обратном порядке).
    # [:4] срез списка. Сколько значений будет выведено из БД
    return render(request, 'main/index.html', {'title': 'Головна сторінка сайту', 'tasks': tasks}) # в словаре в конце передаёи информацию для jinja
    # через jinja передаёт значения 'title' и 'tasks' HTML документ

def about(request):
    return render(request, 'main/about.html')