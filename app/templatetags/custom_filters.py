from django import template

register = template.Library()

@register.filter(name='format_rut')
def format_rut(value):
    rut = str(value)
    formatted_rut = f"{rut[:-7]}.{rut[-7:-4]}.{rut[-4:-1]}-{rut[-1]}"
    return formatted_rut