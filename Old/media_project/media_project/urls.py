from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import media_example.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('media-example/', media_example.views.media_example),
    path('media-example1/', media_example.views.media_example1),
    path('media-example-with-form/', media_example.views.upload_image),
    path('upload-file/', media_example.views.file_upload),
    path('upload-file-model/', media_example.views.model_upload),
    path('upload-image-model/', media_example.views.image_model_upload),
    path('model-form-upload/', media_example.views.model_form_upload)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)