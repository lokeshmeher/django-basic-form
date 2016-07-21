from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


@python_2_unicode_compatible
class ShoppingChoice(models.Model):
    PRICE_RANGE_CHOICES = (
        ('less than 500', 'less than 500'),
        ('500 to 1000', '500 to 1000'),
        ('1000 to 2000', '1000 to 2000'),
        ('over 2000', 'over 2000'),
    )
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=100)
    price_range = models.CharField(max_length=20, choices=PRICE_RANGE_CHOICES)
    discount_percent = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(90)]
    )
    end_date = models.DateField()

    def __str__(self):
        return self.shop_name[:20] + ('...' if len(self.shop_name)>20 else '')

    def get_absolute_url(self):
        return reverse_lazy()
