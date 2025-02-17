from django.contrib import auth, admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import profile, reading_history
import debug_toolbar

urlpatterns = [
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/read_history/', reading_history, name='read_history'),
    path('admin/', admin.site.urls),
    path('accounts/', include(('django.contrib.auth.urls', 'auth'), namespace='accounts')),
    path('accounts/password_reset/done/', auth.views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/done/', auth.views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', include('reviews.urls')),
    path('filter_demo/', include('filter_demo.urls')),
    path('book_management/', include('book_management.urls')),
    path('', include('bookr_test.urls')),
    path('allauth/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns