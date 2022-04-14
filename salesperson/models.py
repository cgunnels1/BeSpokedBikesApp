from django.db import models


# Create your models here.

class Salesperson(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=12)
    startDate = models.DateField(auto_now=False, auto_now_add=False)
    terminationDate = models.DateField(auto_now=False, auto_now_add=False)
    manager = models.CharField(max_length=50)

    def __str__(self):
        return self.firstName
