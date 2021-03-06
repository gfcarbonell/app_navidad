# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-02 04:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('nombre_host', models.CharField(max_length=255)),
                ('direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
                ('fecha_ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('ultimo_nombre_host', models.CharField(max_length=255)),
                ('ultimo_direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
                ('nombre', models.CharField(db_index=True, help_text='Escribir nombre del distrito.', max_length=100, unique=True)),
                ('imagen', models.ImageField(blank=True, default='default/No_Image_1.png', help_text='Subir imagen del distrito. (Opcional)', upload_to='imagenes_distritos')),
                ('descripcion', models.TextField(blank=True, help_text='(Opcional)')),
            ],
            options={
                'verbose_name': 'Distrito',
                'ordering': ('nombre',),
                'verbose_name_plural': 'Distritos',
                'db_table': 'Distritos',
            },
        ),
    ]
