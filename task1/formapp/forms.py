from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ShoppingChoice


class ShoppingChoiceForm(forms.ModelForm):
    class Meta:
        model = ShoppingChoice
        fields = ['shop_name', 'price_range', 'discount_percent', 'end_date']
        widgets = {
            'end_date': forms.SelectDateWidget,
        }


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
