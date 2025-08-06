from django import forms
from .models import OPPatient

class OPPatientForm(forms.ModelForm):
    class Meta:
        model = OPPatient
        fields = '__all__'
        widgets = {
            'op_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}), 
            'description': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
        }