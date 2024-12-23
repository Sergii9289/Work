from django.shortcuts import render
from .forms import UploadForm
from .models import ExampleModel


def media_example(request, pk):
    instance = ExampleModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
    else:
        form = UploadForm()
    return render(request, "media-example.html", {'form': form, 'instance': instance})
