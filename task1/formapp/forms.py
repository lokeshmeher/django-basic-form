from django.forms import ModelForm, ValidationError
from django.contrib.admin.widgets import AdminDateWidget

from .models import ShoppingChoice


class ShoppingChoiceForm(ModelForm):
    class Meta:
        model = ShoppingChoice
        fields = ['shop_name', 'price_range', 'discount_percent', 'end_date']
        widgets = {
            'end_date': AdminDateWidget,
        }
