from django import forms
from person.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = (
            'first_name', 'last_name', 'subsidiary_number', 'social_work',
            'incumbent', 'family_group', 'relationship', 'birth_date', 'street',
            'number', 'suburb', 'locality', 'tel', 'Workplace_holder',
            'hierarchy', 'email', 'gender'
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
            'subsidiary_number': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'social_work': forms.Select(
                attrs={
                    'class': 'selectpicker form-control',
                    'data-live-search': 'true',
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
                    'style': 'width: 80%',
                }
            ),
            'number': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'style': 'width: 20%',
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
        }
