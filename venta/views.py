from django.shortcuts import render
from .models import Category, Product


def home(request):
    return render(request, 'venta/index.html')


def admin(request):
    return render(request, 'venta/admin.html')


def cart(request):
    return render(request, 'venta/cart.html')


def category(request):
    ListCategory = Category.objects.all()
    datos = {
        'Category': ListCategory
    }
    return render(request, 'venta/category.html', datos)


def checkout(request):
    return render(request, 'venta/checkout.html')


def contact(request):
    return render(request, 'venta/contact.html')


def login(request):
    return render(request, 'venta/login.html')


def account(request):
    return render(request, 'venta/account.html')


def productDet(request):
    return render(request, 'venta/product-det.html')


def productList(request):
    productList = Product.objects.all()
    datos = {
        'Product': productList
    }
    return render(request, 'venta/product-list.html', datos)


def wishlist(request):
    return render(request, 'venta/wishlist.html')
