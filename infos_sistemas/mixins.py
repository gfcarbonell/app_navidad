from empleados.models import Empleado

class TipoPerfilUsuarioMixin(object):
    def get_context_data(self, **kwarg):
        context  = super(TipoPerfilUsuarioMixin, self).get_context_data(**kwarg)
        is_auth  = False
        instance = None
        if self.request.user.is_authenticated():
            is_auth     = True
            if Empleado.objects.filter(usuario__username=self.get_username()):
                instance = Empleado.objects.get(usuario__username=self.get_username())
                instance.tipo_perfil = "Empleado"
            else:
                instance = None
        data = {
            'is_auth'       : is_auth,
            'instance'      : instance
        }

        context.update(data)
        return context

    def get_user_id(self):
        return self.request.user.id

    def get_username(self):
        return self.request.user.username


def tipo_perfil_usuario_mixin(request):
    tipo_perfil = None
    if Empleado.objects.filter(usuario__username=request.user.username):
        instance = Empleado.objects.get(usuario__username=request.user.username)
        instance.tipo_perfil = 'Empleado'
    else:
        instance = None
    return instance
