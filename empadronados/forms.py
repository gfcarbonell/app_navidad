# -*- encoding: utf-8 -*-
from django import forms
from .models import Empadronado


class EmpadronadoModelForm(forms.ModelForm):
	class Meta:
		model  = Empadronado
		exclude = ['tipo_persona', 'estado_civil', 'grupo_sanguineo', 'hijo', 'numero_hijo',
				  'slug', 'fecha_registro', 'usuario_creador', 'nombre_host', 'direccion_ip',
				  'fecha_ultima_actualizacion', 'ultimo_usuario_editor', 'ultimo_nombre_host', 'ultimo_direccion_ip']

		widgets = {
			'tipo_persona'				      : forms.RadioSelect(attrs={'class':'radio-button-field-default'}),
			'apellido_paterno'			      : forms.TextInput(attrs={'class':'input-field-default'}),
			'apellido_materno'			      : forms.TextInput(attrs={'class':'input-field-default'}),
			'nombre'					      : forms.TextInput(attrs={'class':'input-field-default'}),
			'descripcion_empleado' 		      : forms.Textarea(attrs={'class':'input-field-area-default'}),
			'observacion_empleado' 		      : forms.Textarea(attrs={'class':'input-field-area-default'}),
			'documento_identificacion'	      : forms.Select(attrs={'class':'select-field-default'}),
			'numero_documento_identificacion' : forms.TextInput(attrs={'class':'select-field-default'}),
			'fecha_nacimiento'				  : forms.DateInput(attrs={'class':'date-field-default'}),
			'genero'						  : forms.RadioSelect(attrs={'class':'radio-button-field-default'}),
			'estado_civil'					  : forms.Select(attrs={'class':'select-field-default'}),
			'grupo_sanguineo'				  : forms.Select(attrs={'class':'select-field-default'}),
			'hijo'							  : forms.RadioSelect(attrs={'class':'radio-button-field-default'}),
			'numero_hijo'					  : forms.NumberInput(attrs={'class':'input-field-default'}),
			'celular'						  : forms.NumberInput(attrs={'class':'input-field-default'}),
			'telefono'						  : forms.NumberInput(attrs={'class':'input-field-default'}),
			'email'							  : forms.EmailInput(attrs={'class':'input-field-default'}),
			'fotografia'    				  : forms.FileInput(attrs={'class':'input-file'}),
			'observacion_persona' 		      : forms.Textarea(attrs={'class':'input-field-area-default'}),
			'activo'						: forms.CheckboxInput(attrs={'class':''}),
			
            'distrito' 		   				: forms.Select(attrs={'class':'select-field-default'}),
			'zona' 		   					: forms.Select(attrs={'class':'select-field-default'}),
			'via' 		   					: forms.Select(attrs={'class':'select-field-default'}),
			'observacion_direccion'			: forms.Textarea(attrs={'class':'input-field-area-default'}),

			'nombre_zona_via'				: forms.TextInput(attrs={'class':'input-field-default'}),
			'sector'						: forms.TextInput(attrs={'class':'input-field-default'}),
			'zona_secccion'					: forms.TextInput(attrs={'class':'input-field-default'}),
			'pabellon'						: forms.TextInput(attrs={'class':'input-field-default'}),
			'bloque' 						: forms.TextInput(attrs={'class':'input-field-default'}),
			'pasadizo' 						: forms.TextInput(attrs={'class':'input-field-default'}),
			'torre'							: forms.TextInput(attrs={'class':'input-field-default'}),
			'edificio'						: forms.TextInput(attrs={'class':'input-field-default'}),
			'departamento'					: forms.TextInput(attrs={'class':'input-field-default'}),
			'apartamento'					: forms.TextInput(attrs={'class':'input-field-default'}),
			'piso' 							: forms.NumberInput(attrs={'class':'input-field-default'}),
			'interior'						: forms.TextInput(attrs={'class':'input-field-default'}),
			'cuadra'						: forms.NumberInput(attrs={'class':'input-field-default'}),
			'manzana'						: forms.TextInput(attrs={'class':'input-field-default'}),
			'numero'						: forms.NumberInput(attrs={'class':'input-field-default'}),
			'etapa'							: forms.TextInput(attrs={'class':'input-field-default'}),
			'lote'							: forms.TextInput(attrs={'class':'input-field-default'}),
			'sub_lote'						: forms.TextInput(attrs={'class':'input-field-default'}),
			'kilometro'						: forms.NumberInput(attrs={'class':'input-field-default'}),
			'denominacion'					: forms.TextInput(attrs={'class':'input-field-default'}),
			'referencia'					: forms.Textarea(attrs={'class':'input-field-area-default'}),

			'descripcion_empadronado'			: forms.Textarea(attrs={'class':'input-field-area-default'}),
			'observacion_empadronado'			: forms.Textarea(attrs={'class':'input-field-area-default'}),
	      }
