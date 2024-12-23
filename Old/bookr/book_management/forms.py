from django import forms
from .models import Book

class BookForm(forms.ModelForm):  # створюємо клас, пов'язаний з моделлю
    class Meta:  # клас для визначення внутрішніх налаштувань моделі
        model = Book  # посилання на модель
        fields = ['name', 'author']  # які поля будуть використані у формі
