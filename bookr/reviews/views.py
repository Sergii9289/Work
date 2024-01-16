from django.shortcuts import render


def index(request):
    name = 'world'
    return render(request, 'base.html', {'name': name})


def search_result(request):
    name = request.GET.get('search') or 'None'
    return render(request, 'searchresult.html', {'book': name})