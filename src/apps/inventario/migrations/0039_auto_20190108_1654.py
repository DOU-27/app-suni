# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-01-08 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0038_auto_20181121_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='modelo',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
