from django import template

register = template.Library()


@register.filter(name='modulo')
def modulo(value, modulus):
    return value % modulus
