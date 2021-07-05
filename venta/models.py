from django.db import models
from django.utils.translation import ugettext as _


class Category(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Categoría')

    def __str__(self):
        return str(self.nombreCategoria)


class ColourVariation(models.Model):
    ColorName = models.CharField(max_length=20, verbose_name='Color')

    def __str__(self):
        return str(self.ColorName)


class TextureVariation(models.Model):
    TextureName = models.CharField(max_length=20, verbose_name='Textura')

    def __str__(self):
        return str(self.TextureName)


class ProductoP(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id')
    title = models.CharField(max_length=150, verbose_name='title')
    image = models.ImageField(upload_to='product_images')
    descritption = models.TextField()
    price = models.IntegerField(default=0, verbose_name='price')
    available_colours = models.ManyToManyField(ColourVariation)
    available_texture = models.ManyToManyField(TextureVariation)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idProducto)

    class Meta:
        permissions = (
            ('administrador', _('Es Administrador')),
            ('usuario', _('Es Usuario'))
        )
