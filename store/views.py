from django.shortcuts import render
from django .http import HttpResponse,Http404
from .models import Product
# Create your views here.

def store_home(request):
    return render(request, "store/store.html")

def product_list(request):
    products = Product.objects.all()
    context= {
        'products':products,
    }
    return render(request, 'store/product_list.html', context)

def test(request):
    return render(request, 'store/test.html')
