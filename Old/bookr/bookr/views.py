from django.shortcuts import render
from django.contrib.auth.decorators import (login_required, permission_required)
from django.contrib.auth.models import User
from plotly.offline import plot
import plotly.graph_objects as graphs
from .utils import get_books_read_by_month


@login_required(redirect_field_name='redirect_to') # декоратор, який перенаправляє неавтентифікованого користувача на сторінку авторизації.
def profile(request):
    return render(request, 'profile.html')

@login_required
def profile1(request):
    user = request.user
    permissions = user.get_all_permissions()
    # Get the books read in different months this year
    books_read_per_month = get_books_read_by_month(user.username)
    # Initialize the Axis for graphs, X-Axis is months, Y - axis is books read
    months = [i+1 for i in range(12)]
    books_read = [0 for _ in range(12)]
    # Set the value for books read per month on Y-Axis
    for num_books_read in books_read_per_month:
        list_index = num_books_read['date_created__month'] - 1
        books_read[list_index] = num_books_read['book_count']

    # Generate a scatter plot HTML
    figure = graphs.Figure()
    scatter = graphs.Scatter(x=months, y=books_read)
    figure.add_trace(scatter)
    figure.update_layout(xaxis_title='Month', yaxis_title="No. of books read")
    plot_html = plot(figure, output_type='div')
    # Add to template
    context = {
        'user': user,
        'permissions': permissions,
        'books_read_plot': plot_html
    }
    return render(request, 'profile.html', context)