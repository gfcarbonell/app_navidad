# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.core.urlresolvers  import reverse_lazy


urlpatterns = [
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^usuario/(?P<slug>[-\w\W\d]+)/cambiar-contraseña/$', views.usuario_password_change, name='password_change'),
    #url(r'^control-de-asistencia/usuario/(?P<slug>[-\w\W\d]+)/cambiar-contraseña/done/$', views.usuario_password_change_done, name='password_change_done'),

    url(r'^restablecer-contraseña/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
            views.usuario_password_reset_confirm, name='password_reset_confirm'),
    url(r'^restablecer-contraseña/$', views.usuario_password_reset, name='password_reset'),
]
