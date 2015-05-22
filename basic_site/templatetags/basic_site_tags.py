from __future__ import absolute_import

from django import template

from basic_site.models import BasicBlock

register = template.Library()


@register.assignment_tag()
def get_embedded_block(slug):
    try:
        snippet = BasicBlock.objects.get(slug=slug)
    except BasicBlock.DoesNotExist:
        snippet = None

    return snippet
