# Generated by Django 4.1 on 2022-08-15 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0002_alter_solmaterial_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solmaterialchoises',
            name='cantidad',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
