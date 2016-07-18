from django.forms import ModelForm

from .models import ShoppingChoice

class ShoppingChoiceForm(ModelForm):
    class Meta:
        model = ShoppingChoice
        exclude = ['submitted_by']
