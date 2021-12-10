from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from myapp.models import Order, Product, Client


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'product', 'num_units']
        widgets = {
            'client': forms.RadioSelect
        }
        labels = {
            'num_units': 'Quantity',
            'client': 'Client Name'
        }


# class InterestForm2(forms.ModelForm):
#     CHOICES = [
#         (1, 'YES'),
#         (0, 'NO')
#     ]
#     interested = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
#     quantity = forms.IntegerField(initial=1)
#     comment = forms.CharField(widget=forms.Textarea, required=False, label='Additional Comment')
#
#     class Meta:
#         model = Product
#         fields = ['interested']


class InterestForm(forms.Form):
    CHOICES = [
        (1, 'YES'),
        (0, 'NO')
    ]
    interested = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    quantity = forms.IntegerField(initial=1)
    comment = forms.CharField(widget=forms.Textarea, required=False, label='Additional Comment')


class RegisterForm(UserCreationForm):
    class Meta:
        model = Client
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UploadPhoto(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['photo']
