# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-10-04 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0023_auto_20181002_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='paquete',
            name='cantidad',
            field=models.PositiveIntegerField(default=0),
        ),
    ]