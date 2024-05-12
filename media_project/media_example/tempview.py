from io import BytesIO
from PIL import Image
from django.core.files.images import ImageFile
from .models import ImageExampleModel
from django.shortcuts import redirect

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