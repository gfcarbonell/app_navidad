# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import CatalogoModuloMenuSubMenu 
from infos_sistemas.admin import InfoSistemaAdmin


@admin.register(CatalogoModuloMenuSubMenu)
class CatalogoModuloMenuSubMenuAdmin(InfoSistemaAdmin):
	list_display   = ('get_nombre', 'grupo_modulo', 'modulo', 'menu', 'orden_modulo', 'orden_menu', 'imagen', 'url', 'activo', 
					  'descripcion', 'observacion', 'slug', 'fecha_registro', 'usuario_creador', 'nombre_host', 'direccion_ip',
					  'fecha_ultima_actualizacion', 'ultimo_usuario_editor', 'ultimo_nombre_host', 'ultimo_direccion_ip')
	list_instances = True
	search_fields  = ('nombre',)
	
