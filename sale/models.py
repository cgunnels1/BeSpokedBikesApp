from django.db import models


# Create your models here.
class Sale(models.Model):
    product = models.CharField(max_length=50)
    customer = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    salesperson = models.CharField(max_length=50)
    salespersonCommission = models.DecimalField(max_digits=6, decimal_places=2, default=None)

    def __str__(self):
        return self.product

# Product, Customer, Date, Price, Salesperson, and Salesperson Commission.
