# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2021-10-17 17:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('escuela', '0010_auto_20171117_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='escarea',
            name='esc_area_creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esccontacto',
            name='esc_contacto_creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esccontactomail',
            name='esc_contacto_telefono_creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esccontactorol',
            name='esc_rol_creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='esccontactotelefono',
            name='esc_contacto_telefono_creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='escjornada',
            name='esc_jornada_creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='escmatricula',
            name='esc_matricula_creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='escmodalidad',
            name='esc_modalidad_creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='escnivel',
            name='esc_nivel_creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='escplan',
            name='esc_plan_creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='escpoblacion',
            name='esc_poblacion_creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='escrendimientoacademico',
            name='esc_rendimiento_academico_creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='escrendimientomateria',
            name='esc_redimiento_materia_creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='escsector',
            name='esc_sector_creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='escstatus',
            name='esc_status_creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='escuela',
            name='esc_creado_por',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]