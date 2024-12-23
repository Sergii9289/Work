from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import media_example.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('media-example/<int:pk>/', media_example.views.media_example)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)