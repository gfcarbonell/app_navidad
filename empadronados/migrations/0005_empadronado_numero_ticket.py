# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-16 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empadronados', '0004_empadronado_codigo_barra_qr'),
    ]

    operations = [
        migrations.AddField(
            model_name='empadronado',
            name='numero_ticket',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Número Ticket'),
        ),
    ]
