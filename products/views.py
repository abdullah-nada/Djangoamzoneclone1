from django.shortcuts import render

# Create your views here.

from .models import Product,Brand ,Review

from django.views.generic import ListView , DetailView


class productlist(ListView):
    model=Product
    template_name='products\product_list.html'


class productdetail(DetailView):
    model=Product
    template_name='products\product_detail.html'




