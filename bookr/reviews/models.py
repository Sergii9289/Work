from django.db import models


class Publisher(models.Model):
    name = models.CharField(
        max_length=50,
        help_text='The name of Publisher')
    website = models.URLField(
        help_text='The Publisher website')
    email = models.EmailField(
        help_text='The Publisher Email')


class Book(models.Model):
    title = models.CharField(
        max_length=70,
        help_text='The title of the book')
    publication_date = models.DateField(
        verbose_name='Date the book was publised.')
    isbn = models.CharField(
        max_length=20,
        verbose_name='ISBN number of the book.')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through='BookContributor')


class Contributor(models.Model):
    first_names = models.CharField(
        max_length=50,
        help_text='Contributor first name or names.')
    last_names = models.CharField(
        max_length=50,
        help_text='Contributor last name or names.')
    email = models.EmailField(
        help_text='Contact email for the contributor.')


class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = 'AUTHOR', 'Author'
        CO_AUTHOR = 'CO_AUTHOR', 'Co-Author'
        EDITOR = 'EDITOR', 'Editor'
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(
        verbose_name='The role this contributor had in book',
        choices=ContributionRole.choices,
        max_length=20)