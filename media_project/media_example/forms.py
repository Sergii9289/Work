from django import forms
from .models import ExampleModel1


class UploadForm(forms.Form):
    file_upload = forms.ImageField()


class DateInput(forms.Form):
    date_input = forms.DateField(widget=forms.DateInput(attrs={"type": 'date'}))


class FileUploadForm(forms.Form):
    uploaded_file = forms.FileField()


class UploadForm1(forms.Form):
    image_upload = forms.ImageField()
    file_upload = forms.FileField()

class ExampleModelForm(forms.ModelForm):
    class Meta:
        model = ExampleModel1
        fields = '__all__'

