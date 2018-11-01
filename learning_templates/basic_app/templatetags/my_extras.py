from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    THIS CUT OUT ALL VAULE OF 'arg' FROM STRING
    """

    return value.replace(arg,'')

# register.filter('cut',cut)