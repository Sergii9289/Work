# файл forms.py создаём сами для добавления функционала к форме добавления задачи в БД

from .models import Task
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm): # класс называем по имени модели + Form
    class Meta: # в этом классе указываем дополнительные настройки
        model = Task
        # дальше прописываем какие поля будут присутствовать в форме
        fields = ['title', 'task']
        # widgets - передаём аттрибуты, которые будут использованы в HTML документе при передаче {{ form.title }} и {{ form.task }}
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть назву'}),
            'task': Textarea(attrs={'class': 'form-control', 'placeholder': 'Введіть опис'})
        }
