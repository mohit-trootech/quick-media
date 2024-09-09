# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.filter(name="format_number")
def format_number(arg):
    """
    format number in K, M, B Formats

    :param arg: The list or iterable to shuffle.
    :return: A new list with elements shuffled.
    """
    try:
        for unit in ["", "K", "M"]:
            if abs(arg) < 1000.0:
                return f"{arg:6.2f}{unit}"
            arg /= 1000.0
        return f"{arg:6.2f}B"
    except TypeError:
        return arg
