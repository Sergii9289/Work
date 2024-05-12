from django.db import models
from django.contrib import auth


class Publisher(models.Model):
    name = models.CharField(
        max_length=50,
        help_text='The name of Publisher')
    website = models.URLField(
        help_text='The Publisher website')
    email = models.EmailField(
        help_text='The Publisher Email')

    def __str__(self):
        return self.name


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
    cover = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    sample = models.FileField(upload_to='book_samples/', null=True, blank=True)


    def __str__(self):
        return f'{self.title}, {self.isbn}'


class Contributor(models.Model):
    first_names = models.CharField(
        max_length=50,
        help_text='Contributor first name or names.')
    last_names = models.CharField(
        max_length=50,
        help_text='Contributor last name or names.')
    email = models.EmailField(
        help_text='Contact email for the contributor.')

    def initialed_name(self):
        names = list(self.first_names.split())
        initials = ''
        for name in names:
            initials += name[0]
        return f'{self.last_names}, {initials}'

    def __str__(self):
        return self.initialed_name()


class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = 'AUTHOR', 'Author'
        CO_AUTHOR = 'CO_AUTHOR', 'Co-Author'
        EDITOR = 'EDITOR', 'Editor'

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.PROTECT)
    role = models.CharField(
        verbose_name='The role this contributor had in book',
        choices=ContributionRole.choices,
        max_length=20)


class Review(models.Model):
    content = models.TextField(help_text='Review text.')
    rating = models.IntegerField(help_text='Rating the review has given.')
    date_created = models.DateTimeField(
        auto_now_add=True,
        help_text='Date and time the review was created.')
    date_edited = models.DateTimeField(
        null=True,
        help_text='Date and time the review was last edited.')
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             help_text='Book that this review is for.')