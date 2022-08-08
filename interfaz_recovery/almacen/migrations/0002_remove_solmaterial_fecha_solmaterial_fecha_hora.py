# Generated by Django 4.1 on 2022-08-08 17:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solmaterial',
            name='fecha',
        ),
        migrations.AddField(
            model_name='solmaterial',
            name='fecha_hora',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
