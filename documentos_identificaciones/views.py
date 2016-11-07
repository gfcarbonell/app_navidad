from django.shortcuts import render
from rest_framework import viewsets
from .models import DocumentoIdentificacion
from .serializers import DocumentoIdentificacionSerializer


class DocumentoIdentificacionViewSet(viewsets.ModelViewSet):
    model            = DocumentoIdentificacion
    serializer_class = DocumentoIdentificacionSerializer
    queryset         = DocumentoIdentificacion.objects.all()