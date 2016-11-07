# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from documentos_identificaciones.models import DocumentoIdentificacion
from clases_entidades.models import ClaseEntidad
from tipos_entidades.models import TipoEntidad
from infos_sistemas.models import InfoSistema
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify



class Entidad(InfoSistema):
	BOOL_ACTIVO 		 			= ((True, 'Si'), (False, 'No'))
	clase_entidad 					= models.ForeignKey(ClaseEntidad)
	tipo_entidad 					= models.ForeignKey(TipoEntidad)
	nombre 	   						= models.CharField(
									  max_length=255,
								      validators=[
								  		        MinLengthValidator(1),
								  		        MaxLengthValidator(255),
								  		    ],
									  unique=True, 
									  db_index=True, 
									  help_text='Escribir el nombre de la entidad.')
	slogan 					 		= models.CharField(blank=True, null=True, max_length=255, db_index=True, help_text='Escribir el slogan de la entidad.')
	siglas							= models.CharField(
									  max_length=10, 
								      validators=[
								  		        MinLengthValidator(1),
								  		        MaxLengthValidator(10),
								  		    ],
									  db_index=True,)
	documento_identificacion 		= models.ForeignKey(DocumentoIdentificacion, verbose_name='Documento identificación')
	numero_documento_identificacion = models.CharField(
									  verbose_name='Número documento identificación', 
									  unique=True, 
									  max_length=20, 
								      validators=[
								  		        MinLengthValidator(1),
								  		        MaxLengthValidator(20),
								  		    ],
									  db_index=True)
	mision    	  			 		= models.TextField(verbose_name='Misión', blank=True, null=True, help_text='(Opcional)') 
	vision 	  	  			 		= models.TextField(verbose_name='Visión', blank=True, null=True, help_text='(Opcional)') 
	logotipo  	  					= models.ImageField(blank=True, 
														null=True, 
														upload_to='logotipos_entidades',
														)
	fecha_creacion					= models.DateField(verbose_name='Fecha creación', blank=True, null=True)	
	fecha_cese						= models.DateField(blank=True, null=True)
	descripcion		    			= models.TextField(verbose_name='Descripción', blank=True, null=True, help_text='(Opcional)')
	observacion		   				= models.TextField(verbose_name='Observación', blank=True, null=True, help_text='(Opcional)') 
	activo 							= models.BooleanField(choices=BOOL_ACTIVO, default=True)
		
	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_nombre()
	
	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre		

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_nombre()) 
		else:
			slug = slugify(self.get_nombre()) 
			if self.slug != slug:
				self.slug = slug
		super(Entidad, self).save(*args, **kwargs)

	def get_nombre(self):
		return self.nombre
		
	def get_siglas(self):
		return self.siglas	
		
	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos 
		db_table = 'Entidades'
		#Ordenar los registros por un campo especifico
		ordering = ('nombre',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Entidad' 
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Entidades'#Métodos
