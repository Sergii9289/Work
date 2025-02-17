# Generated by Django 4.2.3 on 2024-01-15 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of Publisher', max_length=50)),
                ('website', models.URLField(help_text='The Publisher website')),
                ('email', models.EmailField(help_text='The Publisher Email', max_length=254)),
            ],
        ),
    ]
