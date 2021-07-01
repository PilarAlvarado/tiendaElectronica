from django.db import models


class Category(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id')
    nombreCategoria = models.CharField(max_length=50, verbose_name='nombreC')

    def __str__(self):
        return self.nombreCategoria


class ColourVariation(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TextureVariation(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductoP(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id')
    title = models.CharField(max_length=150, verbose_name='title')
    image = models.ImageField(upload_to='venta/img')
    descritption = models.TextField()
    price = models.IntegerField(default=0, verbose_name='price')
    available_colours = models.ManyToManyField(ColourVariation)
    available_texture = models.ManyToManyField(TextureVariation)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.idProducto
