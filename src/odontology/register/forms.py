from django import forms
from register.models import Apross, DetailApross, Faces, Benefit, DetailBenefit, Radiography

class AprossForm(forms.ModelForm):
    class Meta:
        model = Apross
        fields = (
            'managment_code1', 'managment_code2', 'managment_code3',
            'managment_code4', 'rx_amount', 'observations'
        )
        widgets = {
            'managment_code1': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'managment_code2': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'managment_code3': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'managment_code4': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'rx_amount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'observations': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '2',
                }
            ),
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
            'managment_code', 'rx_amount', 'observations'
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
            'managment_code': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'rx_amount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'observations': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '2',
                }
            ),
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

class RadiographyForm(forms.ModelForm):
    class Meta:
        model = Radiography
        fields = (
            'part_number_1', 'finality_1',
            'part_number_2', 'finality_2',
            'part_number_3', 'finality_3',
        )
        widgets = {
            'part_number_1': forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                    'data-live-search': 'true',
                    'data-size': '8',
                }
            ),
            'finality_1': forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                }
            ),
            'part_number_2': forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                    'data-live-search': 'true',
                    'data-size': '8',
                }
            ),
            'finality_2': forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                }
            ),
            'part_number_3': forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                    'data-live-search': 'true',
                    'data-size': '8',
                }
            ),
            'finality_3': forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                }
            ),
        }
