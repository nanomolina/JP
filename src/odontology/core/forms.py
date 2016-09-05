from django import forms
from core.models import Chapter, Tariff

class TariffForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TariffForm, self).__init__(*args, **kwargs)
        chapter = Chapter.objects.all().order_by('number')

        self.fields['chapter'] = forms.ChoiceField(
            widget=forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                    'data-live-search': 'true',
                    'data-size': '10',
                }
            ),
            choices=[(c.id, 'Capitulo ' + str(c.number)) for c in chapter],
        )
