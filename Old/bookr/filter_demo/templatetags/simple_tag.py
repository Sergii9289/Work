from django import template

register = template.Library()


@register.simple_tag  # simple_tag decorator
def greet_user(message, username):
    return f'{message}, {username}!!!'


@register.simple_tag(takes_context=True)  # # simple_tag decorator, which takes context from view
def contextual_greet_user(context, message):
    username = context['username']
    return f'{message}, {username}!!!'
