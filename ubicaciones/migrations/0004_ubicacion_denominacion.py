# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-11 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubicaciones', '0003_remove_ubicacion_denominacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='ubicacion',
            name='denominacion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Denominación'),
        ),
    ]
