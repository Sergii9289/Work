from django.shortcuts import render
from .forms import ExampleForm, OrderForm

def form_example(request):
    # for name in request.POST:
    #     print(f'{name}: {request.POST.getlist(name)}')
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print(f'{name}: ({type(value)}) {value}')
    else:
        form = ExampleForm()
    return render(request, 'form_example.html', {'method': request.method, 'form': form})


def order_form(request):
    initial = {'email': 'user@example.com'}
    if request.method == 'POST':
        form = OrderForm(request.POST, initial=initial)
    else:
        form = OrderForm(initial=initial)
    return render(request, 'order-form.html', {'method': request.method, 'form': form})
