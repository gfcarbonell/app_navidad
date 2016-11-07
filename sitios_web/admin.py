# -*- encoding: utf-8 -*-
from django.contrib import admin
from infos_sistemas.admin import InfoSistemaAdmin
from .models import SitioWeb 

@admin.register(SitioWeb)
class SitioWebAdmin(InfoSistemaAdmin):
	list_display   = ('tipo_sitio_web', 'url', 'descripcion', 'observacion',
					  'slug', 'fecha_registro', 'usuario_creador', 'nombre_host', 'direccion_ip',
					  'fecha_ultima_actualizacion', 'ultimo_usuario_editor', 'ultimo_nombre_host', 'ultimo_direccion_ip')
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = SitioWeb
