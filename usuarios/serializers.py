# -*- encoding: utf-8 -*-
from django.contrib.auth.models import Group,Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from .models import Usuario
from .forms import UsuarioModelForm

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class ContentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'

class PermissionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Permission
		fields = '__all__'

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		form_class = UsuarioModelForm
		model = Usuario
		fields = ['id', 'username', 'email', 'password', 'numero_tarjeta_magnetica', 'numero_acceso_biometrico', 'avatar', 'is_active', 'is_staff', 'is_superuser']
