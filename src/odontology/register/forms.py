from django import forms
from register.models import Apross

    class AprossForm(forms.ModelForm):
        class Meta:
            model = Apross
            fields = (
                'date', 'managment_code1', 'managment_code2',
                'managment_code3', 'rx_amount', 'carrying_home'
            )
            widgets = {
                'date' = forms.DateInput(
                    attrs = {
                        'class': 'form-control',
                    }
                ),
                'managment_code1' = forms.TextInput(
                    attrs = {
                        'class': 'form-control',
                    }
                ),
                'managment_code2' = forms.TextInput(
                    attrs = {
                        'class': 'form-control',
                    }
                ),
                'managment_code3' = forms.TextInput(
                    attrs = {
                        'class': 'form-control',
                    }
                ),
                'rx_amount' = forms.TextInput(
                    attrs = {
                        'class': 'form-control',
                    }
                ),
                'carrying_home' = forms.TextInput(
                    attrs = {
                        'class': 'form-control',
                    }
                ),
            }

    class detailAprossForm(forms.ModelForm):
        class Meta:
            model = Apross
            fields = (
                'date', 'work_done', 'practic_code',
                'element', 'faces'
            )
            widgets = {
                'date' = forms.DateInput(
                    attrs = {
                        'class': 'form-control',
                    }
                ),
                'work_done' = forms.TextInput(
                    attrs = {
                        'class': 'form-control',
                    }
                ),
                'practic_code' = forms.NumberInput(
                    attrs = {
                        'class': 'form-control',
                    }
                ),
                'element' = forms.NumberInput(
                    attrs = {
                        'class': 'form-control',
                    }
                ),
                'faces' = forms.SelectMultiple(
                    attrs = {
                        'class': 'form-control',
                    }
                ),
            }