# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-11-08 14:52
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import infos_sistemas.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estados_civiles', '0001_initial'),
        ('documentos_identificaciones', '0004_auto_20161005_1225'),
        ('ubicaciones', '0002_auto_20161107_1406'),
        ('grupos_sanguineos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empadronado',
            fields=[
                ('ubicacion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, to='ubicaciones.Ubicacion')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('nombre_host', models.CharField(max_length=255)),
                ('direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
                ('fecha_ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('ultimo_nombre_host', models.CharField(max_length=255)),
                ('ultimo_direccion_ip', models.GenericIPAddressField(validators=[django.core.validators.validate_ipv46_address])),
                ('sector', models.CharField(blank=True, max_length=20, null=True)),
                ('zona_secccion', models.CharField(blank=True, max_length=20, null=True, verbose_name='Zona (Sección)')),
                ('pabellon', models.CharField(blank=True, max_length=20, null=True, verbose_name='Pabellón')),
                ('bloque', models.CharField(blank=True, max_length=20, null=True)),
                ('pasadizo', models.CharField(blank=True, max_length=20, null=True)),
                ('torre', models.CharField(blank=True, max_length=20, null=True)),
                ('edificio', models.CharField(blank=True, max_length=20, null=True)),
                ('departamento', models.CharField(blank=True, max_length=20, null=True)),
                ('apartamento', models.CharField(blank=True, max_length=20, null=True)),
                ('piso', models.CharField(blank=True, max_length=20, null=True)),
                ('interior', models.CharField(blank=True, max_length=20, null=True)),
                ('cuadra', models.CharField(blank=True, max_length=20, null=True)),
                ('manzana', models.CharField(blank=True, max_length=20, null=True)),
                ('numero', models.CharField(blank=True, max_length=20, null=True)),
                ('etapa', models.CharField(blank=True, max_length=20, null=True)),
                ('lote', models.CharField(blank=True, max_length=20, null=True)),
                ('sub_lote', models.CharField(blank=True, max_length=20, null=True)),
                ('kilometro', models.CharField(blank=True, max_length=20, null=True)),
                ('referencia', models.TextField(blank=True, null=True)),
                ('tipo_persona', models.CharField(choices=[('Natural', 'Natural'), ('Jurídica', 'Jurídica')], default='Natural', help_text='Seleccionar tipo de persona.', max_length=8)),
                ('apellido_paterno', models.CharField(db_index=True, help_text='Escribir apellido paterno.', max_length=255, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)])),
                ('apellido_materno', models.CharField(db_index=True, help_text='Escribir apellido materno.', max_length=255, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)])),
                ('nombre', models.CharField(db_index=True, help_text='Escribir nombre(s).', max_length=255, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(255)], verbose_name='Nombre(s)')),
                ('numero_documento_identificacion', models.CharField(db_index=True, help_text='Escribir número documento identificación.', max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(20)], verbose_name='Número documento identificación')),
                ('fecha_nacimiento', models.DateField()),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], default='Masculino', max_length=9, verbose_name='Género')),
                ('hijo', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False, verbose_name='¿Hijo(s)?')),
                ('numero_hijo', models.PositiveSmallIntegerField(blank=True, default=0, help_text='Escribir número(s) de hijo(s).', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Número de hijo(s)')),
                ('telefono', models.CharField(blank=True, help_text='(Opcional).', max_length=20, null=True, verbose_name='Télefono (Personal)')),
                ('celular', models.CharField(blank=True, help_text='(Opcional).', max_length=20, null=True, verbose_name='Celular (Personal)')),
                ('email', models.EmailField(db_index=True, max_length=100, unique=True, validators=[django.core.validators.EmailValidator(), django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(100)], verbose_name='Correo electrónico (Personal)')),
                ('fotografia', models.ImageField(blank=True, default='default/No_Avatar_1.png', help_text='Subir fotografia (Opcional).', null=True, upload_to='fotografias', validators=[infos_sistemas.validators.valid_extension], verbose_name='Avatar (Fotografía)')),
                ('observacion_persona', models.TextField(blank=True, help_text='Escribir observación de la persona (Opcional).', null=True, verbose_name='Observación (Persona)')),
                ('descripcion_empedronado', models.TextField(blank=True, help_text='(Opcional).', null=True, verbose_name='Descripción (Empadronado)')),
                ('observacion_empedronado', models.TextField(blank=True, help_text='(Opcional).', null=True, verbose_name='Observación (Empadronado)')),
                ('activo', models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=True)),
                ('documento_identificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empadronados_empadronado_related', to='documentos_identificaciones.DocumentoIdentificacion', verbose_name='Documento identificación')),
                ('estado_civil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empadronados_empadronado_related', to='estados_civiles.EstadoCivil')),
                ('grupo_sanguineo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empadronados_empadronado_related', to='grupos_sanguineos.GrupoSanguineo', verbose_name='Grupo sanguíneo')),
                ('ultimo_usuario_editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empadronados_empadronado_related', to=settings.AUTH_USER_MODEL)),
                ('usuario_creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('apellido_paterno',),
                'verbose_name_plural': 'Empadronados',
                'verbose_name': 'Empadronado',
                'db_table': 'Empadronados',
            },
            bases=('ubicaciones.ubicacion', models.Model),
        ),
    ]