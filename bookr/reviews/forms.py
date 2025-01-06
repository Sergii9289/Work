from django import forms
from .models import Publisher, Review, Book
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

CHOICES = (
    ('title', 'Title'),
    ('contributor', 'Contributor')
)


class BookMediaForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('cover', 'sample')

    cover = forms.ImageField(required=False)


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(choices=CHOICES)

    def __init__(self, *args, **kwargs):  # конструктор, який приймає будь-які аргументи та ключові аргументи.
        # викликає конструктор батьківського класу, передаючи всі аргументи.
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'  # форма буде надсилати дані через метод HTTP GET
        # Це корисно для форм, які виконують пошукові запити або інші операції, що не змінюють стан сервера.
        self.helper.add_input(Submit('', 'Пошук'))  # додано кнопку надсилання з текстом 'Пошук'


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('date_edited', 'book')
        rating = forms.IntegerField(min_value=0, max_value=5)
