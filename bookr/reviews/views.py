from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Contributor, Publisher, Review
from .utils import average_rating
from .forms import SearchForm, PublisherForm, ReviewForm
from django.contrib import messages
from django.utils import timezone

def index(request):
    return render(request, 'base.html')


def book_search(request):
    search_text = request.GET.get('search',
                                  '')  # получаем данные из формы, в которой action ссылается на URL этой функции
    form = SearchForm(request.GET)
    books = set()

    if form.is_valid() and form.cleaned_data['search']:
        search = form.cleaned_data['search']
        search_in = form.cleaned_data.get('search_in') or 'title'
        if search_in == 'title':
            books = Book.objects.filter(title__icontains=search)  # SQL (SELECT..... WHERE title LIKE '%search%'
        else:
            fname_contributors = Contributor.objects.filter(first_names__icontains=search)
            for contributor in fname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)
            lname_contributors = Contributor.objects.filter(last_names__icontains=search)
            for contributor in lname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)
    context = {
        'form': form,
        'search_text': search_text,
        'books': books
    }
    return render(request, 'reviews/search-results.html', context)


def books_list(request):
    books = Book.objects.all()  # передаём все элементы таблицы Book в переменную
    book_list = []
    for book in books:
        reviews = book.review_set.all()  # обратная связь Many-to-one. Получить все объекты 'reviews' для конкретной книги
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


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        context = {
            "book": book,
            "book_rating": book_rating,
            "reviews": reviews
        }
    else:
        context = {
            "book": book,
            "book_rating": None,
            "reviews": None
        }
    return render(request, "reviews/book_detail.html", context)


def instance_form(request, pk=None):
    if pk is not None:
        publisher = get_object_or_404(Publisher, pk=pk)
    else:
        publisher = None

    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            updated_publisher = form.save()
            if publisher is None:
                messages.success(request, f'Publisher {updated_publisher} was created.')
            else:
                messages.success(request, f'Publisher {updated_publisher} was updated.')
            return redirect('instance_form', updated_publisher.pk)
    else:
        form = PublisherForm(instance=publisher)
        updated_publisher = publisher
    context = {
        'form': form,
        'instance': publisher,
        'model_type': 'Publisher'

    }
    return render(request, 'reviews/instance-form.html', context)

def review_edit(request, book_pk, review_pk=None):
    book = get_object_or_404(Book, pk=book_pk)
    if review_pk is not None:
        temp = get_object_or_404(Review, pk=review_pk)
        if temp.book_id == book_pk:
            review = temp
        else:
            review = None
    else:
        review = None
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            updated_review = form.save(commit=False)
            updated_review.book = book
            if review is None:
                messages.success(request, f'Review for {updated_review.book.title} was created.')
            else:
                messages.success(request, f'Review {updated_review.book.title} was updated.')
                updated_review.date_edited = timezone.now()
            updated_review.save()
            return redirect('book_detail', book_pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form,
        'instance': review,
        'model_type': 'Review',
        'related_model_type': 'Book',
        'related_instance': book
    }
    return render(request, 'reviews/instance-form.html', context)

