from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import ProductForm


def home(request):
    return render(request, 'venta/index.html')


def cart(request):
    return render(request, 'venta/cart.html')


def category(request):
    listCategory = Category.objects.all()
    datos = {
        'Categoria': listCategory
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
    return render(request, 'venta/product-detail.html')


def productList(request):
    productList = Product.objects.all()
    datos = {
        'Producto': productList
    }
    return render(request, 'venta/product-list.html', datos)
##########################vista admi############################################


def viewAdmin(request):
    productList = Product.objects.all()
    datos = {
        'productos': productList,
    }
    return render(request, 'venta/vista-admin.html', datos)

##################guardar############################################


def ven_Product(request):
    datos = {
        'form': ProductForm()
    }

    if(request.method == 'POST'):
        venta = ProductForm(request.POST)
        if venta.is_valid():
            venta.save()
            datos['mensaje'] = 'Guardados correctamente'
    return render(request, 'venta/ven_product.html', datos)

####################modificar############################################


def ven_Mod_Product(request, Id):
    product = Product.objects.get(Idproducto=Id)
    datos = {
        'form': ProductForm(instance=product)
    }

    if(request.method == 'POST'):
        venta = ProductForm(data=request.POST, instance=product)
        if venta.is_valid():
            venta.save()
            datos['mensaje'] = 'Modificados correctamente'

    return render(request, 'venta/ven_mod_product.html', datos)

###################Eliminar#################################################


def ven_Del_Product(request, Id):
    product = Product.objects.get(Idproducto=Id)
    product.delete()

    return redirect(to='venta/vista-admin.html')


def wishlist(request):
    return render(request, 'venta/wishlist.html')
