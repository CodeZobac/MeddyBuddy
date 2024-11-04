from django import forms
from .models import Medication

class FormAddMedication(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['name', 'dosage', 'instructions', 'user']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['user'].initial = self.request.user
        self.fields['user'].widget = forms.HiddenInput()
        
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class FormEditMedication(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ("name", "dosage", "instructions" , 'user')

