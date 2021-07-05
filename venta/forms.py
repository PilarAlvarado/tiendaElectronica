from django import forms
from django.forms import ModelForm
from .models import ProductoP


class ProductForm(ModelForm):
    class Meta:
        model = ProductoP
        fields = ['idProducto', 'title', 'image', 'descritption',
                  'price', 'available_colours', 'available_texture', 'categoria']
