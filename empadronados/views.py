# -*- encoding: utf-8 -*-
from django.conf import settings
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from .models import Empadronado
from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets
from django.db.models import Q
import socket
from pure_pagination.mixins import PaginationMixin
from django.template.defaultfilters import slugify


class EmpadronadoCreateView(CreateView):
    template_name = 'empadronado_create.html'
    model         = Empadronado
    success_url   = reverse_lazy('Empadronado:control')
