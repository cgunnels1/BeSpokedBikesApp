from django.db import models


# Create your models here.

class Customer(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    startDate = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.firstName
