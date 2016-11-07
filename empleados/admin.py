# -*- encoding: utf-8 -*-
from django.contrib import admin
from infos_sistemas.admin import InfoSistemaAdmin
from .models import Empleado 


@admin.register(Empleado)
class EmpleadoAdmin(InfoSistemaAdmin):
	list_display   = ('get_nombre_completo', 'usuario', 'area', 'tipo_empleado', 'cargo', 'grado_instruccion',
					  'profesion', 'ocupacion', 'fecha_inicio_contratacion', 'fecha_fin_contratacion', 'fecha_cese',
					  'slug', 'fecha_registro', 'usuario_creador', 'nombre_host', 'direccion_ip',
					  'fecha_ultima_actualizacion', 'ultimo_usuario_editor', 'ultimo_nombre_host', 'ultimo_direccion_ip')
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Empleado
