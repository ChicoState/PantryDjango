from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dashboard(request):
	return render(request, "core/dashboard.html")



def checkout(request):
	return render(request, "core/checkout.html")



def impact(request):
	return render(request, "core/impact.html")



def inventory(request):
	return render(request, "core/inventory.html")
