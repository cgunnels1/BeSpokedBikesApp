# forms.py
from django import forms
from .models import *

class Sale(forms.ModelForm):

	class Meta:
		model = Sale
		fields = ['product' , 'customer' ,'date' , 'price' , 'salesperson' , 'salespersonCommission']

