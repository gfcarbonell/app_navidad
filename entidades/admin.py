# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Entidad
import socket
from infos_sistemas.admin import InfoSistemaAdmin


@admin.register(Entidad)
class EntidadAdmin(InfoSistemaAdmin):
	list_display   = (
					  'clase_entidad', 'tipo_entidad', 'nombre','siglas', 'documento_identificacion', 
					  'numero_documento_identificacion', 'mision', 'vision', 
					  'fecha_creacion', 'fecha_cese', 'descripcion', 'observacion', 'logotipo', 
					  'slug', 'fecha_registro', 'usuario_creador', 'nombre_host', 'direccion_ip',
					  'fecha_ultima_actualizacion', 'ultimo_usuario_editor', 'ultimo_nombre_host', 'ultimo_direccion_ip')
	
	list_instances = True
	search_fields  = ('nombre', 'numero_documento_identificacion')

	class Meta:
		model = Entidad