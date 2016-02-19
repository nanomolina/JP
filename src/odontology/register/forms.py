from django import forms
from register.models import Apross, DetailApross

class AprossForm(forms.ModelForm):
    class Meta:
        model = Apross
        fields = (
            'managment_code1', 'managment_code2',
            'managment_code3', 'rx_amount',
        )
        widgets = {
            'managment_code1': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': '0',
                }
            ),
            'managment_code2': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': '0',
                }
            ),
            'managment_code3': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': '0',
                }
            ),
            'rx_amount': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': '0',
                }
            )
        }


class detailAprossForm(forms.ModelForm):
    class Meta:
        model = DetailApross
        fields = (
            'day', 'work_done', 'practic_code',
            'element', 'faces'
        )
        widgets = {
            'day': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'work_done': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'practic_code': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'element': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'faces': forms.SelectMultiple(
                attrs = {
                    'class': 'selectpicker form-control',
                }
            ),
        }
