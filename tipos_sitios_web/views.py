from django.shortcuts import render
from rest_framework import viewsets
from .models import TipoSitioWeb
from .serializers import TipoSitioWebSerializer


class TipoSitioWebViewSet(viewsets.ModelViewSet):
    model            = TipoSitioWeb
    serializer_class = TipoSitioWebSerializer
    queryset         = TipoSitioWeb.objects.all()