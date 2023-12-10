# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2023-11-15 15:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventario', '0088_auto_20230807_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='CajaRepuestos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('descripcion_equipo', models.TextField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('dispositivo_bueno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dispo_malo', to='inventario.DispositivoPaquete')),
                ('dispositivo_malo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dispo_bueno', to='inventario.DispositivoPaquete')),
            ],
            options={
                'verbose_name': 'Caja de repuesto',
                'verbose_name_plural': 'Caja de repuestos',
            },
        ),
        migrations.AddField(
            model_name='salidainventario',
            name='caja_repuesto',
            field=models.ManyToManyField(blank=True, null=True, related_name='_salidainventario_caja_repuesto_+', to='inventario.SalidaInventario'),
        ),
        migrations.AddField(
            model_name='cajarepuestos',
            name='salida_asignada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salida_asig', to='inventario.SalidaInventario'),
        ),
        migrations.AddField(
            model_name='cajarepuestos',
            name='salida_caja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salida_caja', to='inventario.SalidaInventario'),
        ),
        migrations.AddField(
            model_name='cajarepuestos',
            name='tecnico_asignado',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
