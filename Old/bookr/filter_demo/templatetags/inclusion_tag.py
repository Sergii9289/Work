from django import template
register = template.Library()

@register.inclusion_tag('book_list.html')  # name of template, which will be rendered in another
def book_list(books: dict):  # logic
    book_list = [book_name for book_name, book_author in books.items()]
    return {'book_list': book_list}
