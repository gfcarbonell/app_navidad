# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from infos_sistemas.models import InfoSistema
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify


class Pais(InfoSistema):
	nombre 	   						= models.CharField(
										  max_length=100,
									      validators=[
									  		        MinLengthValidator(1),
									  		        MaxLengthValidator(100),
									  		    ],
										  unique=True, 
										  db_index=True, 
										  help_text='Escribir el nombre del país.')

	codigo_postal  					= models.PositiveIntegerField(
									  verbose_name='Código postal', 
									  unique=True,)
	imagen 		   					= models.ImageField(blank=True, 
														null=True,
														upload_to='imagenes_paises', 
														help_text='Subir imagen del país. (Opcional)')

	descripcion    					= models.TextField(verbose_name='Descripción', blank=True, null=True, help_text='(Opcional)')


	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_nombre()
	
	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre		
	def get_nombre(self):
		return self.nombre
		
	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_nombre()) 
		else:
			slug = slugify(self.get_nombre()) 
			if self.slug != slug:
				self.slug = slug
		super(Pais, self).save(*args, **kwargs)
		
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Pais'
		#Ordenar los registros por un campo especifico
		ordering = ('nombre',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Pais' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Paises'


