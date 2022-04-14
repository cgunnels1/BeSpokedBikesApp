from django.db import models


# Create your models here.

class Discount(models.Model):
    product = models.CharField(max_length=50)
    beginDate = models.DateField(auto_now=False, auto_now_add=False)
    endDate = models.DateField(auto_now=False, auto_now_add=False)
    discountPercentage = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.product
