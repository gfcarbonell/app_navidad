# -*- encoding: utf-8 -*-
from django.conf import settings
from django.http import Http404, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from pure_pagination.mixins import PaginationMixin
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.views.generic import View
from django.views.generic import RedirectView


from braces.views import LoginRequiredMixin, RecentLoginRequiredMixin

from .models import Usuario
from .serializers import UsuarioSerializer, PermissionSerializer, GroupSerializer, ContentTypeSerializer
from .forms import UsuarioModelForm, UsuarioAuthenticationForm

from django.core.urlresolvers import reverse_lazy
from rest_framework import viewsets
from django.db.models import Q
import socket
from django.contrib.auth.views import password_reset, password_reset_confirm, password_reset_done, password_change, password_change_done
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from infos_sistemas.mixins import tipo_perfil_usuario_mixin


def usuario_password_change(request, slug):
    instance = tipo_perfil_usuario_mixin(request)
    return password_change(request,
                        template_name='password_change.html',
                        post_change_redirect=reverse_lazy("empleado:detail", kwargs = {'slug' : instance.slug, }),
                        password_change_form=PasswordChangeForm,
                        extra_context={'username':request.user.username,
                                       'instance':instance}
                    )


def usuario_password_change_done(request, slug):
    instance = tipo_perfil_usuario_mixin(request)
    return password_change_done(request,
                        template_name='password_change_done.html',
                        extra_context={'username':request.user.username,
                                       'instance':instance}
                    )

def usuario_password_reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='password_reset_confirm.html',
        uidb64=uidb64, token=token, post_reset_redirect=reverse_lazy('usuario:login'))


def usuario_password_reset(request):
    return password_reset(request, template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt',
        post_reset_redirect=reverse_lazy('usuario:login'))


class LoginView(FormView):
    form_class    =  UsuarioAuthenticationForm
    template_name = 'login.html'
    success_url   =  reverse_lazy('catalogo_modulo_menu_sub_menu:main')

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid(form)

    @method_decorator(sensitive_post_parameters('password'))
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)


