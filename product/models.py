from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    purchase_price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity_on_hand = models.IntegerField()
    commission_percentage = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name
