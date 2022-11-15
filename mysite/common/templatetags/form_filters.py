from django import template
import re
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='cut')
def cut(value):
    matches = re.findall(r'<input type="file"(?:.*?)>', value)
    for match in matches:
        with_span = '<label class="custom-file-upload">' + match + 'Custom Upload</label>'
        new_value = value.replace(match, with_span)
    return mark_safe(new_value)