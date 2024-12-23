from django import template
from django.contrib.auth.models import User

register = template.Library()
from ..models import Review, Book


@register.inclusion_tag('book_list.html')
def book_list(username):
    user = User.objects.get(username=username)
    reviews = Review.objects.filter(creator_id=user.id)
    readed_books = []
    if reviews:
        for review in reviews:
            readed_books.append(review.book.title)
    return {'readed_books': readed_books}
