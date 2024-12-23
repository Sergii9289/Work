from django.shortcuts import render

def index(request):
    names = "john,doe,mark,swain,1,2,3,4"
    return render(request, 'index.html', {'names': names})

def greeting_view(request):
    books = {
        "The night rider": "Ben Author",
        "The Justice": "Don Abeman"
    }
    context = {
        'username': 'Sergii',
        'books': books
    }
    return render(request, 'simple_tag_template.html', context)