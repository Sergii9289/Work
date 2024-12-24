# Generated by Django 4.2.3 on 2024-11-17 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_book_contributor_review_bookcontributor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='book_covers/'),
        ),
        migrations.AddField(
            model_name='book',
            name='sample',
            field=models.FileField(blank=True, null=True, upload_to='book_samples/'),
        ),
        migrations.AlterField(
            model_name='bookcontributor',
            name='contributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reviews.contributor'),
        ),
    ]
