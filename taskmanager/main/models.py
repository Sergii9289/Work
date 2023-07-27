from django.db import models


class Task(models.Model):
    title = models.CharField('Назва', max_length=50)
    task = models.TextField('Опис')

    def __str__(self):
        return self.title  # то, что будет выводиться на экран при вызове

    class Meta:
        verbose_name = 'Задача'  # присваиваем имя для отображения на странице admin
        verbose_name_plural = 'Задачі'  # присваиваем имя для отображения на странице admin в множественном числе

