# forms.py
from django import forms
from .models import *


class Product(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'manufacturer', 'style', 'purchase_price', 'sale_price', 'quantity_on_hand',
                  'commission_percentage']
