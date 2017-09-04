# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-22 20:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('escuela', '0006_escuela_mapa'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EjerciciosGrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudiantes', models.PositiveIntegerField()),
                ('ejercicios', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'EjerciciosGrado',
                'verbose_name_plural': 'EjerciciosGrados',
            },
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Evaluación',
                'verbose_name_plural': 'Evaluaciones',
            },
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.IntegerField()),
                ('seccion', models.CharField(blank=True, max_length=2, null=True, verbose_name='Sección')),
                ('minimo_esperado', models.PositiveIntegerField(verbose_name='Mínimo esperado')),
            ],
            options={
                'verbose_name': 'Grado',
                'verbose_name_plural': 'Grados',
            },
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicador', models.TextField()),
            ],
            options={
                'verbose_name': 'Indicador',
                'verbose_name_plural': 'Indicadors',
            },
        ),
        migrations.CreateModel(
            name='Punteo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField(choices=[(1, '20%'), (2, '40%'), (3, '60%'), (4, '80%'), (5, '100%')], default=1)),
                ('evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kalite.Evaluacion')),
                ('indicador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kalite.Indicador')),
            ],
            options={
                'verbose_name': 'Punteo',
                'verbose_name_plural': 'Punteos',
            },
        ),
        migrations.CreateModel(
            name='Rubrica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Rúbrica',
                'verbose_name_plural': 'Rúbricas',
            },
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('capacitador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitas_kalite', to=settings.AUTH_USER_MODEL)),
                ('escuela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitas_kalite', to='escuela.Escuela')),
            ],
            options={
                'verbose_name': 'Visita de KA Lite',
                'verbose_name_plural': 'Visitas de KA Lite',
            },
        ),
        migrations.AddField(
            model_name='indicador',
            name='rubrica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indicadores', to='kalite.Rubrica'),
        ),
        migrations.AddField(
            model_name='grado',
            name='visita',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grados', to='kalite.Visita'),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='rubrica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kalite.Rubrica'),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='visita',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluaciones', to='kalite.Visita'),
        ),
        migrations.AddField(
            model_name='ejerciciosgrado',
            name='grado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ejercicios', to='kalite.Grado'),
        ),
        migrations.AlterUniqueTogether(
            name='grado',
            unique_together=set([('visita', 'grado', 'seccion')]),
        ),
        migrations.AlterUniqueTogether(
            name='evaluacion',
            unique_together=set([('visita', 'rubrica')]),
        ),
        migrations.AlterUniqueTogether(
            name='ejerciciosgrado',
            unique_together=set([('grado', 'ejercicios')]),
        ),
    ]