class LogoutView(RedirectView):
    url = reverse_lazy('usuario:login')
    def get(self, request, *args, **kwargs):
        auth_logout(self.request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class UsuarioCreateView(CreateView):
    template_name = 'usuario_create.html'
    form_class    = UsuarioModelForm
    success_url   = reverse_lazy('usuario:control')

    def form_valid(self, form):
        self.object = form.save(commit=False)
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

        return super(UsuarioCreateView, self).form_valid(form)

    def get_context_data(self, **kwarg):
        context     = super(UsuarioCreateView, self).get_context_data(**kwarg)
        is_auth  = False
        username = None
        id_usuario = None
        avatar = None
        if self.request.user.is_authenticated():
            id_usuario  = self.get_user_id()
            is_auth     = True
            username    = self.get_username()
            avatar      = self.get_avatar()
        data = {
            'id_usuario' : id_usuario,
            'is_auth'    : is_auth,
            'username'   : username,
            'avatar'     : avatar
        }
        context.update(data)
        return context

    def get_user_id(self):
        return self.request.user.id

    def get_username(self):
        return self.request.user.username

    def get_avatar(self):
        return self.request.user.avatar


class UsuarioUpdateView(UpdateView):
    form_class      = UsuarioModelForm
    success_url     = reverse_lazy('usuario:control')
    template_name   = 'usuario_update.html'
    queryset        = Usuario.objects.all()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.ultimo_usuario_editor = self.request.user
        try:
            self.object.ultimo_nombre_host = socket.gethostname()
        except:
           self.object.ultimo_nombre_host  = 'localhost'

        self.object.ultimo_direccion_ip    = socket.gethostbyname(socket.gethostname())
        self.object.save()

        return super(UsuarioUpdateView, self).form_valid(form)

    def get_context_data(self, **kwarg):
        context     = super(UsuarioUpdateView, self).get_context_data(**kwarg)
        is_auth  = False
        username = None
        password = None

        if self.request.user.is_authenticated():
            id_usuario  = self.get_user_id()
            is_auth     = True
            username    = self.get_username()
            password    = self.get_password()

        data = {
            'id_usuario' : id_usuario,
            'is_auth'    : is_auth,
            'username'   : username,
            'password'   : password,
        }

        context.update(data)
        return context

    def get_user_id(self):
        return self.request.user.id

    def get_password(self):
        return self.request.user.password

    def get_username(self):
        return self.request.user.username


class UsuarioControlListView(PaginationMixin, ListView):
    model         = Usuario
    template_name = 'usuarios.html'
    paginate_by   = 10

    def get_context_data(self, **kwarg):
        context     = super(UsuarioControlListView, self).get_context_data(**kwarg)
        is_auth  = False
        username = None
        id_usuario = None
        boton_menu     = False
        total_registro = self.model.objects.count()
        avatar = None

        if self.request.user.is_authenticated():
            id_usuario  = self.get_user_id()
            is_auth     = True
            username    = self.get_username()
            avatar      = self.get_avatar()
        data = {
            'id_usuario'    : id_usuario,
            'is_auth'       : is_auth,
            'username'      : username,
            'boton_menu'    : boton_menu,
            'total_registro': total_registro,
            'avatar'        : avatar,
        }

        context.update(data)
        return context

    def get_user_id(self):
        return self.request.user.id

    def get_username(self):
        return self.request.user.username

    def get_avatar(self):
        return self.request.user.avatar

    def get_template_names(self):
        if self.request.GET.get('search_registro', None) != None:
            return "empleado_table.html"
        else:
            return self.template_name

    def get(self, request, *args, **kwargs):
        if request.GET.get('search_registro', None):
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            return self.render_to_response(context)
        else:
            return super(UsuarioControlListView, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        if self.kwargs.get('variable'):
            queryset = self.model.objects.filter(slug__icontains=self.kwargs['variable'])

        elif self.request.GET.get('search_registro', ''):
            queryset = self.model.objects.filter(
                        Q(slug__icontains=self.request.GET.get('search_registro', ''))
                        |Q(email__icontains=self.request.GET.get('search_registro', ''))
                        |Q(pk__icontains=self.request.GET.get('search_registro', ''))
                    )
        else:
            queryset = super(UsuarioControlListView, self).get_queryset()
        return queryset


class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'usuario_detail.html'

    def get_context_data(self, **kwarg):
        context     = super(UsuarioDetailView, self).get_context_data(**kwarg)
        is_auth  = False
        username = None
        avatar   = None
        if self.request.user.is_authenticated():
            id_usuario  = self.get_user_id()
            is_auth     = True
            username    = self.get_username()
            avatar      = self.get_avatar()

        data = {
            'id_usuario' : id_usuario,
            'is_auth'    : is_auth,
            'username'   : username,
            'avatar'     : avatar
        }

        context.update(data)
        return context

    def get_user_id(self):
        return self.request.user.id

    def get_avatar(self):
        return self.request.user.avatar

    def get_username(self):
        return self.request.user.username


class UsuarioViewSet(viewsets.ModelViewSet):
    model            = Usuario
    serializer_class = UsuarioSerializer
    queryset         = Usuario.objects.all()
    queryset_detail  = queryset.prefetch_related('groups__permissions')

class PermissionViewSet(viewsets.ModelViewSet):
    model            = Permission
    serializer_class = PermissionSerializer
    queryset         = Permission.objects.all()

class GroupViewSet(viewsets.ModelViewSet):
    model            = Group
    serializer_class = GroupSerializer
    queryset         = Group.objects.all()


class ContentTypeViewSet(viewsets.ModelViewSet):
    model            = ContentType
    serializer_class = ContentTypeSerializer
    queryset         = ContentType.objects.all()
