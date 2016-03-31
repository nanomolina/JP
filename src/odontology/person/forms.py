from django import forms
from person.models import Patient, Odontogram, SocialWork


class PatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['social_work'].queryset = SocialWork.objects.order_by('initial')

    class Meta:
        model = Patient
        fields = (
            'first_name', 'last_name', 'subsidiary_number', 'social_work',
            'incumbent', 'family_group', 'relationship', 'birth_date', 'street',
            'number', 'floor', 'apartment', 'suburb', 'locality', 'tel',
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
                    'style': 'width: 34%',
                }
            ),
            'number': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'style': 'width: 25%',
                }
            ),
            'floor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'width: 20%',
                }
            ),
            'apartment': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'width: 20%',
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
                    'rows': '5',
                }
            ),
        }
