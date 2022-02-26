from django import forms
from .models import *

class NTPCForm(forms.ModelForm):
    class Meta:
        model: NTPC
        fields: ['Finance','Monday','Tuesday','Wednesday','Thursday','Friday']

class UPLForm(forms.ModelForm):
    class Meta:
        model: UPL
        fields: ['Finance','Monday','Tuesday','Wednesday','Thursday','Friday']

class SUNPHARMAForm(forms.ModelForm):
    class Meta:
        model: SUNPHARMA
        fields: ['Finance','Monday','Tuesday','Wednesday','Thursday','Friday']