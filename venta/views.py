from django.shortcuts import render, redirect
from .models import ProductoP
from .forms import ProductForm


def home(request):
    return render(request, 'venta/index.html')


def cart(request):
    return render(request, 'venta/cart.html')


def category(request):
    return render(request, 'venta/category.html')


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
##########################vista admi############################################


def viewAdmin(request):
    listaProductos = ProductoP.objects.all()
    datos = {
        'product': listaProductos,
    }
    return render(request, 'venta/vista-admin.html', datos)

##################guardar############################################


def ven_product(request):
    datos = {
        'ven': ProductForm()
    }

    if(request.method == 'POST'):
        venta = ProductForm(request.POST)
        if venta.is_valid():
            venta.save()
            datos['mensaje'] = 'Guardados correctamente'
    return render(request, 'venta/ven_product.html', datos)

####################modificar############################################


def ven_mod_product(request, id):
    product = ProductoP.objects.get(Idproducto=id)
    datos = {
        'ven': ProductForm(instance=product)
    }

    if(request.method == 'POST'):
        venta = ProductForm(data=request.POST, instance=product)
        if venta.is_valid():
            venta.save()
            datos['mensaje'] = 'Modificados correctamente'

    return render(request, 'venta/ven_mod_product.html', datos)

###################Eliminar#################################################


def ven_del_product(request, id):
    product = ProductoP.objects.get(Idproducto=id)
    product.delete()

    return redirect(to='viewAdmin')


def wishlist(request):
    return render(request, 'venta/wishlist.html')
