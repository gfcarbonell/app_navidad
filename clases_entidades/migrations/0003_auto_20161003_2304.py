# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 04:04
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clases_entidades', '0002_auto_20160901_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claseentidad',
            name='nombre',
            field=models.CharField(db_index=True, help_text='Escribir el nombre de la clase de la entidad.', max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)]),
        ),
    ]
