# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-02 04:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('distritos', '0002_distrito_provincia'),
    ]

    operations = [
        migrations.AddField(
            model_name='distrito',
            name='ultimo_usuario_editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distritos_distrito_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='distrito',
            name='usuario_creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
