# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import InfoSistema
import socket


class InfoSistemaAdmin(admin.ModelAdmin):
	exclude = ['usuario_creador', 'nombre_host', 'direccion_ip', 'ultimo_usuario_editor', 'ultimo_nombre_host', 'ultimo_direccion_ip']

	def save_model(self, request, obj, form, change):
		if change:
			obj.ultimo_usuario_editor = request.user
			try:
				obj.ultimo_nombre_host = obj.nombre_host
			except:
				obj.ultimo_nombre_host = 'localhost'

			obj.ultimo_direccion_ip = socket.gethostbyname(socket.gethostname())

		else:
			obj.usuario_creador = request.user
			obj.ultimo_usuario_editor = obj.usuario_creador
			try:
				obj.nombre_host = socket.gethostname()
				obj.ultimo_nombre_host = obj.nombre_host
			except:
				obj.nombre_host  = 'localhost'
				obj.ultimo_nombre_host = obj.nombre_host
			obj.direccion_ip = socket.gethostbyname(socket.gethostname())
			obj.ultimo_direccion_ip = obj.direccion_ip
		obj.save()
