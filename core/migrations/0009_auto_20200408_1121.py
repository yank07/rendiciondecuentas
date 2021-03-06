# Generated by Django 2.2.12 on 2020-04-08 15:21

from django.db import migrations


def populate_monto(apps, schema_editor):
    TipoCambio = apps.get_model('utils', 'TipoCambio')
    Donacion = apps.get_model('core', 'Donacion')
    for d in Donacion.objects.all():
        if d.moneda != 'PYG':
            try:
                cambio = TipoCambio.objects.get(moneda='USD', fecha=d.fecha)
                d._monto_pyg = d.monto * cambio.cambio
            except TipoCambio.DoesNotExist:
                d_monto_pyg = d.monto * 6350.0
        else:
            d._monto_pyg = d.monto
        d.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200408_1120'),
    ]

    operations = [
        migrations.RunPython(populate_monto, reverse_code=migrations.RunPython.noop),
    ]
