# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2023-12-10 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyd', '0031_auto_20230713_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parrol',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='participante',
            name='dpi',
            field=models.CharField(blank=True, db_index=True, error_messages={'Unico': 'El dpi ya existe'}, max_length=15, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='asignacion',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='crasistencia',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='grupo',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='notaasistencia',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='notahito',
            unique_together=set([]),
        ),
    ]