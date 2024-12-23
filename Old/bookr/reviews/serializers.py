from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import NotAuthenticated, PermissionDenied

from .models import Book, Publisher, Review
from .utils import average_rating


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'website', 'email']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class ReviewSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)  # передаємо серіалізовані дані таблиці User у змінну
    book = serializers.StringRelatedField(read_only=True)  # take result of __str__ method in model

    class Meta:
        model = Review
        fields = ['pk', 'content', 'date_created', 'date_edited', 'rating', 'creator', 'book', 'book_id']

    def create(self, validated_data):
        request = self.context['request']  # отримати об’єкт запиту всередині класу серіалізатора
        creator = request.user  # помістити інфо про користувача в змінну creator
        if not creator.is_authenticated:
            raise NotAuthenticated('Authentication required.')
        book = Book.objects.get(pk=request.data['book_id'])
        return Review.objects.create(content=validated_data['content'], book=book, creator=creator,
                                     rating=validated_data['rating'])

    def update(self, instance, validated_data):  # передаємо рядок БД reviews.review і нові дані
        request = self.context['request']  # отримати об’єкт запиту всередині класу серіалізатора
        creator = request.user  # помістити інфо про користувача в змінну creator
        if not creator.is_authenticated or instance.creator_id != creator.pk:
            raise PermissionDenied('Permission denied, you are not the creator of this review')
        instance.content = validated_data['content']  # оновлюємо вміст колонки review.content
        instance.rating = validated_data['rating']  # оновлюємо вміст колонки review.кфештп
        instance.date_edited = timezone.now()  # оновлюємо вміст колонки review.date_edited
        instance.save()
        return instance  # повертаємо рядок БД reviews.review змінений


class BookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()  # передаємо серіалізовані дані таблиці Publisher у змінну
    rating = serializers.SerializerMethodField('book_rating')  # returns result of 'book_rating' function
    reviews = serializers.SerializerMethodField('book_reviews')  # returns result of 'book_review' function

    def book_rating(self, book):
        reviews = book.review_set.all()  # _set повертає всі об'єкти review пов'язані з book
        if reviews:
            return average_rating([review.rating for review in reviews])
        else:
            None

    def book_reviews(self, book):
        reviews = book.review_set.all()  # _set повертає всі об'єкти review пов'язані з book
        if reviews:
            return ReviewSerializer(reviews, many=True).data  # data - це атрибут,
            # який містить серіалізовані дані з об’єктів, які були передані в серіалізатор

    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'isbn', 'publisher', 'rating', 'reviews']
