# -*- encoding: utf-8 -*-
from django.contrib.auth.models import Group,Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from .models import SitioWeb


class SitioWebSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SitioWeb
        fields = ['red_social', 'tipo_sitio_web', 'url', 'descripcion', 'observacion']
