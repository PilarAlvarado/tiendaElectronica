from rest_framework import serializers
from venta.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['idProducto', 'title', 'image', 'descritption',
                  'price', 'available_colours', 'available_texture', 'categoria']
