from django.shortcuts import render
from .models import Product



def products(request):
    x = Product.objects.all().filter(active=True)
    q = Product.objects.all().filter(activetoday=True)
    
    # c = Cups.objects.all().filter(active=True)
    # set = {'biscut': x.filter(category__exact='photo'),'cups': Cups.objects.all().filter(active=True),}
    return render(request, 'products/product.html', {'biscut': x.filter(category__exact='بسكوت'),'cups': x.filter(category__exact='كوب'),'drink': x.filter(category__exact='مشروب'),'todayw': q})