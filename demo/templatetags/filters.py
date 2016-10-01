from django import template

register = template.Library()


@register.filter
def otp_format(value):
    value = str(value).zfill(6)
    return ' '.join([value[:3], value[3:]])
