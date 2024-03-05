# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2023-11-18 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalite', '0005_auto_20211017_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='visita',
            name='alumnas',
            field=models.PositiveIntegerField(default=0, verbose_name='Alumnas capacitadas'),
        ),
        migrations.AddField(
            model_name='visita',
            name='alumnos',
            field=models.PositiveIntegerField(default=0, verbose_name='Alumnos capacitados'),
        ),
        migrations.AddField(
            model_name='visita',
            name='maestras',
            field=models.PositiveIntegerField(default=0, verbose_name='Maestras capacitadas'),
        ),
        migrations.AddField(
            model_name='visita',
            name='maestros',
            field=models.PositiveIntegerField(default=0, verbose_name='Maestros capacitados'),
        ),
    ]