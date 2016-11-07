# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from infos_sistemas.models import InfoSistema
from sitios_web.models import SitioWeb
from ubicaciones.models import Ubicacion
from entidades.models import Entidad
from distritos.models import Distrito
from zonas.models import Zona
from vias.models import Via
from infos_sistemas.models import InfoSistema
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify
from django.core.validators import EmailValidator


class Sede(InfoSistema, Ubicacion):
	BOOL_ACTIVO 		 			= ((True, 'Si'), (False, 'No'))
	entidad 		 				= models.ForeignKey(Entidad)
	nombre 	   						= models.CharField(
												  max_length=255,
											      validators=[
											  		        MinLengthValidator(1),
											  		        MaxLengthValidator(255),
											  		    ],
												  unique=True,
												  db_index=True,
												  help_text='Escribir el nombre de la sede.')
	sitio_web 						= models.OneToOneField(SitioWeb, unique=True,)
	telefono						= models.CharField(verbose_name="Télefono",
													    max_length=20,
													    blank=True, null=True, help_text='(Opcional).')

	fax								= models.CharField(
													    max_length=20,
													    blank=True, null=True, help_text='(Opcional).')

	email 							= models.EmailField(
														verbose_name = 'Correo electrónico (Sede)',
														max_length=100,
														unique=True,
														db_index=True,
														validators=[
															EmailValidator(),
														])
	fecha_creacion					= models.DateField(verbose_name='Fecha creación', blank=True, null=True)
	fecha_cese						= models.DateField(blank=True, null=True)
	descripcion_sede	   			= models.TextField('Descripción (Sede)', blank=True, null=True, help_text='(Opcional).')
	observacion_sede   				= models.TextField('Observación (Sede)', blank=True, null=True, help_text='(Opcional).')
	activo 							= models.BooleanField(choices=BOOL_ACTIVO, default=True)

	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_nombre_full()

	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre
	def get_nombre(self):
		return self.nombre

	def get_nombre_full(self):
		return ' %s | %s ' %(self.entidad.get_nombre(), self.get_nombre())

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_nombre())
		else:
			slug = slugify(self.get_nombre())
			if self.slug != slug:
				self.slug = slug
		super(Sede, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'Sedes'
		#Ordenar los registros por un campo especifico
		ordering = ('nombre',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Sede'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Sedes'
