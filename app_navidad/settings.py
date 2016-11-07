# -*- encoding: utf-8 -*-
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r8&tmihwg##xrlri5kj*x@_t&!)pt@c)jm4tq1u5p!&^sjufi3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pure_pagination',
    'widget_tweaks',

    'usuarios.apps.UsuariosConfig',
    'index.apps.IndexConfig',
    #MAIN
    'modulos.apps.ModulosConfig',
    'grupos_modulos.apps.GruposModulosConfig',
    'catalogos_modulos_menus_sub_menus.apps.CatalogosModulosMenusSubMenusConfig',
    'menus.apps.MenusConfig',
    'grupos_menus.apps.GruposMenusConfig',
    'sub_menus.apps.SubMenusConfig',
    #CLASES ABSTRACTAS
    'infos_sistemas.apps.InfosSistemasConfig',
    'ubicaciones.apps.UbicacionesConfig',
    'personas.apps.PersonasConfig',
    #EMPADRONAMIENTO
    'clases_entidades.apps.ClasesEntidadesConfig',
    'tipos_entidades.apps.TiposEntidadesConfig',
    'entidades.apps.EntidadesConfig',
    'sedes.apps.SedesConfig',
    'areas.apps.AreasConfig',
    'tipos_empleados.apps.TiposEmpleadosConfig',
    'empleados.apps.EmpleadosConfig',
    'tipos_areas_funcionales.apps.TiposAreasFuncionalesConfig',
    'tipos_areas.apps.TiposAreasConfig',
    'tipos_sitios_web.apps.TiposSitiosWebConfig',
    'sitios_web.apps.SitiosWebConfig',
    'paises.apps.PaisesConfig',
    'departamentos.apps.DepartamentosConfig',
    'provincias.apps.ProvinciasConfig',
    'distritos.apps.DistritosConfig',
    'zonas.apps.ZonasConfig',
    'vias.apps.ViasConfig',
    'documentos_identificaciones.apps.DocumentosIdentificacionesConfig',
    'estados_civiles.apps.EstadosCivilesConfig',
    'grupos_sanguineos.apps.GruposSanguineosConfig',

    'cargos.apps.CargosConfig',
    'profesiones.apps.ProfesionesConfig',
    'ocupaciones.apps.OcupacionesConfig',
    'grados_instrucciones.apps.GradosInstruccionesConfig',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app_navidad.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app_navidad.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-pe'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
#MEDIA -> STATIC
STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['static'])

STATICFILES_FINDERS = {
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
}

#Activar cache para archivos estaticos
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFileStorage'

#Imagenes, audios y videos
MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])
MEDIA_URL  = '/media/'

#Configuración de Usuario
AUTH_USER_MODEL = 'usuarios.Usuario'
