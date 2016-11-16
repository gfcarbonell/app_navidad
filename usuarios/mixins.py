# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin
from braces.views import StaffuserRequiredMixin
from braces.views import SuperuserRequiredMixin
from braces.views import MultiplePermissionsRequiredMixin
from braces.views import AnonymousRequiredMixin
from braces.views import RecentLoginRequiredMixin


class AccessUserRequiredMixin(LoginRequiredMixin):
	#10 minutos
	#max_last_login_delta = 600
	#LoginRequiredMixin
	login_url	  = reverse_lazy('usuario:login')
