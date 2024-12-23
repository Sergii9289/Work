from django.contrib import admin
from .models import *


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn__exact', 'publisher__name')
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13', 'has_isbn')
    list_filter = ('publisher', 'publication_date')


    @admin.display(ordering='isbn',
                   description='ISBN number',
                   empty_value='-/-')
    def isbn13(self, obj):
        return f'{obj.isbn[0:3]} - {obj.isbn[3:4]} ' \
               f'- {obj.isbn[4:6]}' \
               f' - {obj.isbn[6:12]} - {obj.isbn[12:13]}'

    def get_publisher(self, obj):
        return obj.publisher.name

    @admin.display(boolean=True, description='Has ISBN')
    def has_isbn(self, obj):
        return bool(obj.isbn)


class ReviewAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('creator', 'book')}),
                 ('Review content', {'fields': ('content', 'rating')}))


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    search_fields = ('last_names__startswith', 'first_names')
    list_filter = ('last_names',)


# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)
