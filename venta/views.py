from django.shortcuts import render
from .models import Category, Product
from .forms import ProductForm, CategoryForm


def home(request):
    return render(request, 'venta/index.html')


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


def form_producto(request):
    datos = {
        'form': ProductForm()
    }

    if (request.method == 'POST'):
        formulario = ProductForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardado'
        return render(request, 'formulario/form_producto.html', datos)


def form_category(request):
    datos = {
        'form': CategoryForm()
    }

    if (request.method == 'POST'):
        formulario = CategoryForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardado'
        return render(request, 'formulario/form_category.html', datos)
