from django import forms
from register.models import (Apross, DetailApross,
    Faces, Benefit, DetailBenefit, Radiography, Record)
from core.models import Chapter, Tariff

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
        tariffs = Tariff.objects.all().order_by('chapter__number','index','sub_index')
        self.fields['practic_code'] = forms.ChoiceField(
            widget=forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                    'data-live-search': 'true',
                    'data-size': '8',
                }
            ),
            choices=[(t.id, t.get_code()) for t in tariffs],
        )

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


class RecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecordForm, self).__init__(*args, **kwargs)
        self.fields['tariff'].queryset = Tariff.objects.all()

    class Meta:
        model = Record
        fields = (
            'date', 'treatment', 'faces', 'tooth', 'period_so',
            'state', 'assistance', 'observations', 'code',
            'to_account', 'to_social_work', 'tariff'
        )
        widgets = {
            'date': forms.DateTimeInput(
                format=('%d/%m/%Y %I:%M'),
                attrs={
                    'class': 'form-control',
                }
            ),
            'treatment': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'faces': forms.SelectMultiple(
                attrs={
                    'class': 'selectpicker form-control',
                }
            ),
            'tooth': forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                    'data-live-search': 'true',
                    'data-size': '8',
                }
            ),
            'period_so': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'state': forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                }
            ),
            'assistance': forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                }
            ),
            'observations': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '2',
                }
            ),
            'code': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'tariff': forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                    'data-live-search': 'true',
                    'data-size': '8',
                }
            ),
            'to_account': forms.CheckboxInput(),
            'to_social_work': forms.CheckboxInput(),

        }


class AccountingForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = (
            'debit', 'havings',
        )
        widgets = {
            'debit': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'havings': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
