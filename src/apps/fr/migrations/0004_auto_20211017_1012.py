# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2021-10-17 16:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fr', '0003_auto_20170113_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='fr_contacto_creada_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='empresa',
            name='fr_empresa_creada_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='etiqueta',
            name='fr_etiqueta_creada_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='evento',
            name='fr_evento_creada_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tipoevento',
            name='fr_tipo_evento_creada_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]