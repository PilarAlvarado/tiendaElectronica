from django.urls import path
from venta.views import home, cart, category, checkout, contact, login, account, productDet, productList, ven_mod_product, ven_product, ven_del_product, viewAdmin, wishlist

urlpatterns = [
    path('', home, name='home'),
    path('cart', cart, name='cart'),
    path('category', category, name='category'),
    path('checkout', checkout, name='checkout'),
    path('contact', contact, name='contact'),
    path('login', login, name='login'),
    path('account', account, name='account'),
    path('productDet', productDet, name='productDet'),
    path('productList', productList, name='productList'),
    path('agregar-product', ven_product, name='ven_product'),
    path('modificar-product/<id>', ven_mod_product, name='ven_mod_product'),
    path('borrar-product/<id>', ven_del_product, name='ven_del_product'),
    path('viewAdmin', viewAdmin, name='viewAdmin'),
    path('wishlist', wishlist, name='wishlist')
]
