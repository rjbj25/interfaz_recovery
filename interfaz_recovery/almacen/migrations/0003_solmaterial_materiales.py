# Generated by Django 4.1 on 2022-08-12 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0002_remove_solmaterial_cantidad_remove_solmaterial_fecha_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='solmaterial',
            name='materiales',
            field=models.ManyToManyField(to='almacen.recurso'),
        ),
    ]
