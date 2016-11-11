from django.db import models

# Create your models here.

class UbicacionInterna(models.Model):
	sector							= models.CharField(blank=True, max_length=20, null=True)
	zona_secccion					= models.CharField(verbose_name='Zona (Sección)', blank=True, max_length=20, null=True)
	pabellon						= models.CharField(verbose_name='Pabellón', blank=True, max_length=20, null=True)
	bloque 							= models.CharField(blank=True, max_length=20, null=True)
	pasadizo 						= models.CharField(blank=True, max_length=20, null=True)
	torre							= models.CharField(blank=True, max_length=20, null=True)
	edificio						= models.CharField(blank=True, max_length=20, null=True)
	departamento					= models.CharField(blank=True, max_length=20, null=True)
	apartamento						= models.CharField(blank=True, max_length=20, null=True)
	piso 							= models.CharField(blank=True, max_length=20, null=True)
	interior						= models.CharField(blank=True, max_length=20, null=True)
	cuadra							= models.CharField(blank=True, max_length=20, null=True)
	manzana							= models.CharField(blank=True, max_length=20, null=True)
	numero 							= models.CharField(blank=True, max_length=20, null=True)
	etapa							= models.CharField(blank=True, max_length=20, null=True)
	lote							= models.CharField(blank=True, max_length=20, null=True)
	sub_lote						= models.CharField(blank=True, max_length=20, null=True)
	kilometro						= models.CharField(blank=True, max_length=20, null=True)
	
	referencia						= models.TextField(blank=True, null=True)

	class Meta:
		abstract = True
