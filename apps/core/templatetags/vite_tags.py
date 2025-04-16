# apps/core/templatetags/vite_tags.py

import json
import os
from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def vite_asset(asset_name):
    manifest_path = os.path.join(settings.BASE_DIR, 'static/vue/manifest.json')
    try:
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        return f"/static/vue/{manifest[asset_name]['file']}"
    except Exception:
        return ""


# @register.simple_tag
# def vue_asset(filetype):
#     """
#     Usage: {% vue_asset 'js' %} or {% vue_asset 'css' %}
#     """
#     manifest_path = os.path.join(settings.BASE_DIR, 'static/vue/manifest.json')
#     with open(manifest_path, 'r') as f:
#         manifest = json.load(f)
    
#     entry = manifest.get('index.html') or next(iter(manifest.values()))
#     if filetype == 'js':
#         return f"/static/vue/{entry['file']}"
#     elif filetype == 'css':
#         css_file = entry.get('css', [])[0] if 'css' in entry else None
#         return f"/static/vue/{css_file}" if css_file else ''
#     return ''