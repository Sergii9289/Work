from django.shortcuts import render, get_object_or_404
from .models import Book
from .utils import average_rating


def index(request):
    return render(request, 'reviews/base.html')


def book_search(request):
    search_text = request.GET.get('search', '')
    return render(request, 'reviews/search-results.html', {'search_text': search_text})


def books_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            rating_list = []
            for review in reviews:
                rating_list.append(review.rating)
            book_rating = average_rating(rating_list)
        else:
            book_rating = None
        number_of_reviews = len(reviews)
        book_list.append({'book': book,
                          'book_rating': book_rating,
                          'number_of_reviews': number_of_reviews})
    context = {'book_list': book_list}
    return render(request, 'reviews/book_list.html', context)


def book_details(request, book_pk):
    review_list = []
    book = get_object_or_404(Book, id=book_pk)
    reviews = book.review_set.all()
    if reviews:
        rating_list = []
        for review in reviews:
            review_list.append(review)
            rating_list.append(review.rating)
        book_rating = average_rating(rating_list)
    else:
        book_rating = None
    book_data = [{'book': book,
                  'book_rating': book_rating}]
    context = {'book_data': book_data,
               'review_list': review_list}
    return render(request, 'reviews/book_details.html', context)