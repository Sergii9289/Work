from django.db import models


# Create your models here.
def user_grouped_file_path(instance, filename):
    return f'files/{filename[0].lower()}/{filename}'


class ExampleModel(models.Model):
    file_field = models.FileField(upload_to='files/')
    # file_field = models.FileField(upload_to='files/%Y/%m/%d/')
    # file_field = models.FileField(upload_to=user_grouped_file_path)
    # username = models.CharField(unique=True, max_length=20)


class ImageExampleModel(models.Model):
    image = models.ImageField(upload_to='images/',
                              height_field='image_height',
                              width_field='image_width')
    image_height = models.IntegerField()
    image_width = models.IntegerField()


class ExampleModel1(models.Model):
    image_field = models.ImageField(upload_to='images/')
    file_field = models.FileField(upload_to='files/')
