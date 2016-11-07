# -*- encoding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from .models import DocumentoIdentificacion


class DocumentoIdentificacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DocumentoIdentificacion
        fields = [
        			'id', 'nombre', 'siglas', 'numero_digito',
        		 ]
