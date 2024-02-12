from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import FormularioPost
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Post
from .models import Categoria

import os
import uuid
import json

# Create your views here.


@login_required
def post(request):
    if request.method == 'POST':
        formulario = FormularioPost(request.POST, request.FILES)
        # print(formulario)

        if formulario.is_valid():
            titulo = formulario.cleaned_data['titulo']
            contenido = formulario.cleaned_data['contenido_del_post']
            imagen = None
            nombre_archivo = None

            # print(f'imagen: {formulario.cleaned_data["imagen"]}')

            if formulario.cleaned_data['imagen'] != None:
                imagen = formulario.cleaned_data['imagen']
                nombre_archivo = str(uuid.uuid4()) + \
                    os.path.splitext(imagen.name)[1]

                # guardamos la imagen en el directorio correspondiente, 'imagenes'
            # obtenemos la ruta
                ruta_carpeta_imagenes = settings.MEDIA_ROOT
                print(settings.MEDIA_ROOT)
                with open(os.path.join(ruta_carpeta_imagenes, nombre_archivo), 'wb+') as destino:
                    for chunk in imagen.chunks():
                        destino.write(chunk)

            nuevo_post = Post(titulo=titulo, contenido=contenido,
                              imagen=nombre_archivo, autor_id=request.user.id, categoria_id=1)
            nuevo_post.save()

    return render(request, 'post.dj', {'formulario':  FormularioPost})


@login_required
@csrf_exempt
def eliminar_post(request, id_post):

    if request.method == 'POST':
        data = json.loads(request.body)
        post = Post.objects.filter(id=data['id_post'])
        respuesta = None
        redireccion = None
        
        print(data)

        if request.user.id == post.get().autor.id:
            post.delete()
            respuesta = True
            redireccion = 'inicio'

        return JsonResponse({'respuesta': respuesta, 'redireccion': redireccion})
    
    
    

    post = Post.objects.filter(id=id_post)

    if post.exists():
        if request.user.id == post.get().autor.id:
            post.delete()
            return redirect('inicio')
    else:
        return redirect('inicio')


@login_required
def vista_previa_post(request, id_post):
    post = Post.objects.get(id=id_post)
    print(post)
    print(f'Autor: {post.autor}')

    return render(request, 'vista_previa_post.dj', {'post': post})
