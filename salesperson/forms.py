# forms.py
from django import forms
from .models import *


class SalespersonForm(forms.ModelForm):
    class Meta:
        model = Salesperson
        fields = ['firstName', 'lastName', 'address', 'phoneNumber', 'startDate', 'terminationDate', 'manager']
