from django import template
from django.templatetags.static import static
import json
import os

MANIFEST_FILENAME = 'manifest.json'


register = template.Library()

def split_path(path):
    file_name = path.split('/')[-1]
    file_dir = path.replace(file_name, '')
    return file_dir, file_name


@register.simple_tag
def load_bundle(relative_path):

    if not os.path.exists(MANIFEST_FILENAME):
        raise Exception(f'"{MANIFEST_FILENAME}" does not exist at the root of your project.')

    with open(MANIFEST_FILENAME, 'r') as manifest:
        data = json.load(manifest)

    if not '.' in relative_path:
        raise Exception(f'"{relative_path}" is not a valid path.')

    file_dir, file_name = split_path(relative_path)

    if not file_name in data:
        raise Exception(f'"{file_name}" does not exist in "{MANIFEST_FILENAME}"')

    return static(os.path.join(file_dir, data[file_name]))
