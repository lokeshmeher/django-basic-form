from django.forms import ModelForm

from .models import ShoppingChoice


class ShoppingChoiceForm(ModelForm):
    class Meta:
        model = ShoppingChoice
        fields = ['shop_name', 'discount', 'price', 'end_date']
