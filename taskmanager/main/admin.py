from django.contrib import admin
from .models import Task, City

# Register your models here.

admin.site.register(Task)  # регистрация модели обязательна

admin.site.register(City)