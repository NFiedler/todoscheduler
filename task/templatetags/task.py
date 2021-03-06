from datetime import date, timedelta

from django import template
from django.contrib.humanize.templatetags.humanize import naturalday
from django.utils.formats import date_format

register = template.Library()


@register.filter
def multiply(value, arg):
    return value * arg


@register.filter
def to_str(value) -> str:
    return str(value)


@register.filter
def more_natural_day(value: date) -> str:
    if timedelta(days=1) < value - date.today() <= timedelta(days=6):
        return date_format(value, 'l')
    return naturalday(value)
