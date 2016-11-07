# -*- encoding: utf-8 -*-
from django.contrib import admin
from infos_sistemas.admin import InfoSistemaAdmin


class PersonaAdmin(InfoSistemaAdmin):
	list_display   = (
					'tipo_persona', 'get_nombre_completo', 'documento_identificacion',
					'numero_documento_identificacion', 'fecha_nacimiento', 'genero', 'estado_civil', 'grupo_sanguineo',
					'fotografia', 'hijo', 'numero_hijo', 'telefono', 'celular', 'email', 'observacion_persona', 
					'distrito', 'zona', 'via', 'nombre_direccion',
					'sector', 'zona_secccion', 'pabellon', 'bloque', 'pasadizo', 'torre', 'edificio',
					'departamento', 'apartamento', 'piso', 'interior', 'cuadra', 'manzana', 'numero',
					'etapa', 'lote', 'sub_lote', 'kilometro', 'denominacion', 'referencia',
					'observacion_dirección'
				 )
