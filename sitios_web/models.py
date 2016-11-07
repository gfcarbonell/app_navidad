# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from infos_sistemas.models import InfoSistema
from tipos_sitios_web.models import TipoSitioWeb
from django.template.defaultfilters import slugify


class SitioWeb(InfoSistema):
	tipo_sitio_web 					= models.ForeignKey(TipoSitioWeb)
	url 	   						= models.URLField(unique=True, db_index=True)
	descripcion    					= models.TextField(blank=True, help_text='(Opcional)')
	observacion    					= models.TextField(blank=True, help_text='(Opcional)')

	#Métodos
	#Python 3.X
	def __str__(self):
		return self.get_url()

	#Python 2.X
	#def __unicode__(self):
	#	return self.nombre
	def get_url(self):
		return self.url

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.get_url())
		else:
			slug = slugify(self.get_url())
			if self.slug != slug:
				self.slug = slug
		super(SitioWeb, self).save(*args, **kwargs)

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'Sitios_Web'
		#Ordenar los registros por un campo especifico
		ordering = ('url',)
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Sitio Web'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Sitios Web'
