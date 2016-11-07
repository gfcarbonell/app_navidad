# -*- encoding: utf-8 -*-
from django.db import models
from usuarios.models import Usuario
from django.core.validators import validate_ipv46_address


class InfoSistema(models.Model):
	slug							= models.SlugField(editable=False, max_length=255 ,unique=True, db_index=True, )
	fecha_registro 			   		= models.DateTimeField(auto_now_add=True, auto_now=False)
	usuario_creador          	 	= models.ForeignKey(Usuario)
	nombre_host				    	= models.CharField(max_length=255)
	direccion_ip			    	= models.GenericIPAddressField(validators=[validate_ipv46_address])

	fecha_ultima_actualizacion 		= models.DateTimeField(auto_now_add=False, auto_now=True)
	ultimo_usuario_editor			= models.ForeignKey(Usuario,  related_name='%(app_label)s_%(class)s_related')
	ultimo_nombre_host 				= models.CharField(max_length=255)
	ultimo_direccion_ip				= models.GenericIPAddressField(validators=[validate_ipv46_address])

	class Meta:
		abstract = True
