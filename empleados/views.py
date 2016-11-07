# -*- encoding: utf-8 -*-
from django.conf import settings
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from .models import Empleado
from .forms import EmpleadoModelForm, EmpleadoUsuarioForm
from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets
from django.db.models import Q
import socket
from pure_pagination.mixins import PaginationMixin
from django.template.defaultfilters import slugify

from infos_sistemas.mixins import TipoPerfilUsuarioMixin

class EmpleadoCreateView(TipoPerfilUsuarioMixin, CreateView):
    template_name = 'empleado_create.html'
    form_class    	  = EmpleadoUsuarioForm
    model         = Empleado
    success_url   = reverse_lazy('empleado:control')

    def form_valid(self, form):
        user = form['model_form_usuario'].save(commit=False)
        user.usuario_creador      = self.request.user
        user.ultimo_usuario_editor = user.usuario_creador
        try:
            user.nombre_host = socket.gethostname()
            user.ultimo_nombre_host = user.nombre_host
        except:
           user.nombre_host  = 'localhost'
           user.ultimo_nombre_host = user.nombre_host
        user.direccion_ip    = socket.gethostbyname(socket.gethostname())
        user.ultimo_direccion_ip =  socket.gethostbyname(socket.gethostname())


        empleado = form['model_form_empleado'].save(commit=False)
        empleado.tipo_persona = 'Natural'
        if empleado.numero_hijo is None:
            empleado.numero_hijo = 0

        user.save()

        empleado.usuario = user
        empleado.usuario_creador      = self.request.user
        empleado.ultimo_usuario_editor = empleado.usuario_creador
        try:
            empleado.nombre_host = socket.gethostname()
            empleado.ultimo_nombre_host = empleado.nombre_host
        except:
           empleado.nombre_host  = 'localhost'
           empleado.ultimo_nombre_host = empleado.nombre_host
        empleado.direccion_ip    = socket.gethostbyname(socket.gethostname())
        empleado.ultimo_direccion_ip =  socket.gethostbyname(socket.gethostname())

        empleado.save()

        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdate(TipoPerfilUsuarioMixin, UpdateView):
    form_class      = EmpleadoModelForm
    success_url     = reverse_lazy('empleado:control')
    template_name   = 'empleado_update.html'
    queryset        = Empleado.objects.all()


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

        return super(EmpleadoUpdate, self).form_valid(form)

class EmpleadoUsuarioUpdateView(TipoPerfilUsuarioMixin, UpdateView):
    form_class      = EmpleadoUsuarioForm
    success_url     = reverse_lazy('empleado:control')
    template_name   = 'empleado_usuario_update.html'
    queryset        = Empleado.objects.all()

    def get_context_data(self, **kwarg):
        context  = super(EmpleadoUpdateView, self).get_context_data(**kwarg)
        empleado  = self.queryset.get(slug__contains=self.kwargs['slug'])
        data = {'empleado':empleado}
        context.update(data)
        return context

    def get_form_kwargs(self):
        kwargs = super(EmpleadoUpdateView, self).get_form_kwargs()
        kwargs.update(instance={
            'model_form_empleado': self.object,
            'model_form_usuario': self.object.usuario,
        })
        return kwargs

    def form_valid(self, form):
        empleado = self.queryset.get(slug__contains=self.kwargs['slug'])
        user = form['model_form_usuario'].save(commit=False)
        user = empleado.usuario
        user.ultimo_usuario_editor = self.request.user
        try:
            user.ultimo_nombre_host = user.nombre_host
        except:
           user.ultimo_nombre_host = user.nombre_host
        user.ultimo_direccion_ip =  socket.gethostbyname(socket.gethostname())

        empleado = form['model_form_empleado'].save(commit=False)
        empleado.tipo_persona = 'Natural'
        if empleado.numero_hijo is None:
            empleado.numero_hijo = 0
        user.save()

        empleado.usuario = user
        empleado.ultimo_usuario_editor = self.request.user
        try:
            empleado.ultimo_nombre_host = empleado.nombre_host
        except:
           empleado.ultimo_nombre_host = empleado.nombre_host
        empleado.ultimo_direccion_ip =  socket.gethostbyname(socket.gethostname())
        empleado.save()
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDetailView(TipoPerfilUsuarioMixin, DetailView):
    template_name   = 'empleado_detail.html'
    model           = Empleado
    queryset        = Empleado.objects.all()


class EmpleadoControlListView(PaginationMixin, TipoPerfilUsuarioMixin, ListView):
    model         = Empleado
    template_name = 'empleados.html'
    paginate_by   = 10

    def get_context_data(self, **kwarg):
        context     = super(EmpleadoControlListView, self).get_context_data(**kwarg)
        boton_menu     = False
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
            return super(EmpleadoControlListView, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        if self.request.GET.get('search_registro', None):
            value = self.request.GET.get('search_registro', None)
            queryset = self.model.objects.filter(Q(slug__icontains=slugify(value)))
        else:
            queryset = super(EmpleadoControlListView, self).get_queryset()
        return queryset
