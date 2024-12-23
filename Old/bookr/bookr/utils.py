import datetime
from ..reviews.models import Review
from django.db.models import Count

def get_books_read_by_month(username):
    """Get the books read by the user on per month
    basis.
    :param: str The username for which the books needs
    to be returned
    :return: dict of month wise books read
    """
    current_year = datetime.datetime.now().year

    books = Review.objects.filter(  # filtration of records that btlong to user in this year
        creator__username__contains=username,
        date_created__year=current_year)\
        .values('date_created__month')\
        .annotate(book_count=Count('book__title'))  # values() - select only the month field from the date_created
    # annotate() - total number of books read in a given month
    return books

