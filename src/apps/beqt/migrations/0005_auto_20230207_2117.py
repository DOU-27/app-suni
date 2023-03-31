# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2023-02-08 03:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0084_auto_20230110_2101'),
        ('beqt', '0004_auto_20230127_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptopbeqt',
            name='almacenamiento',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='laptopbeqt',
            name='medida_almacenamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='almacenamiento_laptop_beqt', to='inventario.DispositivoMedida'),
        ),
    ]