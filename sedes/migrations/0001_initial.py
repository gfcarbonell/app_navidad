# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-11-07 18:30
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ubicaciones', '0001_initial'),
        ('entidades', '0001_initial'),
        ('sitios_web', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('ubicacion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, to='ubicaciones.Ubicacion')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('nombre_host', models.CharField(max_length=255)),
                ('direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
                ('fecha_ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('ultimo_nombre_host', models.CharField(max_length=255)),
                ('ultimo_direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
                ('nombre', models.CharField(db_index=True, help_text='Escribir el nombre de la sede.', max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)])),
                ('telefono', models.CharField(blank=True, help_text='(Opcional).', max_length=20, null=True, verbose_name='Télefono')),
                ('fax', models.CharField(blank=True, help_text='(Opcional).', max_length=20, null=True)),
                ('email', models.EmailField(db_index=True, max_length=100, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='Correo electrónico (Sede)')),
                ('fecha_creacion', models.DateField(blank=True, null=True, verbose_name='Fecha creación')),
                ('fecha_cese', models.DateField(blank=True, null=True)),
                ('descripcion_sede', models.TextField(blank=True, help_text='(Opcional).', null=True, verbose_name='Descripción (Sede)')),
                ('observacion_sede', models.TextField(blank=True, help_text='(Opcional).', null=True, verbose_name='Observación (Sede)')),
                ('activo', models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=True)),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.Entidad')),
                ('sitio_web', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sitios_web.SitioWeb')),
                ('ultimo_usuario_editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sedes_sede_related', to=settings.AUTH_USER_MODEL)),
                ('usuario_creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Sedes',
                'ordering': ('nombre',),
                'verbose_name': 'Sede',
                'verbose_name_plural': 'Sedes',
            },
            bases=('ubicaciones.ubicacion', models.Model),
        ),
    ]
