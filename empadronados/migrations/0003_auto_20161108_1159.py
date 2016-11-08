# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-11-08 16:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empadronados', '0002_auto_20161108_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empadronado',
            name='email',
            field=models.EmailField(blank=True, db_index=True, max_length=100, null=True, validators=[django.core.validators.EmailValidator(), django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)], verbose_name='Correo electrónico (Personal)'),
        ),
    ]
