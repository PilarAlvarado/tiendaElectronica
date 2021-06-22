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
        'Categoria': ListCategory
    }
    return render(request, 'venta/category.html', datos)


def checkout(request):
    return render(request, 'venta/checkout.html')


def contact(request):
    return render(request, 'venta/contact.html')


def login(request):
    return render(request, 'venta/login.html')


def account(request):
    return render(request, 'venta/my-account.html')


def productDet(request):
    return render(request, 'venta/product-det.html')


def productList(request):
    productList = Product.objects.all()
    datos = {
        'Producto': productList
    }
    return render(request, 'venta/product-list.html', datos)


def viewAdmin(request):
    return render(request, 'venta/vista-admin.html')


def wishlist(request):
    return render(request, 'venta/wishlist.html')


def venProduct(request):
    datos = {
        'vProd': ProductForm()
    }

    if(request.method == 'POST'):
        venta = ProductForm(request.POST)
        if venta.is_valid():
            venta.save()
            datos['mensaje'] = 'Guardados correctamente'
    return render(request, 'venta/ven_product.html', datos)


def venModProduct(request):
    Producto = Product.objects.get()

    datos = {
        'Producto': ProductForm(instance=Product)
    }

    if(request.method == 'POST'):
        venta = ProductForm(data=request.POST, instance=Product)
        if venta.is_valid():
            venta.save()
            datos['mensaje'] = 'Modificados correctamente'

    return render(request, 'venta/ven-mod-product.html', datos)


def venDelProduct(request, id):
    Producto = Product.objects.get()
    Product.delete()

    return redirect(to='vista-admin')
