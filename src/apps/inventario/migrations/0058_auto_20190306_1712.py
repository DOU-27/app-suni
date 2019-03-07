# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-03-06 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0057_auto_20190306_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='desechoempresa',
            name='dpi',
            field=models.CharField(default='0', max_length=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='desechoempresa',
            name='encargado',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='desechoempresa',
            name='telefono',
            field=models.IntegerField(default=0, verbose_name='Número Telefónico'),
            preserve_default=False,
        ),
    ]
