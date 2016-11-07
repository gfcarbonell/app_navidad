# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from documentos_identificaciones.models import DocumentoIdentificacion
from estados_civiles.models import EstadoCivil
from grupos_sanguineos.models import GrupoSanguineo
from distritos.models import Distrito
from vias.models import Via
from zonas.models import Zona
from infos_sistemas.models import InfoSistema
from ubicaciones.models import Ubicacion
from ubicaciones_internas.models import UbicacionInterna


from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from infos_sistemas.validators import valid_extension
from django.core.validators import EmailValidator
from django.core.validators import validate_ipv46_address
from django.template.defaultfilters import slugify


class Persona(InfoSistema, Ubicacion, UbicacionInterna):
	BOOL_HIJO 		 				= ((False, 'No'),(True, 'Si'))
	CHOICES_GENERO 	 				= (('Masculino', 'Masculino'), ('Femenino', 'Femenino'))
	CHOICES_TIPO_PERSONA 			= (('Natural', 'Natural'), ('Jurídica', 'Jurídica'))

	tipo_persona 					= models.CharField(choices=CHOICES_TIPO_PERSONA, max_length=8, default=CHOICES_TIPO_PERSONA[0][1], help_text='Seleccionar tipo de persona.')
	apellido_paterno 		 		= models.CharField(max_length=255,
													   help_text='Escribir apellido paterno.',
													   validators=[
															        MinLengthValidator(1),
															        MaxLengthValidator(255),
															    ],
													   db_index=True)
	apellido_materno 		 		= models.CharField( max_length=255,
														validators=[
															        MinLengthValidator(1),
															        MaxLengthValidator(255),
															    ],
														help_text='Escribir apellido materno.',
														db_index=True)
	nombre 			 		 		= models.CharField( verbose_name='Nombre(s)',
													    max_length=255,
														validators=[
															        MinLengthValidator(1),
															        MaxLengthValidator(255),
															    ],
													    help_text='Escribir nombre(s).',
													    db_index=True)
	documento_identificacion 		= models.ForeignKey(DocumentoIdentificacion, verbose_name='Documento identificación',  related_name='%(app_label)s_%(class)s_related')
	numero_documento_identificacion = models.CharField(verbose_name='Número documento identificación',
													   unique=True,
													   max_length=20,
													   validators=[
													   	        MinLengthValidator(1),
													   	        MaxLengthValidator(20),
													   	    ],
													   help_text='Escribir número documento identificación.',
													   db_index=True)
	fecha_nacimiento			    = models.DateField()
	genero 							= models.CharField(verbose_name='Género', choices=CHOICES_GENERO, default=CHOICES_GENERO[0][1], max_length=9)
	estado_civil 					= models.ForeignKey(EstadoCivil, related_name='%(app_label)s_%(class)s_related')
	grupo_sanguineo 				= models.ForeignKey(GrupoSanguineo, verbose_name='Grupo sanguíneo', related_name='%(app_label)s_%(class)s_related')
	hijo							= models.BooleanField(verbose_name='¿Hijo(s)?',
														  choices=BOOL_HIJO, default=False)
	numero_hijo						= models.PositiveSmallIntegerField(
																		blank=True,
																		verbose_name='Número de hijo(s)',
																		default = 0,
																		validators=[
																			        MinValueValidator(0),
																			        MaxValueValidator(10),
																			    ],
																		help_text='Escribir número(s) de hijo(s).')

	telefono 						= models.CharField(verbose_name="Télefono (Personal)",
													    max_length=20,
													    blank=True, null=True, help_text='(Opcional).')
	celular 						= models.CharField(verbose_name="Celular (Personal)",
														max_length=20, blank=True, null=True, help_text='(Opcional).')
	email 							= models.EmailField(
														verbose_name="Correo electrónico (Personal)",
														max_length=100,
														unique=True,
														db_index=True,
														validators=[
																EmailValidator(),
																MinLengthValidator(1),
																MaxLengthValidator(100),
															]
														)
	fotografia   					 = models.ImageField(
															blank=True,
															null=True,
															verbose_name='Avatar (Fotografía)',
															upload_to='fotografias',
															help_text='Subir fotografia (Opcional).',
															default='default/No_Avatar_1.png',
															validators=[valid_extension]
														)
	observacion_persona 			= models.TextField(verbose_name='Observación (Persona)',
													   blank=True, null=True,
													   help_text='Escribir observación de la persona (Opcional).')


	def __unicode__(self):
		return self.get_nombre_completo()

	def get_nombre_completo(self):
		return self.apellido_paterno + ' ' + self.apellido_materno + ', ' + self.nombre

	class Meta:
		abstract = True
