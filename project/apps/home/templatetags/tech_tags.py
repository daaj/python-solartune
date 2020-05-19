from django import template
from project.apps.home.models import Technology

register = template.Library()


@register.inclusion_tag('includes/technologies.html', takes_context=True)
def technologies(context):
    return {
        'technologies': Technology.objects.all(),
        'request': context['request'],
    }
