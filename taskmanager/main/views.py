from django.shortcuts import render, redirect
from .models import Task, City
from .forms import TaskForm
import requests


def index(request):
    # tasks = Task.objects.all() # выводит все объекты в виде списка
    tasks = Task.objects.order_by('-id')[
            :3]  # выводит сортированный список (если поставить '-', то сортировка в обратном порядке).
    # [:4] срез списка. Сколько значений будет выведено из БД
    return render(request, 'main/index.html', {'title': 'Головна сторінка сайту',
                                               'tasks': tasks})  # в словаре в конце передаёи информацию для jinja
    # через jinja передаёт значения 'title' и 'tasks' HTML документ


def weather(request):
    api_key = '6d26d75769caffae67cc0c6302c7dd59'

    all_cities = []

    cities = City.objects.all() # получаем список городов из БД

    for city in cities:
        url2 = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}'
        res2 = requests.get(url2).json() # в эту пересенную мы помещаем результат запроса API. '.json' конвертирует результат в словарь

        lat = res2[0]['lat']
        lon = res2[0]['lon']
        url1 = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}'
        res = requests.get(url1).json()

        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }
        all_cities.append(city_info)    # создаём список информации по всем городам


    context = {'all_info': all_cities}      # сщздаёи словарь Jinja для передачи данных в HTML

    return render(request, 'main/weather.html', context)


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
