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
        p_info = lambda name, id: name.upper() + ' - ' + id if id else name.upper()
        choices = [('', '---------')]
        for p in patients:
            choices.append((p.id, p_info(p.get_full_name(), p.subsidiary_number)))
        self.fields['patient'] = forms.ChoiceField(
            widget=forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                    'data-live-search': 'true',
                    'data-size': '8',
                }
            ),
            choices=choices
        )
