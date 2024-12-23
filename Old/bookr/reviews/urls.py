from django.urls import path, include
from . import views, api_views
from django.conf import settings
from django.conf.urls.static import static
from bookr.views import profile
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', api_views.BookViewSet)  # Це означає, що ви реєструєте перегляд BookViewSet для маршруту /books/
router.register(r'reviews', api_views.ReviewViewSet)  # Це означає, що ви реєструєте перегляд ReviewViewSet для маршруту /reviews/

urlpatterns = [
    path('api/login', api_views.Login.as_view(), name='login'),
    path('api/', include(router.urls)),  # Це додасть всі маршрути з router.urls під префікс /api/
    path('accounts/profile/', profile, name='profile'), # надає інформацію про користувача
    path('', views.index, name='home'), # базова сторінка
    path('book-search/', views.book_search, name='search'),
    path('books/', views.books_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/<int:book_pk>/reviews/<int:review_pk>/', views.review_edit, name='review_edit'),
    path('books/<int:book_pk>/reviews/new/', views.review_edit, name='review_create'),
    path('books/<int:pk>/media/', views.book_media),
    path('publishers/<int:pk>/', views.publisher_edit, name='publisher_detail'),
    path('publishers/new/', views.publisher_edit, name='publisher_create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)  # context processor

