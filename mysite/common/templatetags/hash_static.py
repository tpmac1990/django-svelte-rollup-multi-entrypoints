from django import template
from django.templatetags.static import static
from django.conf import settings
import json
import os
import re
from django.utils.safestring import mark_safe

MANIFEST_FILENAME = 'manifest.json'
JS = 'js'
CSS = 'css'

register = template.Library()

def _split_path(path):
    file_name = path.split('/')[-1]
    file_dir = path.replace(file_name, '')
    ext = file_name.split('.')[-1]
    no_ext_name = file_name.replace(f'.{ext}', '')
    return file_dir, file_name, no_ext_name, ext


@register.simple_tag()
def hash_static(relative_path):

    if not (relative_path.endswith(JS) or relative_path.endswith(CSS)):
        raise Exception(f'"{relative_path}" is not a valid path.')

    file_dir, file_name, no_ext_name, ext = _split_path(relative_path)

    if ext == JS:

        if not os.path.exists(MANIFEST_FILENAME):
            raise Exception(f'"{MANIFEST_FILENAME}" does not exist at the root of your project.')

        with open(MANIFEST_FILENAME, 'r') as manifest:
            data = json.load(manifest)

        if not file_name in data:
            raise Exception(f'"{file_name}" does not exist in "{MANIFEST_FILENAME}"')

        path = static(os.path.join(file_dir, data[file_name]))
        return mark_safe(f'<script type="module" defer src="{path}"></script>')

    if ext == CSS:

        dir_list = os.listdir(os.path.join(settings.STATICFILES_DIRS[0], file_dir))
        # NameError: name 'no_ext_name' is not defined
        # return static(os.path.join(file_dir, list(filter(lambda v: re.match(rf"{no_ext_name}.*\.{ext}", v), dir_list))[0]))
        ls = []
        for x in dir_list:
            if re.match(rf"{no_ext_name}.*\.{ext}", x):
                ls.append(x)

        path = static(os.path.join(file_dir, ls[0]))
        return mark_safe(f'<link rel="stylesheet" type="text/css" href="{path}" />')
