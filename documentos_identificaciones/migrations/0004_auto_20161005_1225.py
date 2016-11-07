# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos_identificaciones', '0003_auto_20161003_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentoidentificacion',
            name='numero_digito',
            field=models.PositiveSmallIntegerField(help_text='Ingresar el número de dígitos total del documento de indetificación.', verbose_name='Número dígito(s)'),
        ),
    ]
