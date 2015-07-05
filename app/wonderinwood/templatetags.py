from django import template

register = template.Library()

@register.filter
def firstsentence(value):
    return "{}.".format(value.split('.')[0])