# Generated by Django 2.2.12 on 2020-04-05 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200403_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuenta',
            name='moneda',
        ),
        migrations.RemoveField(
            model_name='donacion',
            name='moneda',
        ),
        migrations.RemoveField(
            model_name='itemcompra',
            name='moneda',
        ),
        migrations.AddField(
            model_name='compra',
            name='moneda',
            field=models.CharField(default='PYG', max_length=3, verbose_name='Moneda'),
        ),
    ]
