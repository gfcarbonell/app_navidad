# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Area
from infos_sistemas.admin import InfoSistemaAdmin


@admin.register(Area)
class AreaAdmin(InfoSistemaAdmin):
	list_instances = True
	search_fields  = ('nombre',)

	class Meta:
		model = Area
