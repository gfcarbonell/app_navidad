# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^empadronado/nuevo/$', views.EmpadronadoCreateView.as_view(), name='create'),
    url(r'^verificar/empadronado/$', views.EmpadronadoSearchQRListView.as_view(), name='codigo_barra_qr'),
    url(r'^empadronado/(?P<slug>[-\w\W\d]+)/modificar/$', views.EmpadronadoUpdateView.as_view(), name='update'),
    url(r'^empadronados/$', views.EmpadronadoControlListView.as_view(), name='control'),
    url(r'^empadronados/(?P<search_registro>[-\w\W\d]+)/$', views.EmpadronadoControlListView.as_view(), name='control'),
    url(r'^empadronado/(?P<slug>[-\w\W\d]+)/$', views.EmpadronadoDetailView.as_view(), name='detail'),
    url(r'^empadronado/(?P<slug>[-\w\W\d]+)/imprimir$', views.EmpadronadoPrintTicketDetailView.as_view(), name='print'),
    url(r'^reportes$', views.EmpadronadoReportListView.as_view(), name='report'),


]
