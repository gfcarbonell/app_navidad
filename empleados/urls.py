# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^empleado/nuevo/$', views.EmpleadoCreateView.as_view(), name='create'),
    #url(r'^empleado/(?P<slug>[-\w\W\d]+)/modificar/$', views.EmpleadoUpdateView.as_view(), name='update'),
    url(r'^empleado/(?P<slug>[-\w\W\d]+)/modificar/$', views.EmpleadoUpdate.as_view(), name='update'),
    url(r'^empleado/(?P<slug>[-\w\W\d]+)/$', views.EmpleadoDetailView.as_view(), name='detail'),
    url(r'^empleados/$', views.EmpleadoControlListView.as_view(), name='control'),
    url(r'^empleados/(?P<search_registro>[-\w\W\d]+)/$', views.EmpleadoControlListView.as_view(), name='control'),
]
