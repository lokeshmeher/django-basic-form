from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class ShoppingChoice(models.Model):
    PRICE_RANGE_CHOICES = (
        ('<500', 'less than 500'),
        ('500-1000', '500 to 1000'),
        ('1000-2000', '1000 to 2000'),
        ('>2000', 'over 2000'),
    )
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=100)
    price_range = models.CharField(max_length=20, choices=PRICE_RANGE_CHOICES)
    discount_percent = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(90)]
    )
    end_date = models.DateField()
