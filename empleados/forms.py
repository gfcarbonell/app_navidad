# -*- encoding: utf-8 -*-
from django import forms
from .models import Empleado
from django.contrib.admin import widgets
from betterforms.multiform import MultiModelForm
from usuarios.forms import UsuarioModelForm


class EmpleadoModelForm(forms.ModelForm):
	class Meta:
		model  = Empleado
		exclude = ['tipo_persona',  'usuario',
				  'slug', 'fecha_registro', 'usuario_creador', 'nombre_host', 'direccion_ip',
				  'fecha_ultima_actualizacion', 'ultimo_usuario_editor', 'ultimo_nombre_host', 'ultimo_direccion_ip']

		widgets = {
			'tipo_persona'				   : forms.RadioSelect(attrs={'class':'radio-button-field-default'}),
			'apellido_paterno'			   : forms.TextInput(attrs={'class':'input-field-default'}),
			'apellido_materno'			   : forms.TextInput(attrs={'class':'input-field-default'}),
			'nombre'					   : forms.TextInput(attrs={'class':'input-field-default'}),
			'descripcion_empleado' 		   : forms.Textarea(attrs={'class':'input-field-area-default'}),
			'observacion_empleado' 		   : forms.Textarea(attrs={'class':'input-field-area-default'}),
			'documento_identificacion'	   : forms.Select(attrs={'class':'select-field-default'}),
			'numero_documento_identificacion'	   : forms.TextInput(attrs={'class':'select-field-default'}),
			'fecha_nacimiento'				: forms.DateInput(attrs={'class':'date-field-default'}),
			'genero'						: forms.RadioSelect(attrs={'class':'radio-button-field-default'}),
			'estado_civil'					: forms.Select(attrs={'class':'select-field-default'}),
			'grupo_sanguineo'				: forms.Select(attrs={'class':'select-field-default'}),
			'hijo'							: forms.RadioSelect(attrs={'class':'radio-button-field-default'}),
			'numero_hijo'					: forms.NumberInput(attrs={'class':'input-field-default'}),
			'celular'						: forms.NumberInput(attrs={'class':'input-field-default'}),
			'telefono'						: forms.NumberInput(attrs={'class':'input-field-default'}),
			'email'							: forms.EmailInput(attrs={'class':'input-field-default'}),
			'fotografia'    				    : forms.FileInput(attrs={'class':'input-file'}),
			'observacion_persona' 		    : forms.Textarea(attrs={'class':'input-field-area-default'}),

			'distrito' 		   				: forms.Select(attrs={'class':'select-field-default'}),
			'zona' 		   					: forms.Select(attrs={'class':'select-field-default'}),
			'via' 		   					: forms.Select(attrs={'class':'select-field-default'}),
			'observacion_zona_via'			: forms.Textarea(attrs={'class':'input-field-area-default'}),

			'nombre_zona_via'						 : forms.TextInput(attrs={'class':'input-field-default'}),
			'numero_letra_asociado_nombre_via'		 : forms.TextInput(attrs={'class':'input-field-default'}),
			'prefijo_bis_vial'						 : forms.CheckboxInput(attrs={'class':''}),
			'numero_letra_asociado_prefijo_bis_vial' : forms.TextInput(attrs={'class':'input-field-default'}),
			'cuadrante_vial'						 : forms.Select(attrs={'class':'select-field-default'}),


			'numero_via_generadora' 					 	: forms.NumberInput(attrs={'class':'input-field-default'}),
			'numero_letra_asociado_numero_via_generadora'	: forms.TextInput(attrs={'class':'input-field-default'}),
			'prefijo_bis_numero_via_generadora'				: forms.CheckboxInput(attrs={'class':''}),
			'numero_letra_asociado_prefijo_bis_numero_via_generadora'	: forms.TextInput(attrs={'class':'input-field-default'}),
			'numero_placa'									: forms.NumberInput(attrs={'class':'input-field-default'}),
			'cuadrante_via_generadora' 						: forms.Select(attrs={'class':'select-field-default'}),

			'division_area_urbana'						: forms.Select(attrs={'class':'select-field-default'}),
			'nombre_division_area_urbana'				: forms.TextInput(attrs={'class':'input-field-default'}),

			'nucleo_residencial'						: forms.Select(attrs={'class':'select-field-default'}),
			'nombre_nucleo_residencial'					: forms.NumberInput(attrs={'class':'input-field-default'}),

			'ubicacion_predio'							: forms.Select(attrs={'class':'select-field-default'}),
			'identificador_ubicacion_predio'			: forms.TextInput(attrs={'class':'input-field-default'}),

			'tipo_predio'						: forms.Select(attrs={'class':'select-field-default'}),
			'nombre_tipo_predio'				: forms.NumberInput(attrs={'class':'input-field-default'}),


			'denominacion'					: forms.TextInput(attrs={'class':'input-field-default'}),
			'referencia'					: forms.Textarea(attrs={'class':'input-field-area-default'}),

			'complemento_ubicacion_tipo_predio' 		     : forms.Select(attrs={'class':'select-field-default'}),
			'numero_letra_complemento_ubicacion_tipo_predio' : forms.TextInput(attrs={'class':'input-field-default'}),

			'area'							: forms.Select(attrs={'class':'select-field-default'}),
			'tipo_empleado'					: forms.Select(attrs={'class':'select-field-default'}),
			'cargo'							: forms.Select(attrs={'class':'select-field-default'}),
			'grado_instruccion'				: forms.Select(attrs={'class':'select-field-default'}),
			'profesion'						: forms.Select(attrs={'class':'select-field-default'}),
			'ocupacion'						: forms.Select(attrs={'class':'select-field-default'}),
			'fecha_inicio_contratacion'		: forms.DateInput(attrs={'class':'date-field-default'}),
			'fecha_fin_contratacion'		: forms.DateInput(attrs={'class':'date-field-default'}),
			'fecha_cese'					: forms.DateInput(attrs={'class':'date-field-default'}),
			'activo'						: forms.CheckboxInput(attrs={'class':''}),

	      }


class EmpleadoUsuarioForm(MultiModelForm):
	form_classes = {
        'model_form_empleado': EmpleadoModelForm,
        'model_form_usuario': UsuarioModelForm,
    }
