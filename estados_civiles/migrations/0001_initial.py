# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 04:04
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('nombre_host', models.CharField(max_length=255)),
                ('direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
                ('fecha_ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('ultimo_nombre_host', models.CharField(max_length=255)),
                ('ultimo_direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
                ('nombre', models.CharField(db_index=True, help_text='Escribir el nombre del estado civíl.', max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)])),
                ('ultimo_usuario_editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estados_civiles_estadocivil_related', to=settings.AUTH_USER_MODEL)),
                ('usuario_creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Estados_Civiles',
                'verbose_name': 'Estado Civíl',
                'ordering': ('nombre',),
                'verbose_name_plural': 'Estados Civiles',
            },
        ),
    ]
