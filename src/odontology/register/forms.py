from django import forms
from register.models import Apross, DetailApross, Faces, Benefit, DetailBenefit

class AprossForm(forms.ModelForm):
    class Meta:
        model = Apross
        fields = (
            'managment_code1', 'managment_code2',
            'managment_code3', 'rx_amount',
        )
        widgets = {
            'managment_code1': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '0',
                }
            ),
            'managment_code2': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '0',
                }
            ),
            'managment_code3': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '0',
                }
            ),
            'rx_amount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '0',
                }
            )
        }


class detailAprossForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(detailAprossForm, self).__init__(*args, **kwargs)
        self.fields['faces'].queryset = Faces.objects.all()

    class Meta:
        model = DetailApross
        fields = (
            'day', 'work_done', 'practic_code',
            'element', 'faces'
        )
        widgets = {
            'day': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'work_done': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'practic_code': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'element': forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                    'data-live-search': 'true',
                    'data-size': '8',
                }
            ),
            'faces': forms.SelectMultiple(
                attrs={
                    'class': 'selectpicker form-control',
                }
            )
        }


class BenefitForm(forms.ModelForm):
    class Meta:
        model = Benefit
        fields = (
            'primary_entity', 'principal_code',
            'managment_code', 'rx_amount'
        )
        widgets = {
            'primary_entity': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'principal_code': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'managment_code': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'rx_amount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }


class detailBenefitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(detailBenefitForm, self).__init__(*args, **kwargs)
        self.fields['faces'].queryset = Faces.objects.all()

    class Meta:
        model = DetailBenefit
        fields = (
            'day', 'tooth', 'code', 'faces'
        )
        widgets = {
            'day': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'tooth': forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                    'data-live-search': 'true',
                    'data-size': '8',
                }
            ),
            'code': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'faces': forms.SelectMultiple(
                attrs={
                    'class': 'selectpicker form-control',
                }
            )
        }
