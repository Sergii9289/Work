from django.contrib import admin, auth
from django.urls import path, include

urlpatterns = [
    path('book_management/', include('book_management.urls')),
    path('filter_demo/', include('filter_demo.urls')),
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')), # додає файл reviews/urls.py і всі його адреси
    path('accounts/', include(('django.contrib.auth.urls', 'auth'), namespace='accounts')), # автоматичне додання URL - шаблонів Django до нашого коду
    # /accounts/login/  , /accounts/logout/  і т.н.
    path('accounts/password_reset/done/', auth.views.PasswordResetDoneView.as_view(), name="password_reset_done",),
    path("accounts/reset/done/", auth.views.PasswordResetCompleteView.as_view(), name="password_reset_complete",),
]
