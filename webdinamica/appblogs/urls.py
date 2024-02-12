from django.urls import path
from .views import *

# app_name = AppName

urlpatterns = [
    path('post/', post, name='post'),
    path('vista_previa_post/<int:id_post>', vista_previa_post, name='vista_previa_post'),
    path('eliminar_post/<int:id_post>', eliminar_post, name='eliminar_post')
    # path('crear_post/', crear_post, name='crear_post'),
]