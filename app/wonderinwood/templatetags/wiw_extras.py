from django import template

register = template.Library()

@register.filter
def firstsentence(value):
    return value.split('.')[0]