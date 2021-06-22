from django.urls import path
from rest_producto.views import productList

urlpatterns = [
    path('productList', productList, name='productList'),
]
