# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from person.models import Patient, Dentist, Odontogram, SocialWork


class PatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['social_work'].queryset = SocialWork.objects.order_by('initial')

    class Meta:
        model = Patient
        fields = (
            'first_name', 'last_name', 'subsidiary_number', 'social_work',
            'incumbent', 'family_group', 'relationship', 'birth_date', 'street',
            'number', 'floor', 'apartment', 'suburb', 'locality', 'tel', 'cel_phone',
            'Workplace_holder', 'hierarchy', 'email', 'gender', 'derivation',
            'neighborhood'
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
                    'style': 'width: 26%',
                    'placeholder': 'Calle',
                }
            ),
            'number': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'style': 'width: 14%',
                    'placeholder': 'Número',
                }
            ),
            'floor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'width: 14%',
                    'placeholder': 'Piso',
                }
            ),
            'apartment': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'width: 14%',
                    'placeholder': 'Dpto',
                }
            ),
            'neighborhood': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'width: 21%',
                    'placeholder': 'Barrio',
                }
            ),
            'suburb': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'width: 50%',
                }
            ),
            'locality': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'width: 50%',
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
        }


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


class PasswordForm(forms.Form):
    old_password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    new_password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    confirm_password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
