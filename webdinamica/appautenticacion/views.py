from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse

from .models import CustomUser
from appblogs.models import Post

import json

# Create your views here.


def registro(request):
    return render(request, 'registro.dj')


def inicio_sesion(request):
    return render(request, 'inicio_sesion.dj')


@login_required
def perfil(request):
    # perfil: https://codepen.io/ThomasDaubenton/pen/boVgjW?editors=0010

    posts = Post.objects.filter(autor_id=request.user.id).order_by('-fecha_publicacion')
    cantidad_posts = posts.count()
    contexto = {
        'posts': posts,
        'cantidad_posts': cantidad_posts,
    }

    return render(request, 'perfil.dj', contexto)


@csrf_exempt
def crear_cuenta(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        nombre_usuario = data['nombreUsuario']
        correo = data['correoElectronico']
        contrasenia = data['contrasenia']

        nuevo_usuario = CustomUser.objects.create_user(
            username=nombre_usuario, password=contrasenia, email=correo)
        nuevo_usuario.save()
        print(nuevo_usuario)

        respuesta = {
            'mensaje': nuevo_usuario.username,
            'estado': 'success',
            'redirecion': 'inicio_sesion'
        }

        return JsonResponse(respuesta)


@csrf_exempt
def crear_sesion(request):
    print(request)
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre_usuario = data['nombreUsuario']
        contrasenia = data['contrasenia']

        user = authenticate(username=nombre_usuario, password=contrasenia)

        if user:
            # User is authenticated
            login(request, user)
            # return HttpResponse('Hola Mundo')
            return JsonResponse({'redirect': 'inicio'})
        else:
            return JsonResponse({'data': 'chao mundo'})


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('inicio_sesion')


login_required


@csrf_exempt
def editar_datos_personales_perfil(request):

    if request.method == 'POST':
        try:
            datos = json.loads(request.body)
            usuario_actual = CustomUser.objects.get(id=request.user.id)
            # data_a_modificar = {}

            for clave, valor in datos.items():
                if valor != '':
                    # data_a_modificar[clave] = valor
                    setattr(usuario_actual, clave, valor)
            usuario_actual.save()

            return JsonResponse({'respuesta': 'success'})

        except Exception as e:
            print(f'Error en la ejecucion: {e}')
            return JsonResponse({'respuesta': 'error'})
