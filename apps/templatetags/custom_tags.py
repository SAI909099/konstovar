from django import template
from apps.models import Category  # Adjust import based on your app's name

register = template.Library()

@register.simple_tag(takes_context=True)
def recursetree(context, category):
    request = context['request']
    categories = category.children.all()
    return {'categories': categories}
