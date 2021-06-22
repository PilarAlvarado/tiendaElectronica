from django.forms import ModelForm
from.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['idProducto', 'title', 'image', 'descritption',
                  'price', 'available_colours', 'available_texture', 'categoria']
