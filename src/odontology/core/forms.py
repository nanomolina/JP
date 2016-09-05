from django import forms
from core.models import Chapter, Tariff

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
