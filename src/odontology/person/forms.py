from django import forms
from person.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = (
            'first_name', 'last_name',
            'benefit_type',
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'benefit_type': forms.Select(
                attrs = {
                    'class': 'form-control',
                }
            ),
        }
