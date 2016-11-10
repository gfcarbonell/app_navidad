# -*- encoding: utf-8 -*-
from django.conf import settings
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from .models import Empadronado
from .forms import EmpadronadoModelForm
from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets
from django.db.models import Q
import socket
from pure_pagination.mixins import PaginationMixin
from django.template.defaultfilters import slugify
from infos_sistemas.mixins import TipoPerfilUsuarioMixin

class EmpadronadoCreateView(TipoPerfilUsuarioMixin, CreateView):
    template_name = 'empadronado_create.html'
    model         = Empadronado
    success_url   = reverse_lazy('empadronado:control')
    form_class    = EmpadronadoModelForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.tipo_persona = 'Natural'
        if self.object.numero_hijo is None:
            self.object.numero_hijo = 0
        self.object.usuario_creador      = self.request.user
        self.object.ultimo_usuario_editor = self.object.usuario_creador
        try:
            self.object.nombre_host = socket.gethostname()
            self.object.ultimo_nombre_host = self.object.nombre_host
        except:
           self.object.nombre_host  = 'localhost'
           self.object.ultimo_nombre_host = self.object.nombre_host
        self.object.direccion_ip    = socket.gethostbyname(socket.gethostname())
        self.object.ultimo_direccion_ip =  socket.gethostbyname(socket.gethostname())
        self.object.save()

        return super(EmpadronadoCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EmpadronadoCreateView, self).get_context_data(**kwargs)
        boton_menu = True
        data = {
			'boton_menu':boton_menu,
			}
        context.update(data)
        return context





class EmpadronadoUpdateView(TipoPerfilUsuarioMixin, UpdateView):
    form_class      = EmpadronadoModelForm
    success_url     = reverse_lazy('empadronado:control')
    template_name   = 'empadronado_update.html'
    queryset        = Empadronado.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EmpadronadoUpdateView, self).get_context_data(**kwargs)
        boton_menu = True
        data = {
			'boton_menu':boton_menu,
			}
        context.update(data)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.object.numero_hijo  is None:
            self.object.numero_hijo = 0
        self.object.ultimo_usuario_editor = self.request.user
        try:
            self.object.ultimo_nombre_host = socket.gethostname()
        except:
           self.object.ultimo_nombre_host  = 'localhost'

        self.object.ultimo_direccion_ip    = socket.gethostbyname(socket.gethostname())
        self.object.save()

        return super(EmpadronadoUpdateView, self).form_valid(form)


class EmpadronadoReportListView(PaginationMixin, TipoPerfilUsuarioMixin, ListView):
    model         = Empadronado
    template_name = 'empadronado_report.html'
    paginate_by   = 25

    def get_context_data(self, **kwargs):
        context = super(EmpadronadoReportListView, self).get_context_data(**kwargs)
        boton_menu     = True
        total_registro = self.model.objects.count()
        total_masculino = self.model.objects.filter(Q(genero__icontains='Masculino')).count()
        total_femenino  = self.model.objects.filter(Q(genero__icontains='Femenino')).count()
        data = {
            'boton_menu'    : boton_menu,
            'total_registro': total_registro,
            'total_masculino' : total_masculino,
            'total_femenino' : total_femenino,
        }

        context.update(data)
        return context

    def get(self, request, *args, **kwargs):
        if self.request.GET.get('radio_genero', None):
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            value = self.request.GET.get('radio_genero', None)
            if value == 'Masculino':
                context['total_masculino'] = self.model.objects.filter(Q(genero__icontains='Masculino')).count()
                context['total_femenino'] = 0
                context['total_registro'] = context['total_masculino']
            if value == 'Femenino':
                context['total_femenino'] = self.model.objects.filter(Q(genero__icontains='Femenino')).count()
                context['total_masculino'] = 0
                context['total_registro'] = context['total_femenino']
            if value == 'General':
                context['total_masculino'] = self.model.objects.filter(Q(genero__icontains='Masculino')).count()
                context['total_femenino'] = self.model.objects.filter(Q(genero__icontains='Femenino')).count()
                context['total_registro'] = self.model.objects.all().count()
            return self.render_to_response(context)
        else:
            context['total_masculino'] = self.model.objects.filter(Q(genero__icontains='Masculino')).count()
            context['total_femenino']  = self.model.objects.filter(Q(genero__icontains='Femenino')).count()
            context['total_registro'] = self.object_list.count()
            return super(EmpadronadoReportListView, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        if  self.request.GET.get('radio_genero', None):
            value = self.request.GET.get('radio_genero', None)
            if value == 'Masculino':
                queryset = self.model.objects.filter(Q(genero__icontains='Masculino'))
            elif value == 'Femenino':
                queryset = self.model.objects.filter(Q(genero__icontains='Femenino'))
            elif value == 'General':
                queryset = self.model.objects.all()
        else:
            queryset = super(EmpadronadoReportListView, self).get_queryset()
        return queryset


class EmpadronadoControlListView(PaginationMixin, TipoPerfilUsuarioMixin, ListView):
    model         = Empadronado
    template_name = 'empadronados.html'
    paginate_by   = 10

    def get_context_data(self, **kwarg):
        context     = super(EmpadronadoControlListView, self).get_context_data(**kwarg)
        boton_menu     = True
        total_registro = self.model.objects.count()

        data = {
            'boton_menu'    : boton_menu,
            'total_registro': total_registro,
        }

        context.update(data)
        return context

    def get(self, request, *args, **kwargs):
        if request.GET.get('search_registro', None):
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            return self.render_to_response(context)
        else:
            return super(EmpadronadoControlListView, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        if self.request.GET.get('search_registro', None):
            value = self.request.GET.get('search_registro', None)
            queryset = self.model.objects.filter(Q(slug__icontains=slugify(value)))
        else:
            queryset = super(EmpadronadoControlListView, self).get_queryset()
        return queryset


class EmpadronadoDetailView(TipoPerfilUsuarioMixin, DetailView):
    template_name   = 'empadronado_detail.html'
    model           = Empadronado
    queryset        = Empadronado.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EmpadronadoDetailView, self).get_context_data(**kwargs)
        boton_menu = True
        data = {
			'boton_menu':boton_menu,
			}
        context.update(data)
        return context
