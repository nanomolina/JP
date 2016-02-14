from django import forms
from person.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = (
            'first_name', 'last_name',
            'subsidiary_number',
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
            'subsidiary_number': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'aria-describedby': "helpBlock"
                }
            ),
        }
