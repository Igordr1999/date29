from django import forms
from django.contrib.auth.models import User
from main.models import Shop


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('name', 'phone', 'address', 'logo')
