from rest_framework import serializers
from venta.models import ProductoP


class ProductoPSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoP
        fields = ['idProducto', 'title', 'image', 'descritption',
                  'price', 'available_colours', 'available_texture', 'categoria']
