from django import forms
from .models import *

class DojoForm(forms.ModelForm):
    class Meta:
        model = Dojo
        fields = ['name', 'city', 'state', 'desc']


class NinjaForm(forms.ModelForm):
    class Meta:
        model = Ninja
        fields = ['first_name', 'last_name', 'dojo']