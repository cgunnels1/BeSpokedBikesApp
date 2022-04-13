# forms.py
from django import forms
from .models import *

class Customer(forms.ModelForm):

	class Meta:
		model = Customer
		fields = ['firstName', 'lastName', 'address', 'phone', 'startDate']

