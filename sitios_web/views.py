from django.shortcuts import render
from rest_framework import viewsets
from .models import SitioWeb
from .serializers import SitioWebSerializer


class SitioWebViewSet(viewsets.ModelViewSet):
    model            = SitioWeb
    serializer_class = SitioWebSerializer
    queryset         = SitioWeb.objects.all()