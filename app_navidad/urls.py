# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from usuarios.views import UsuarioViewSet, PermissionViewSet, GroupViewSet, ContentTypeViewSet
from documentos_identificaciones.views import DocumentoIdentificacionViewSet
router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'content_type', ContentTypeViewSet)
router.register(r'documentos_identificaciones', DocumentoIdentificacionViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',                           include('catalogos_modulos_menus_sub_menus.urls', namespace='catalogo_modulo_menu_sub_menu')),
    url(r'^', 	                        include('usuarios.urls', namespace='usuario')),
    url(r'^', 	                        include('empleados.urls', namespace='empleado')),
    url(r'^', 	                        include('empadronados.urls', namespace='empadronado')),
    #REST
    url(r'^api/', 						include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
