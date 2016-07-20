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
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:
        model = User
        # Password and password confirmation fields are added by parent class.
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        # password is set by save() of parent class.
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
