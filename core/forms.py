from django import forms
from django.contrib.auth.models import User
from django.core import validators
from core.models import *

class DateInput(forms.DateInput):
   input_type = 'date'

class additem_form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Item Name '}))
    expiry_D = forms.DateField(widget=DateInput)
    price = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Price'}))
    quantity  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Quantity '}))

    class Meta():
	     model = inventory
	     fields = '__all__'

class checkout_form(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Item Name '}))
    studentID = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Student ID '}))
    quantity  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Quantity '}))

class provider_form(forms.Form):
    donor_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Provider Name '}))
    user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Provider Name'}))
    CHS = [('Individual', 'Individual'), ('Organisation', 'Organisation')]
    donor_status = forms.CharField(widget=forms.Select(attrs={'style':'display:inline;'},choices=CHS))
    CHS1 = [('True', 'Yes'), ('False', 'No')]
    anonymus_status = forms.CharField(widget=forms.Select(attrs={'style':'display:inline;'},choices=CHS1))