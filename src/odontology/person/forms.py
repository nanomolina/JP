# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from person.models import Patient, Dentist, Odontogram, SocialWork
from core.models import Day


class PatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['social_work'].queryset = SocialWork.objects.order_by('initial')
        self.fields['preferred_day'].queryset = Day.objects.all()

    class Meta:
        model = Patient
        fields = (
            'first_name', 'last_name', 'subsidiary_number', 'social_work', 'plan',
            'incumbent', 'family_group', 'relationship', 'birth_date', 'street',
            'number', 'floor', 'apartment', 'suburb', 'locality', 'tel', 'cel_phone',
            'Workplace_holder', 'hierarchy', 'email', 'gender', 'derivation',
            'neighborhood', 'dni', 'alias', 'occupation', 'preferred_day', 'turn',
            'companion',
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'subsidiary_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'social_work': forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                    'data-live-search': 'true',
                    'data-size': '8',
                }
            ),
            'plan': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'incumbent': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'family_group': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'relationship': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'birth_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'street': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'number': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'floor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'apartment': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'neighborhood': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'suburb': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'locality': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'cel_phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'Workplace_holder': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'hierarchy': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                }
            ),
            'derivation': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'dni': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'alias': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'occupation': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'preferred_day': forms.SelectMultiple(
                attrs={
                    'class': 'selectpicker form-control',
                }
            ),
            'turn': forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                }
            ),
            'companion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = (
            'picture',
        )
    picture = forms.ImageField()


class OdontogramForm(forms.ModelForm):
    class Meta:
        model = Odontogram
        fields = (
            'teeth_number', 'observations'
        )
        widgets = {
            'teeth_number': forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                    'data-live-search': 'true',
                    'data-size': '8',
                }
            ),
            'observations': forms.Textarea(
                attrs={
                    'id': 'id_odont_observations',
                    'class': 'form-control',
                    'rows': '2',
                }
            ),
        }


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email'
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class DentistForm(forms.ModelForm):
    class Meta:
        model = Dentist
        fields = (
            'circle', 'register_number', 'carrying_home'
        )
        widgets = {
            'circle': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'register_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'carrying_home': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class PatientSelectForm(forms.Form):
    def __init__(self, dentist_id, *args, **kwargs):
        super(PatientSelectForm, self).__init__(*args, **kwargs)
        patients = Patient.objects.filter(
            dentist__id=dentist_id
        )
        self.fields['patient'] = forms.MultipleChoiceField(
            widget=forms.SelectMultiple(
                attrs={
                    'class': 'selectpicker form-control',
                    'data-live-search': 'true',
                    'data-size': '10',
                }
            ),
            choices=[(p.id, str(p)) for p in patients]
        )


class TeethSelectForm(forms.Form):
    def __init__(self, patient, *args, **kwargs):
        from person.models import TOOTH_STATUS
        super(TeethSelectForm, self).__init__(*args, **kwargs)
        teeth = patient.odontogram.get_teeth_ordered()
        self.fields['teeth'] = forms.MultipleChoiceField(
            widget=forms.SelectMultiple(
                attrs={
                    'class': 'selectpicker form-control',
                    'data-live-search': 'true',
                    'data-size': '10',
                    'id': 'teeth_selected'
                }
            ),
            choices=[(tooth.id, str(tooth.number)) for tooth in teeth]
        )
        self.fields['tooth_status'] = forms.ChoiceField(
            widget=forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                }
            ),
            choices=[status for status in TOOTH_STATUS]
        )
