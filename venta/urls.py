from django.urls import path
from .views import home, cart, category, checkout, contact, login, account, productDet, productList, ven_Mod_Product, ven_Product, ven_Del_Product, viewAdmin, wishlist

urlpatterns = [
    path('', home, name="home"),
    path('cart', cart, name="cart"),
    path('category', category, name="category"),
    path('checkout', checkout, name="checkout"),
    path('contact', contact, name="contact"),
    path('login', login, name="login"),
    path('account', account, name="account"),
    path('productDet', productDet, name="productDet"),
    path('productList', productList, name="productList"),
    path('modificar-Product/<id>', ven_Mod_Product, name="ven_Mod_Product"),
    path('agregar-Product', ven_Product, name="ven_Product"),
    path('borrar-Product/<id>', ven_Del_Product, name='ven_Del_Product'),
    path('viewAdmin', viewAdmin, name="viewAdmin"),
    path('wishlist', wishlist, name="wishlist")
]
