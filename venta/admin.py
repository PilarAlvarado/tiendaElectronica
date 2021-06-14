from django.contrib import admin
from .models import (Product, ColourVariation, SizeVariation, Category)

admin.site.register(Product)
admin.site.register(ColourVariation)
admin.site.register(SizeVariation)
admin.site.register(Category)
