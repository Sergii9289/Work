from django.db import models


class Task(models.Model):   # создаём таблицу Task и проводим миграции (сначала 'makemigrations', затем 'migrate')
    title = models.CharField('Назва', max_length=50)    # !!!! обязательно зарегистрировать в admin.py !!!!!
    task = models.TextField('Опис')

    def __str__(self):
        return self.title  # то, что будет выводиться на экран при вызове

    class Meta:
        verbose_name = 'Задача'  # присваиваем имя для отображения на странице admin
        verbose_name_plural = 'Задачі'  # присваиваем имя для отображения на странице admin в множественном числе

class City(models.Model):   # создаём таблицу City и проводим миграции (сначала 'makemigrations', затем 'migrate')
    name = models.CharField(max_length=30)  # !!!! обязательно зарегистрировать в admin.py !!!!!

    def __str__(self):
        return self.name
