from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # datos personales
    biografia = models.CharField(max_length = 150, null=True)
    edad = models.IntegerField(null=True)
    nombre_completo = models.CharField(max_length = 150, default='')
    estado_estudiante = models.CharField(max_length = 150, default='')
    sexo = models.CharField(max_length = 2, default='')
    orientacion_sexual = models.CharField(max_length = 150, default='')
    
    
    
    

    # imagenes
    # imagen_perfil = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    # imagen_portada = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    
    # habilidades

    # redes sociales
    link_instagram = models.CharField(max_length=150, null=True)
    link_facebook = models.CharField(max_length = 150, null=True)
    link_twitter = models.CharField(max_length = 150, null=True)
    link_tik_tok = models.CharField(max_length = 150, null=True)
    link_youtube = models.CharField(max_length = 150, null=True)
    link_linkedin = models.CharField(max_length = 150, null=True)
    
    
    # datos instituto
    semestre_cursado = models.IntegerField(default=0, null=True)
    carrera = models.CharField(max_length = 150, default='')
    institucion = models.CharField(max_length = 150, default='')
    correo_institucional = models.EmailField(default='correo.institucional@alumnos.santotomas.cl')
    asignatura_favorita = models.CharField(max_length = 150, default='')
    
    
    
    
    
    # sistema de niveles
    nivel = models.IntegerField(default=0, null=True) # nivel maximo 100
    experiencia_obtenida = models.IntegerField(default=0, null=True)
    
    
    

    