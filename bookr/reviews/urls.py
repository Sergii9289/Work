from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('search-results/', views.book_search, name='search'),
    path('books/', views.books_list, name='book_list'),
    path('books/<int:book_pk>/', views.book_details, name='book_details')
]