from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('idCategoria', models.IntegerField(
                    primary_key=True, serialize=False, verbose_name='Id')),
                ('nombreCategoria', models.CharField(
                    max_length=50, verbose_name='Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='ColourVariation',
            fields=[
                ('ColorName', models.CharField(max_length=50, verbose_name='Color')),
            ],
        ),
        migrations.CreateModel(
            name='TextureVariation',
            fields=[
                ('TextureName', models.CharField(
                    max_length=50, verbose_name='Textura')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoP',
            fields=[
                ('idProducto', models.IntegerField(
                    primary_key=True, serialize=False, verbose_name='Id')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('image', models.ImageField(upload_to='venta/img')),
                ('descritption', models.TextField()),
                ('price', models.IntegerField(default=0, verbose_name='price')),
                ('categoria', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='venta.categoriap')),
            ],
        ),
    ]
