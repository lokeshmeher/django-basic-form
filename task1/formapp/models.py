from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Maximum price allowed is Rs 1 lakh.
class ShoppingChoice(models.Model):
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=100)
    discount = models.IntegerField('Discount percent')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    end_date = models.DateField(auto_add_now=True)
