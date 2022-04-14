# forms.py
from django import forms
from .models import *

class Discount(forms.ModelForm):

	class Meta:
		model = Discount
		fields = ['product', 'beginDate', 'endDate', 'discountPercentage']
