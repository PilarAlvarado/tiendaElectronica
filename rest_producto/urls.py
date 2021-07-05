from django.urls import path
from rest_producto.views import lista_productos, detalle_producto
from rest_producto.viewsLogin import loginT

urlpatterns = [
    path('lista-productos', lista_productos, name='lista_productos'),
    path('detalle-producto/<id>', detalle_producto, name='detalle_producto'),
    path('loginT', loginT, name='loginT'),
]
