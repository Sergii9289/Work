from django import template

register = template.Library()

@register.filter
def explode(value: str, separator):
    return value.split(separator)