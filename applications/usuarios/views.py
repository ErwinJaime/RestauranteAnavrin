from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password



def saludo(request):
    return HttpResponse("pagina usuarios")

# Registro de usuario
@api_view(['POST'])
def registro_usuario(request):
    data = request.data.copy()
    data['password'] = make_password(data['password'])  # encriptar password
    serializer = UsuarioSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({"mensaje": "Usuario creado correctamente"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login de usuario
@api_view(['POST'])
def login_usuario(request):
    correo = request.data.get("correo")
    password = request.data.get("password")

    try:
        usuario = Usuario.objects.get(correo=correo)
    except Usuario.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    # 🔑 CAMBIO IMPORTANTE: usar check_password en lugar de "=="
    if check_password(password, usuario.password):
        refresh = RefreshToken.for_user(usuario)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "usuario": {
                "id": usuario.id,
                "nombre": usuario.nombre,
                "correo": usuario.correo
            }
        }, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Contraseña incorrecta"}, status=status.HTTP_401_UNAUTHORIZED)