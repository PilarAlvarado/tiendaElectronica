from django.urls import path
from .views import home, cart, category, checkout, contact, login, account, productDet, productList, venModProduct, venProduct, venDelProduct, viewAdmin, wishlist

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
    path('modificarProduct', venModProduct, name="venModProduct"),
    path('agregarProduct', venProduct, name="venProduct"),
    path('borrarProduct', venDelProduct, name='venDelProduct'),
    path('viewAdmin', viewAdmin, name="viewAdmin"),
    path('wishlist', wishlist, name="wishlist")
]
