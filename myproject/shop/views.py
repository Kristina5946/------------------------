from django.shortcuts import render
from .models import Product
from .forms import OrderForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def order_create(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        # перенаправление или сообщение об успехе
    return render(request, 'shop/order_create.html', {'form': form})
