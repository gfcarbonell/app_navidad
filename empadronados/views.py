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
import datetime
import qrcode
from django.core.files import File
import os

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
        #img_qr = qrcode.make(str(self.object.id).zfill(10))
        img_qr = qrcode.make(self.object.id)
        nombre_img_qr_extension = str(self.object.id).zfill(10)+".png"
        f = open(nombre_img_qr_extension, "wb")
        img_qr.save(f)
        f.close()
        reopen = open(nombre_img_qr_extension, "rb")
        django_file = File(reopen)
        self.object.codigo_barra_qr.save(nombre_img_qr_extension, django_file, save=True)
        reopen.close()
        self.object.save()
        os.remove(nombre_img_qr_extension)
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
        if  self.request.GET.get('radio_report', None) and self.request.GET.get('radio_genero', None):
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            value = self.request.GET.get('radio_genero', None)
            select = self.request.GET.get('radio_report', None)
            if select == 'Todos':
                if value == 'Masculino':
                    context['total_masculino'] = self.model.objects.filter(Q(genero__icontains='Masculino')).count()
                    context['total_femenino'] = 0
                    context['total_registro'] = context['total_masculino']
                elif value == 'Femenino':
                    context['total_femenino'] = self.model.objects.filter(Q(genero__icontains='Femenino')).count()
                    context['total_masculino'] = 0
                    context['total_registro'] = context['total_femenino']
                elif value == 'General':
                    context['total_masculino'] = self.model.objects.filter(Q(genero__icontains='Masculino')).count()
                    context['total_femenino'] = self.model.objects.filter(Q(genero__icontains='Femenino')).count()
                    context['total_registro'] = self.model.objects.all().count()
            elif select == 'Fecha':
                input_fecha = self.request.GET.get('input_fecha', None)
                if value == 'Masculino':
                    context['total_masculino'] = self.model.objects.filter(Q(genero__icontains='Masculino') & Q(fecha_registro__icontains=input_fecha)).count()
                    context['total_femenino'] = 0
                    context['total_registro'] = context['total_masculino']
                elif value == 'Femenino':
                    context['total_femenino'] = self.model.objects.filter(Q(genero__icontains='Femenino') & Q(fecha_registro__icontains=input_fecha)).count()
                    context['total_masculino'] = 0
                    context['total_registro'] = context['total_femenino']
                elif value == 'General':
                    context['total_masculino'] = self.model.objects.filter(Q(genero__icontains='Masculino') & Q(fecha_registro__icontains=input_fecha)).count()
                    context['total_femenino'] = self.model.objects.filter(Q(genero__icontains='Femenino') & Q(fecha_registro__icontains=input_fecha)).count()
                    context['total_registro'] = context['total_masculino'] + context['total_femenino']
            elif select == 'Rango_Fecha':
                inicio_fecha = self.request.GET.get('inicio_fecha', None)
                fin_fecha = self.request.GET.get('fin_fecha', None)
                if value == 'Masculino':
                    context['total_masculino'] = self.model.objects.filter(Q(genero__icontains='Masculino') & Q(fecha_registro__range=[inicio_fecha, fin_fecha])).count()
                    context['total_femenino'] = 0
                    context['total_registro'] = context['total_masculino']
                elif value == 'Femenino':
                    context['total_femenino'] = self.model.objects.filter(Q(genero__icontains='Femenino') & Q(fecha_registro__range=[inicio_fecha, fin_fecha])).count()
                    context['total_masculino'] = 0
                    context['total_registro'] = context['total_femenino']
                elif value == 'General':
                    context['total_masculino'] = self.model.objects.filter(Q(genero__icontains='Masculino') & Q(fecha_registro__range=[inicio_fecha, fin_fecha])).count()
                    context['total_femenino'] = self.model.objects.filter(Q(genero__icontains='Femenino') & Q(fecha_registro__range=[inicio_fecha, fin_fecha])).count()
                    context['total_registro'] = context['total_masculino'] + context['total_femenino']

            elif self.request.GET.get('radio_report', None) == 'Rango_0_3':
                if value == 'Masculino':
                    context['total_masculino'] = self.model.objects.filter(Q(genero__icontains='Masculino') & Q(fecha_nacimiento__range=('2013-01-01', '2016-12-31'))).count()
                    context['total_femenino'] = 0
                    context['total_registro'] = context['total_masculino']
                elif value == 'Femenino':
                    context['total_femenino'] = self.model.objects.filter(Q(genero__icontains='Femenino') & Q(fecha_nacimiento__range=('2013-01-01', '2016-12-31'))).count()
                    context['total_masculino'] = 0
                    context['total_registro'] = context['total_femenino']
                elif value == 'General':
                    context['total_femenino'] = self.model.objects.filter(Q(genero__icontains='Femenino') & Q(fecha_nacimiento__range=('2013-01-01', '2016-12-31'))).count()
                    context['total_femenino'] = self.model.objects.filter(Q(genero__icontains='Femenino') & Q(fecha_nacimiento__range=('2013-01-01', '2016-12-31'))).count()
                    context['total_registro'] = context['total_masculino'] + context['total_femenino']

            elif self.request.GET.get('radio_report', None) == 'Rango_4_7':
                if value == 'Masculino':
                    context['total_masculino'] = self.model.objects.filter(Q(genero__icontains='Masculino') & Q(fecha_nacimiento__range=('2009-01-01', '2012-12-31'))).count()
                    context['total_femenino'] = 0
                    context['total_registro'] = context['total_masculino']
                elif value == 'Femenino':
                    context['total_femenino'] = self.model.objects.filter(Q(genero__icontains='Femenino') & Q(fecha_nacimiento__range=('2009-01-01', '2012-12-31'))).count()
                    context['total_masculino'] = 0
                    context['total_registro'] = context['total_femenino']
                elif value == 'General':
                    context['total_femenino'] = self.model.objects.filter(Q(genero__icontains='Femenino') & Q(fecha_nacimiento__range=('2009-01-01', '2012-12-31'))).count()
                    context['total_femenino'] = self.model.objects.filter(Q(genero__icontains='Femenino') & Q(fecha_nacimiento__range=('2009-01-01', '2012-12-31'))).count()
                    context['total_registro'] = context['total_masculino'] + context['total_femenino']
            elif self.request.GET.get('radio_report', None) == 'Rango_8_10':
                if value == 'Masculino':
                    context['total_masculino'] = self.model.objects.filter(Q(genero__icontains='Masculino') & Q(fecha_nacimiento__range=('2013-01-01', '2016-12-31'))).count()
                    context['total_femenino'] = 0
                    context['total_registro'] = context['total_masculino']
                elif value == 'Femenino':
                    context['total_femenino'] = self.model.objects.filter(Q(genero__icontains='Femenino') & Q(fecha_nacimiento__range=('2013-01-01', '2016-12-31'))).count()
                    context['total_masculino'] = 0
                    context['total_registro'] = context['total_femenino']
                elif value == 'General':
                    context['total_femenino'] = self.model.objects.filter(Q(genero__icontains='Femenino') & Q(fecha_nacimiento__range=('2013-01-01', '2016-12-31'))).count()
                    context['total_femenino'] = self.model.objects.filter(Q(genero__icontains='Femenino') & Q(fecha_nacimiento__range=('2013-01-01', '2016-12-31'))).count()
                    context['total_registro'] = context['total_masculino'] + context['total_femenino']

            return self.render_to_response(context)
        else:
            return super(EmpadronadoReportListView, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        if  self.request.GET.get('radio_report', None) and self.request.GET.get('radio_genero', None):
            value = self.request.GET.get('radio_genero', None)
            #select = self.request.GET.get('radio_report', None)
            if self.request.GET.get('radio_report', None) == 'Todos':
                if value == 'Masculino':
                    queryset = self.model.objects.filter(Q(genero__icontains='Masculino'))
                elif value == 'Femenino':
                    queryset = self.model.objects.filter(Q(genero__icontains='Femenino'))
                elif value == 'General':
                    queryset = self.model.objects.all()

            elif self.request.GET.get('radio_report', None) == 'Fecha':
                input_fecha = self.request.GET.get('input_fecha', None)
                if value == 'Masculino':
                    queryset = self.model.objects.filter(Q(genero__icontains='Masculino') & Q(fecha_registro__icontains=input_fecha))
                elif value == 'Femenino':
                    queryset = self.model.objects.filter(Q(genero__icontains='Femenino') & Q(fecha_registro__icontains=input_fecha))
                elif value == 'General':
                    queryset = self.model.objects.filter(Q(fecha_registro__icontains=input_fecha))

            elif self.request.GET.get('radio_report', None) == 'Rango_Fecha':
                inicio_fecha = self.request.GET.get('inicio_fecha', None)
                fin_fecha = self.request.GET.get('fin_fecha', None)
                if value == 'Masculino':
                    queryset = self.model.objects.filter(Q(genero__icontains='Masculino') & Q(fecha_registro__range=[inicio_fecha, fin_fecha] ))
                elif value == 'Femenino':
                    queryset = self.model.objects.filter(Q(genero__icontains='Femenino') & Q(fecha_registro__range=[inicio_fecha, fin_fecha]))
                elif value == 'General':
                    queryset = self.model.objects.filter(fecha_registro__range=[inicio_fecha, fin_fecha])

            elif self.request.GET.get('radio_report', None) == 'Rango_0_3':
                if value == 'Masculino':
                    queryset = self.model.objects.filter(Q(genero__icontains='Masculino') & Q(fecha_nacimiento__range=('2013-01-01', '2016-12-31')))
                elif value == 'Femenino':
                    queryset = self.model.objects.filter(Q(genero__icontains='Femenino') & Q(fecha_nacimiento__range=('2013-01-01', '2016-12-31')))
                elif value == 'General':
                    queryset = self.model.objects.filter(Q(fecha_registro__range=('2013-01-01', '2016-12-31')))

            elif self.request.GET.get('radio_report', None) == 'Rango_4_7':
                if value == 'Masculino':
                    queryset = self.model.objects.filter(Q(genero__icontains='Masculino') & Q(fecha_nacimiento__range=('2009-01-01', '2012-12-31')))
                elif value == 'Femenino':
                    queryset = self.model.objects.filter(Q(genero__icontains='Femenino') & Q(fecha_nacimiento__range=('2009-01-01', '2012-12-31')))
                elif value == 'General':
                    queryset = self.model.objects.filter(Q(fecha_registro__range=('2009-01-01', '2012-12-31')))

            elif self.request.GET.get('radio_report', None) == 'Rango_8_10':
                if value == 'Masculino':
                    queryset = self.model.objects.filter(Q(genero__icontains='Masculino') & Q(fecha_nacimiento__range=('2006-01-01', '2008-12-31')))
                elif value == 'Femenino':
                    queryset = self.model.objects.filter(Q(genero__icontains='Femenino') & Q(fecha_nacimiento__range=('2006-01-01', '2008-12-31')))
                elif value == 'General':
                    queryset = self.model.objects.filter(Q(fecha_registro__range=('2006-01-01', '2008-12-31')))
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


class EmpadronadoSearchQRListView(TipoPerfilUsuarioMixin, ListView):
    template_name   = 'empadronado_search_qr.html'
    model           = Empadronado

    def get_context_data(self, **kwargs):
        context = super(EmpadronadoSearchQRListView, self).get_context_data(**kwargs)
        boton_menu = True
        data = {
			'boton_menu':boton_menu,
			}
        context.update(data)
        return context

    def get(self, request, *args, **kwargs):
        if request.GET.get('codigo_barra_qr', None):
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            return self.render_to_response(context)
        else:
            return super(EmpadronadoSearchQRListView, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        if self.request.GET.get('codigo_barra_qr', None):
            value = self.request.GET.get('codigo_barra_qr', None)
            queryset = self.model.objects.filter(Q(id__contains=value))
        else:
            queryset = super(EmpadronadoSearchQRListView, self).get_queryset()
        return queryset


class EmpadronadoPrintTicketDetailView(TipoPerfilUsuarioMixin, DetailView):
    template_name   = 'empadronado_ticket.html'
    model           = Empadronado
    queryset        = Empadronado.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EmpadronadoPrintTicketDetailView, self).get_context_data(**kwargs)
        boton_menu = True
        data = {
			'boton_menu':boton_menu,
			}
        context.update(data)
        return context
