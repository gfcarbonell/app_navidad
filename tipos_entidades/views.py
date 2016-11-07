from django.shortcuts import render
from rest_framework import viewsets
from .models import TipoEntidad
from .serializers import TipoEntidadSerializer


class TipoEntidadViewSet(viewsets.ModelViewSet):
    model            = TipoEntidad
    serializer_class = TipoEntidadSerializer
    queryset         = TipoEntidad.objects.all()