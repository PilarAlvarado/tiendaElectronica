from rest_framework import serializers
from venta.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'slug', 'image', 'descritption', 'price', 'created', 'updated', 'active',
                  'available_colours', 'available_sizes', 'primary_category', 'secondary_categories', 'stock']
