from django.shortcuts import get_object_or_404
from django import template
from person.models import Patient
from register.models import Apross, Benefit, DetailApross, DetailBenefit, Radiography
from register.forms import detailAprossForm, detailBenefitForm, RadiographyForm
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


@register.filter(name='get_radiography_form')
def get_radiography_form(patient_id, bf_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if patient.social_work and patient.social_work.initial == 'APROSS':
        benefit = get_object_or_404(Apross, id=bf_id)
        radiography = Radiography.objects.get(apross=benefit)
    else:
        benefit = get_object_or_404(Benefit, id=bf_id)
        radiography = Radiography.objects.get(benefit=benefit)
    radiography_form = RadiographyForm(instance=radiography)
    return radiography_form

@register.filter(name='get_month_name')
def get_month_name(key):
    MONTHS = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre',
    }
    return MONTHS[key]
