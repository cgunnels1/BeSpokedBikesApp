from django.db import models

# Create your models here.
class Sale(models.Model):
    product = models.CharField(max_length=50)
    salesperson = models.CharField(max_length=50)
    customer = models.CharField(max_length=50)
    salesDate = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.product

#Product, Salesperson, Customer, Sales Date