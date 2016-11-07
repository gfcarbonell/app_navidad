# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from infos_sistemas.models import InfoSistema
from sedes.models import Sede
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import EmailValidator
from tipos_areas_funcionales.models import TipoAreaFuncional
from tipos_areas.models import TipoArea
from django.template.defaultfilters import slugify


class Area(InfoSistema):
	BOOL_ACTIVO 		 			= ((True, 'Si'), (False, 'No'))
	sede 							= models.ForeignKey(Sede)
	area_dependiente				= models.ForeignKey('self', related_name='areas_areas_dependientes_related', null=True, blank=True, default=None)
	tipo_area_funcional 			= models.ForeignKey(TipoAreaFuncional)
	tipo_area 						= models.ForeignKey(TipoArea)
	nombre 	   						= models.CharField(
												  max_length=255,
											      validators=[
											  		        MinLengthValidator(1),
											  		        MaxLengthValidator(255),
											  		    ],
												  unique=True,
												  db_index=True,
												  help_text='Escribir el nombre del área.')
	siglas							= models.CharField(
									  max_length=10,
								      validators=[
								  		        MinLengthValidator(1),
								  		        MaxLengthValidator(10),
								  		    ],
									  db_index=True,)
	email 							= models.EmailField(
														verbose_name = 'Correo electrónico (Institucional)',
														max_length=100,
														unique=True,
														db_index=True,
														validators=[
															EmailValidator(),
														])
	fax_interno						= models.CharField( verbose_name='Fax (Interno)',
													    max_length=20,
													    blank=True, null=True, help_text='(Opcional).')
	anexo_interno					= models.CharField( verbose_name='Anexo (Interno)',
													    max_length=20,
													    blank=True, null=True, help_text='(Opcional).')
	mision    	  			 		= models.TextField(verbose_name='Misión', blank=True, null=True, help_text='(Opcional)')
	vision 	  	  			 		= models.TextField(verbose_name='Visión', blank=True, null=True, help_text='(Opcional)')

	logotipo  	  					= models.ImageField(blank=True,
														null=True,
														upload_to='logotipos_areas',
														)
	fecha_creacion					= models.DateField(verbose_name='Fecha creación', blank=True, null=True)
	fecha_cese						= models.DateField(blank=True, null=True)
	descripcion		    			= models.TextField(verbose_name='Descripción', blank=True, null=True, help_text='(Opcional)')
	observacion		   				= models.TextField(verbose_name='Observación', blank=True, null=True, help_text='(Opcional)')
	activo 							= models.BooleanField(choices=BOOL_ACTIVO, default=True)


	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_siglas_nombre()

	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre
	def get_tipo_area(self):
		return self.tipo_area

	def get_siglas_nombre(self):
		return '%s - %s' %(self.get_tipo_area(), self.get_nombre())

	def get_nombre(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_nombre())
		else:
			slug = slugify(self.get_nombre())
			if self.slug != slug:
				self.slug = slug
		super(Area, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'Areas'
		#Ordenar los registros por un campo especifico
		ordering = ('tipo_area', 'nombre',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Area'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Areas'#Métodos
