from django import forms
from django.contrib.auth.models import User
from django.core import validators
from core.models import *



class additem_form(forms.ModelForm):
    name = forms.CharField()
    expiry_D = forms.DateField()
    price = forms.FloatField()
    quantity  = forms.CharField()

    class Meta():
	     model = inventory
	     fields = '__all__'