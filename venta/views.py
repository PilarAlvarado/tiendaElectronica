from django.shortcuts import render
# aqui solo van funciones


def home(request):
    return render(request, 'venta/index.html')


def cart(request):
    return render(request, 'venta/cart.html')


def checkout(request):
    return render(request, 'venta/checkout.html')


def contact(request):
    return render(request, 'venta/contact.html')


def login(request):
    return render(request, 'venta/login.html')


def account(request):
    return render(request, 'venta/my-account.html')


def productDet(request):
    return render(request, 'venta/product-detail.html')


def productList(request):
    return render(request, 'venta/product-list.html')


def wishlist(request):
    return render(request, 'venta/wishlist.html')
