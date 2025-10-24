from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from google.oauth2 import id_token
from google.auth.transport import requests
import os

def saludo(request):
    return HttpResponse("pagina usuarios")

# Registro de usuario
@api_view(['POST'])
def registro_usuario(request):
    data = request.data.copy()
    data['password'] = make_password(data['password'])
    serializer = UsuarioSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({"mensaje": "Usuario creado correctamente"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login de usuario normal
@api_view(['POST'])
def login_usuario(request):
    correo = request.data.get("correo")
    password = request.data.get("password")

    try:
        usuario = Usuario.objects.get(correo=correo)
    except Usuario.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

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


# 🆕 Login con Google
@api_view(['POST'])
def google_login(request):
    token = request.data.get('token')
    print("GOOGLE_CLIENT_ID en backend:", GOOGLE_CLIENT_ID)
    print("Token recibido:", token[:40] + "...")

    if not token:
        return Response(
            {"error": "Token de Google requerido"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        # Verificar el token con Google
        GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
        
        if not GOOGLE_CLIENT_ID:
            return Response(
                {"error": "Google Client ID no configurado en el servidor"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        idinfo = id_token.verify_oauth2_token(
            token, 
            requests.Request(), 
            GOOGLE_CLIENT_ID
        )
        
        # Extraer información del usuario
        email = idinfo.get('email')
        nombre = idinfo.get('name', email.split('@')[0])
        google_id = idinfo.get('sub')
        
        if not email:
            return Response(
                {"error": "No se pudo obtener el email de Google"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Buscar o crear usuario
        usuario, created = Usuario.objects.get_or_create(
            correo=email,
            defaults={
                'nombre': nombre,
                'password': make_password(google_id)  # Password basada en Google ID
            }
        )
        
        # Generar tokens JWT
        refresh = RefreshToken.for_user(usuario)
        
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "usuario": {
                "id": usuario.id,
                "nombre": usuario.nombre,
                "correo": usuario.correo
            },
            "is_new_user": created
        }, status=status.HTTP_200_OK)
        
    except ValueError as e:
        # Token inválido
        return Response(
            {"error": f"Token de Google inválido: {str(e)}"}, 
            status=status.HTTP_401_UNAUTHORIZED
        )
    except Exception as e:
        return Response(
            {"error": f"Error al procesar login con Google: {str(e)}"}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# Perfil de usuario (requiere autenticación)
@api_view(['GET'])
def perfil_usuario(request):
    usuario = request.user
    
    if not usuario or not hasattr(usuario, 'id'):
        return Response({"error": "Usuario no autenticado"}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        usuario_db = Usuario.objects.get(id=usuario.id)
        return Response({
            "usuario": {
                "id": usuario_db.id,
                "nombre": usuario_db.nombre,
                "correo": usuario_db.correo,
                "creadoen": usuario_db.creadoen
            }
        }, status=status.HTTP_200_OK)
    except Usuario.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)