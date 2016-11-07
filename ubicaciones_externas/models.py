# -*- encoding: utf-8 -*-
from django.db import models
from nucleos_residenciales.models import NucleoResidencial
from divisiones_areas_urbanas.models import DivisionAreaUrbana
from ubicaciones_predios.models import UbicacionPredio
from tipos_predios.models import TipoPredio
from complementos_ubicaciones_predios.models import ComplementoUbicacionPredio

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from infos_sistemas.validators import valid_extension


class UbicacionExterna(models.Model):
    CHOICES_PREFIJO_BIS     = (('Bis', 'Bis'), ('No Bis', 'No Bis'))
    CHOICES_CUADRANTE       = (('Este', 'Este'), ('Norte', 'Norte'), ('Oeste', 'Oeste'), ('Sur', 'Sur') )
    numero_letra_asociado_nombre_via      = models.CharField(verbose_name='N° Letra - Nombre (Zona/Vía)' , blank=True, max_length=20, null=True)
    prefijo_bis_vial                           = models.CharField(verbose_name='Pref. Bis vial', blank=True, choices=CHOICES_PREFIJO_BIS, max_length=20, null=True)
    numero_letra_asociado_prefijo_bis_vial     = models.CharField(verbose_name='N° Letra - Pref. Bis vial', blank=True, max_length=20, null=True)
    cuadrante_vial                             = models.CharField(blank=True, null=True, default=None, choices=CHOICES_CUADRANTE, max_length=5)


    numero_via_generadora                      = models.PositiveSmallIntegerField(
																		blank=True,
																		verbose_name='N° vía generadora',
																		default = 0,
																		help_text='Escribir N° vía generadora.')
    numero_letra_asociado_numero_via_generadora  = models.CharField(verbose_name='N° Letra - N° vía generadora', blank=True, max_length=20, null=True)
    prefijo_bis_numero_via_generadora          = models.CharField(verbose_name='Pref. Bis N° vía generadora', blank=True, choices=CHOICES_PREFIJO_BIS, max_length=20, null=True)
    numero_letra_asociado_prefijo_bis_numero_via_generadora     = models.CharField(verbose_name='N° Letra - Pref. Bis N° vía generadora', blank=True, max_length=20, null=True)
    numero_placa                               = models.PositiveSmallIntegerField(
																		blank=True,
																		verbose_name='Número placa',
																		default = 0,
																		help_text='Escribir número placa.')
    cuadrante_via_generadora                   = models.CharField(blank=True, null=True, default=None, choices=CHOICES_CUADRANTE, max_length=5)


    division_area_urbana                       = models.ForeignKey(DivisionAreaUrbana, null=True, default=None, related_name='%(app_label)s_%(class)s_related',)
    nombre_division_area_urbana				   = models.CharField(
														verbose_name='Nombre división urbana',
														max_length=255,
														validators=[
															        MinLengthValidator(1),
															        MaxLengthValidator(255),
															    ],
														db_index=True,
														help_text='Escribir nombre de la división urbana')
    nucleo_residencial                         = models.ForeignKey(NucleoResidencial, null=True, default=None, related_name='%(app_label)s_%(class)s_related',)
    nombre_nucleo_residencial				   = models.CharField(
														verbose_name='Nombre núcleo residencial',
														max_length=255,
														validators=[
															        MinLengthValidator(1),
															        MaxLengthValidator(255),
															    ],
														db_index=True,
														help_text='Escribir núcleo residencial')
    ubicacion_predio                    = models.ForeignKey(UbicacionPredio, null=True, default=None, related_name='%(app_label)s_%(class)s_related',)
    identificador_ubicacion_predio      = models.CharField(blank=True, max_length=20, null=True)

    tipo_predio   = models.ForeignKey(TipoPredio, null=True, default=None, related_name='%(app_label)s_%(class)s_related',)
    nombre_tipo_predio = models.CharField(
    								verbose_name='Nombre tipo predio',
    								max_length=255,
    								validators=[
    									        MinLengthValidator(1),
    									        MaxLengthValidator(255),
    									    ],
    								db_index=True,
    								help_text='Escribir nombre del predio.')

    complemento_ubicacion_tipo_predio              = models.ForeignKey(ComplementoUbicacionPredio, null=True, default=None, related_name='%(app_label)s_%(class)s_related',)
    numero_letra_complemento_ubicacion_tipo_predio = models.CharField(blank=True, max_length=20, null=True)

    referencia                                = models.TextField(blank=True, null=True, help_text='(Opcional).')

    class Meta:
        abstract = True
