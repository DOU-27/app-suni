# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-01-31 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0041_auto_20190124_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivo',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]