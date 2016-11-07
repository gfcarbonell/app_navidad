# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^modulos/$', views.CatalagoModuloMenuTemplateView.as_view(), name='main'),
    url(r'^empadronamiento-municipal/$', views.EmpadronamientoMunicipalTemplateView.as_view(), name='empadronamiento_municipal'),
    url(r'^empadronamiento-municipal/menu/$', views.EmpadronamientoMunicipalMenuTemplateView.as_view(), name='empadronamiento_municipal_menu'),
]
