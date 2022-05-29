from . models import Prescriptions
from django import forms

class Prescriptionsform(forms.ModelForm):
    
    class Meta:
        model = Prescriptions
        fields = ("patient","description","email")