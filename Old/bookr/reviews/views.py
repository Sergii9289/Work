from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Contributor, Publisher, Review
from .utils import average_rating
from .forms import SearchForm, PublisherForm, ReviewForm, BookMediaForm
from django.contrib import messages
from django.utils import timezone
from PIL import Image
from io import BytesIO
from django.core.files.images import ImageFile
from django.contrib.auth.decorators import (user_passes_test, login_required, permission_required)
from django.core.exceptions import PermissionDenied


def is_staff_user(user):
    return user.is_staff


def is_new_review(review_pk):
    return review_pk is None


def index(request):
    return render(request, 'base.html')


def book_search(request):
    search_text = request.GET.get('search', '')  # получаем данные из формы, в которой action ссылается на URL этой функции
    form = SearchForm(request.GET)
    books = set()
    search_history = request.session.get('search_history', [])  # отримати значення 'search_history'.
    # Якщо його нема, то створити порожній список.
    if form.is_valid() and form.cleaned_data['search']:
        search = form.cleaned_data['search']
        search_in = form.cleaned_data.get('search_in') or 'title'
        if request.user.is_authenticated:
            search_session = [search_in, search]
            search_history.insert(0, search_session)
            search_history = search_history[:10]
            request.session['search_history'] = search_history
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
    elif search_history: # якщо файл не пустий, то беремо з нього значення
        initial = dict(search=search_text, search_in=search_history[0][0]) # задаємо останній результат пошуку в initial
        form = SearchForm(initial=initial) # передаємо в файл forms.py значення initial параметрів форми
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
        reviews = book.review_set.all()  # обратная связь Many-to-one. Получить все объекты 'reviews'
        # для конкретной книги
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
    if request.user.is_authenticated:
        max_viewed_books_length = 10
        viewed_books = request.session.get('viewed_books', [])  # отримати значення 'viewed_books'.
        # Якщо його нема, то створити порожній список.
        viewed_book = [book.id, book.title]  # робимо об'єкт даної книги.
        if viewed_book in viewed_books:  # якщо книга є в списку переглянутих, то видаляємо її зі списка.
            viewed_books.remove(viewed_book)
        viewed_books.insert(0, viewed_book)  # добавляємо поточну книгу на першу позицію списку.
        viewed_books = viewed_books[:max_viewed_books_length]  # обрізаємо список до максимальної довжини (10 елементів)
        request.session['viewed_books'] = viewed_books  # повертаємо значення назад в сесію
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


def publisher_edit(request, pk=None):
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


@login_required
def review_edit(request, book_pk, review_pk=None):
    book = get_object_or_404(Book, pk=book_pk)
    user = request.user
    if review_pk is not None:
        temp = get_object_or_404(Review, pk=review_pk)
        if temp.book_id == book_pk:
            review = temp
            if user.id != review.creator_id:
                raise PermissionDenied
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


@login_required
def book_media(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookMediaForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save(False)
            uploaded_image = form.cleaned_data['cover']
            if uploaded_image and not hasattr(uploaded_image, 'path'):
                image = Image.open(uploaded_image)
                image.thumbnail((300, 300))
                image_data = BytesIO()
                image.save(fp=image_data, format=uploaded_image.image.format)
                image_file = ImageFile(image_data)
                book.cover.save(uploaded_image.name, image_file)
                book.sample = form.cleaned_data['sample']
                messages.success(request, f'{book} was updated')
            book.save()

            return redirect('book_detail', book.pk)

    else:
        form = BookMediaForm()
    context = {
        'form': form,
        'instance': book,
        'model_type': 'Book',
        'is_file_upload': True,
    }
    return render(request, 'reviews/instance-form.html', context)
