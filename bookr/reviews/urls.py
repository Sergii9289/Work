from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('book-search/', views.book_search, name='search'),
    path('books/', views.books_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('publishers/<int:pk>/', views.instance_form, name='instance_form'),
    path('publishers/new/', views.instance_form, name='instance_form'),
    path('books/<int:book_pk>/reviews/<int:review_pk>/', views.review_edit, name='review_edit'),
    path('books/<int:book_pk>/reviews/new/', views.review_edit, name='review_create')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

