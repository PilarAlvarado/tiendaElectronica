from django.forms import ModelForm
from.models import Product, Category


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title, slug, image, descritption, price, created, updated, active, available_colours, available_sizes, primary_category, secondary_categories, stock']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
