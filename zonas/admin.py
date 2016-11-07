# -*- encoding: utf-8 -*-
from django.contrib import admin
from infos_sistemas.admin import InfoSistemaAdmin
from .models import Zona 

@admin.register(Zona)
class ZonaAdmin(InfoSistemaAdmin):
	list_display   = ('nombre', 
					  'slug', 'fecha_registro', 'usuario_creador', 'nombre_host', 'direccion_ip',
					  'fecha_ultima_actualizacion', 'ultimo_usuario_editor', 'ultimo_nombre_host', 'ultimo_direccion_ip')
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Zona
