#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from core.models import Chapter, Tariff
from person.models import Patient


class TariffForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TariffForm, self).__init__(*args, **kwargs)
        chapter = Chapter.objects.all().order_by('number')
        chapter_name = lambda num, name: 'Capitulo ' + str(num) + ' - ' + name.capitalize()
        self.fields['chapter'] = forms.ChoiceField(
            widget=forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                    'data-live-search': 'true',
                    'data-size': '10',
                }
            ),
            choices=[(c.id, chapter_name(c.number, c.name)) for c in chapter],
        )


class PatientSelectForm(forms.Form):
    def __init__(self, dentist_id, *args, **kwargs):
        super(PatientSelectForm, self).__init__(*args, **kwargs)
        patients = Patient.objects.filter(
            dentist__id=dentist_id
        )
        p_info = lambda name, id: name.capitalize() + ' - ' + id
        self.fields['patient'] = forms.ChoiceField(
            empty_value='No hay selección.',
            widget=forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                    'data-live-search': 'true',
                    'data-size': '5',
                }
            ),
            choices=[(p.id, p_info(p.get_full_name(), p.subsidiary_number)) for p in patients]
        )
