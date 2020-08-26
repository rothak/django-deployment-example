from django import template

register = template.Library()

@register.filter(name='cut')  # using a decorator, as we pass one fn into another.
def cut(value, arg):
    """Cut out all the values of 'arg' from the string.

    Args:
        value (str): string to parse.
        arg (str): value to cut out of the string
    """
    return value.replace(arg, '')

# we could register with the method below, but instead we will use decorator as above
# register.filter('cut', cut)  # 'cut' - name of the filter to use in the tags; cut - name of the actual fn().