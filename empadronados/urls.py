# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^empadronamiento-municipal/empadronado/nuevo/$', views.EmpadronadoCreateView.as_view(), name='create'),
    url(r'^empadronamiento-municipal/empadronado/(?P<slug>[-\w\W\d]+)/modificar/$', views.EmpadronadoUpdateView.as_view(), name='update'),
    url(r'^empadronamiento-municipal/empadronados/$', views.EmpadronadoControlListView.as_view(), name='control'),
    url(r'^empadronamiento-municipal/empadronados/(?P<search_registro>[-\w\W\d]+)/$', views.EmpadronadoControlListView.as_view(), name='control'),
    url(r'^empadronamiento-municipal/empadronado/(?P<slug>[-\w\W\d]+)/$', views.EmpadronadoDetailView.as_view(), name='detail'),
    url(r'^empadronamiento-municipal/reportes$', views.EmpadronadoReportListView.as_view(), name='report'),
]
