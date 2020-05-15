from django.shortcuts import render
from django.http import HttpResponse
from core.models import *
from core.forms import *

# Create your views here.

def dashboard(request):
	return render(request, "core/dashboard.html")



def checkout(request):
	return render(request, "core/checkout.html")



def impact(request):
	return render(request, "core/impact.html")



def inventory(request):

	item_data = additem_form()
	if (request.method=="POST"):
		item_data = additem_form(request.POST)
		if item_data.is_valid():
			Name = item_data.cleaned_data['name']
			Expiry = item_data.cleaned_data['expiry_D']
			Price = item_data.cleaned_data['price']
			Quantity = item_data.cleaned_data['quantity']
			print(Name)
			print(Expiry)
			print(Price)
			print(Quantity)

	context = {'item_data':item_data}
	return render(request, "core/inventory.html", context)
