from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

from appautenticacion.models import CustomUser

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    # contenido = models.TextField()
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.autor.username} en {self.post.titulo}'
