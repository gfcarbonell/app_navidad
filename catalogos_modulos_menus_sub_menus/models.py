# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from menus.models import Menu
from sub_menus.models import SubMenu
from modulos.models import Modulo
from grupos_modulos.models import GrupoModulo
from infos_sistemas.models import InfoSistema
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify


class CatalogoModuloMenuSubMenu(InfoSistema):
	BOOL_ACTIVO 		 			= ((True, 'Si'), (False, 'No'))
	grupo_modulo 					= models.ForeignKey(GrupoModulo)
	modulo 							= models.ForeignKey(Modulo)
	menu 							= models.ForeignKey(Menu)
	sub_menu 						= models.ForeignKey(SubMenu)
	orden_modulo 					= models.SmallIntegerField(
												default = 0,
											)
	orden_menu 						= models.SmallIntegerField(
												default = 0,
												)
	orden_sub_menu 					= models.SmallIntegerField(
												default = 0,
											)
	imagen 	  						= models.ImageField(blank=True,
						   							null=True,
						   							help_text='Subir imagen. (Opcional)'
						 							)
	url 							= models.URLField(unique=True, db_index=True)
	descripcion		    			= models.TextField(verbose_name='Observación', blank=True, null=True, help_text='(Opcional)')
	observacion		   				= models.TextField(verbose_name='Descripción', blank=True, null=True, help_text='(Opcional)')
	activo 							= models.BooleanField(default=True, choices=BOOL_ACTIVO)

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
		super(CatalogoModuloMenuSubMenu, self).save(*args, **kwargs)

	def get_nombre(self):
		return ' %s | %s | %s' %(self.modulo.get_nombre() , self.menu.get_nombre(), self.sub_menu.get_nombre())

	#Opciones
	class Meta:
		#Nombre para la tabla del gestor de base de datos
		db_table = 'Catalogos_Modulos_Menus_Sub_Menus'
		#Ordenar los registros por un campo especifico
		ordering = ('orden_modulo','orden_menu', 'orden_sub_menu')
		#Nombre para el Conjunto de Objetos en el Panel de Administración
		verbose_name = 'Catalogo Módulo Menu Sub Menu'
		#Nombre en Plural en la lista de módulos en el Panel de Administración
		verbose_name_plural = 'Catalogos Módulos Menus Sub Menus'
