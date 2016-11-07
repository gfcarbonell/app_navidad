# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',                           include('catalogos_modulos_menus_sub_menus.urls', namespace='catalogo_modulo_menu_sub_menu')),
    url(r'^', 	                        include('usuarios.urls', namespace='usuario')),
    url(r'^', 	                        include('empleados.urls', namespace='empleado'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
