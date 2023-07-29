from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    # tasks = Task.objects.all() # выводит все объекты в виде списка
    tasks = Task.objects.order_by('-id')[:3]  # выводит сортированный список (если поставить '-', то сортировка в обратном порядке).
    # [:4] срез списка. Сколько значений будет выведено из БД
    return render(request, 'main/index.html', {'title': 'Головна сторінка сайту',
                                               'tasks': tasks})  # в словаре в конце передаёи информацию для jinja
    # через jinja передаёт значения 'title' и 'tasks' HTML документ


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':  # без отправки данных стоит метод GET. Когда отправляем данные - POST
        form = TaskForm(request.POST)  # сщздаём объект, наполненный данными от пользователя
        if form.is_valid():  # усли данные корректны
            form.save()  # то сохраняем
            return redirect('home')  # перенаправляем клиента на домашнюю страницу
        else:
            error = 'Форма не корректна'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
