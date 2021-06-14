from django.urls import path
from .views import home, cart, category, checkout, contact, login, account, productDet, productList, wishlist, form_producto, form_category

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
    path('wishlist', wishlist, name="wishlist"),
    path('Add_producto', form_producto, name="form_producto"),
    path('Add_categoria', form_category, name="form_category")
]
