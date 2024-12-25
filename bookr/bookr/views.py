from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from plotly.offline import plot
import plotly.graph_objects as graphs
from .utils import get_books_read_by_month, books_read_by_user
import xlsxwriter
from io import BytesIO
from django.http import HttpResponse


@login_required
def profile(request):
    user = request.user
    permissions = user.get_all_permissions()  # Retrieves all the permissions of the user.
    # Get the books read in different months this year
    books_read_by_months = get_books_read_by_month(user.username)
    # Initialize the Axis for graphs, X-Axis is months, Y-axis is books read
    months = [i + 1 for i in range(12)]  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    books_read = [0 for _ in range(12)]  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for num_books_read in books_read_by_months:
        # books_read_by_months видає нам querySet:
        # <QuerySet [{'date_created__month': 11, 'book_count': 1}, {'date_created__month': 12, 'book_count': 1}]>
        list_index = num_books_read['date_created__month'] - 1  # робимо Python нумерація від нуля.
        books_read[list_index] = num_books_read['book_count']  # заповнюємо список books_read

    # Generate a scatter plot HTML
    figure = graphs.Figure()  # make an instance of 'plotly.graph_objects.Figure' class
    scatter = graphs.Scatter(x=months, y=books_read)  # створюємо діаграму
    figure.add_trace(scatter)
    figure.update_layout(xaxis_title='Months', yaxis_title='Nubmer of books read')
    plot_html = plot(figure, output_type='div')
    context = {
        'user': user,
        'permissions': permissions,
        'books_read_plot': plot_html
    }
    return render(request, 'profile.html', context)

@login_required
def reading_history(request):
    user = request.user  # retrieve user from request
    books: [list] = books_read_by_user(user.username)  # retrieve books read by user through reviews model
    # filename = f'{user.username}_books.xlsx'  # create filename using username
    filename = BytesIO()
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    for row in range(len(books)):
        worksheet.write(row, 0, books[row])
    workbook.close()
    excel_data = filename.getvalue()  # retrieve data from memory file
    # setting up an HttpResponse to send an Excel file.
    response = HttpResponse(content_type='application/vnd.ms-excel')
    # Set the Content-Disposition header to prompt a download with a personalized filename
    response['Content-Disposition'] = f'attachment; filename={user.username}_reading_history.xlsx'
    response.write(excel_data)
    return response

