from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('', views.inicio_sesion, name='inicio_sesion'),
    path('crear_cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('crear_sesion/', views.crear_sesion, name='crear_sesion'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar_datos_personales_perfil/', views.editar_datos_personales_perfil, name='editar_datos_personales_perfil'),
]