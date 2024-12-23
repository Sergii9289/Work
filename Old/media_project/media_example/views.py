import os.path
from PIL import Image
from django.shortcuts import render
from django.conf import settings
from .forms import *
from .models import *
from django.shortcuts import redirect
from io import BytesIO
from django.core.files.images import ImageFile


def index(request, pk):
    m = ImageExampleModel.objects.get(pk=pk)
    uploaded_image = request.FILES['image_field']
    image = Image.open(uploaded_image)
    image.thumbnail((150, 150))
    image_data = BytesIO()
    image.save(fp=image_data, format=uploaded_image.format)
    image_file = ImageFile(image_data)
    m.image_field.save(uploaded_image.name, image_file)
    return redirect('/success-url/')



def media_example1(request):
    instance = None
    if request.method == 'POST':
        form = UploadForm1(request.POST, request.FILES)
        if form.is_valid():
            instance = ExampleModel1()
            instance.file_field = form.cleaned_data['file_upload']
            instance.image_field = form.cleaned_data['image_upload']
            instance.save()
    else:
        form = UploadForm1()
    return render(request, 'media-example1.html', {'form': form, 'instance': instance})


def media_example(request):
    if request.method == 'POST':
        save_path = settings.MEDIA_ROOT / request.FILES['file_upload'].name

        with open(save_path, 'wb') as output_file:
            for chunk in request.FILES['file_upload'].chunks():
                output_file.write(chunk)
    return render(request, 'media-example.html')


def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            save_path = os.path.join(settings.MEDIA_ROOT, request.FILES['file_upload'].name)

            image = Image.open(form.cleaned_data['file_upload'])
            image.thumbnail((50, 50))
            image.save(save_path)
    else:
        form = UploadForm()
    return render(request, 'media-example-with-form.html', {'form': form})


def model_upload(request):
    if request.method == 'POST':
        m = ExampleModel()  # Create a new ExampleModel instance
        m.file_field = request.FILES['file_upload']
        m.save()
    return render(request, 'media-example.html')


def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            save_path = os.path.join(settings.MEDIA_ROOT, request.FILES['uploaded_file'].name)

            with open(save_path, 'wb') as output_file:
                for chunk in request.FILES['uploaded_file'].chunks():
                    output_file.write(chunk)
    else:
        form = FileUploadForm()
    return render(request, 'media-example-with-form.html', {'form': form})


def file_upload_with_model(request, model_pk):
    form = FileUploadForm(request.POST, request.FILES)
    if form.is_valid():
        m = ExampleModel.objects.get(pk=model_pk)
        m.file_field = form.cleaned_data['uploaded_file']
        m.save()
    return render(request, 'media-example-with-form.html', {'form': form})


def image_model_upload(request):
    if request.method == 'POST':
        m = ImageExampleModel()  # Create a new ExampleModel instance
        m.image = request.FILES['file_upload']
        m.save()
    return render(request, 'media-example.html')


def model_form_upload(request):
    instance = None
    if request.method == 'POST':
        form = ExampleModelForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
    else:
        form = ExampleModelForm()
    return render(request, 'media-example1.html', {'form': form, 'instance': instance})
