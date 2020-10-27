from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView

# Create your views here.
class Home(ListView):
    model = Product
    template_name = 'products/base.html'
    
