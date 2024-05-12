from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('form-example/', views.form_example, name='form-example'),
    path('order-form/', views.order_form, name='order-form')
]
