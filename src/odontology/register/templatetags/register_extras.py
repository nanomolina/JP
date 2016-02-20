from django import template
from register.models import DetailApross
from register.forms import detailAprossForm

register = template.Library()

@register.filter(name='detail_form_instance')
def detail_form_instance(detail_id):
    """Removes all values of arg from the given string"""
    detail = DetailApross.objects.get(id=detail_id)
    form = detailAprossForm(instance=detail)
    return form
