from django.contrib import admin
from .models import (Product, ColourVariation, TextureVariation, Categoria)

admin.site.register(Product)
admin.site.register(ColourVariation)
admin.site.register(TextureVariation)
admin.site.register(Categoria)
