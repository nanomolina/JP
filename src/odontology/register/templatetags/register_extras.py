from django import template
from register.models import DetailApross, DetailBenefit
from register.forms import detailAprossForm, detailBenefitForm

register = template.Library()

@register.filter(name='detail_form_instance')
def detail_form_instance(detail_id):
    """Removes all values of arg from the given string"""
    detail = DetailApross.objects.get(id=detail_id)
    form = detailAprossForm(instance=detail)
    return form


@register.filter(name='benefit_detail_form')
def benefit_detail_form(detail_id):
    """Return a form of the given benefit detail"""
    detail = DetailBenefit.objects.get(id=detail_id)
    form = detailBenefitForm(instance=detail)
    return form
