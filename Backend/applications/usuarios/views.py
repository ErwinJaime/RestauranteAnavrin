# usuarios/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken
from google.oauth2 import id_token
from google.auth.transport import requests
import os

from .models import Usuario, Producto, Pedido, Resena
from .serializers import (
    # Usuario
    UsuarioSerializer, UsuarioRegistroSerializer, UsuarioPerfilSerializer,
    # Producto
    ProductoSerializer, ProductoListSerializer,
    # Pedido
    PedidoSerializer, PedidoCreateSerializer, PedidoListSerializer, PedidoEstadoSerializer,
    # Reseña
    ResenaSerializer, ResenaCreateSerializer, ResenaListSerializer, ResenaVisibilidadSerializer
)

def saludo(request):
    return HttpResponse("API Anavrin - Sistema de Pedidos")

# ========== AUTENTICACIÓN ==========

@api_view(['POST'])
def registro_usuario(request):
    """Registro de usuario normal"""
    serializer = UsuarioRegistroSerializer(data=request.data)
    
    if serializer.is_valid():
        usuario = serializer.save()
        refresh = RefreshToken.for_user(usuario)
        
        return Response({
            "mensaje": "Usuario creado correctamente",
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "usuario": {
                "id": usuario.id,
                "nombre": usuario.nombre,
                "correo": usuario.correo
            }
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_usuario(request):
    """Login de usuario normal"""
    correo = request.data.get("correo")
    password = request.data.get("password")

    if not correo or not password:
        return Response({
            "error": "Correo y contraseña son requeridos"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        usuario = Usuario.objects.get(correo=correo)
    except Usuario.DoesNotExist:
        return Response({
            "error": "Credenciales incorrectas"
        }, status=status.HTTP_401_UNAUTHORIZED)

    if check_password(password, usuario.password):
        refresh = RefreshToken.for_user(usuario)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "usuario": {
                "id": usuario.id,
                "nombre": usuario.nombre,
                "correo": usuario.correo,
                "es_admin": usuario.es_admin
            }
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            "error": "Credenciales incorrectas"
        }, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def google_login(request):
    """Login con Google OAuth"""
    token = request.data.get('token')
    
    if not token:
        return Response(
            {"error": "Token de Google requerido"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
        
        if not GOOGLE_CLIENT_ID:
            return Response(
                {"error": "Google Client ID no configurado en el servidor"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        # Verificar el token con Google
        idinfo = id_token.verify_oauth2_token(
            token, 
            requests.Request(), 
            GOOGLE_CLIENT_ID
        )
        
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
                'password': make_password(google_id)
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
                "correo": usuario.correo,
                "es_admin": usuario.es_admin
            },
            "is_new_user": created
        }, status=status.HTTP_200_OK)
        
    except ValueError as e:
        return Response(
            {"error": f"Token de Google inválido: {str(e)}"}, 
            status=status.HTTP_401_UNAUTHORIZED
        )
    except Exception as e:
        return Response(
            {"error": f"Error al procesar login con Google: {str(e)}"}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def perfil_usuario(request):
    """Obtener perfil del usuario autenticado"""
    serializer = UsuarioPerfilSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def actualizar_perfil(request):
    """Actualizar perfil del usuario autenticado"""
    serializer = UsuarioSerializer(
        request.user, 
        data=request.data, 
        partial=True,
        context={'request': request}
    )
    
    if serializer.is_valid():
        serializer.save()
        return Response({
            "mensaje": "Perfil actualizado correctamente",
            "usuario": serializer.data
        }, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ========== PRODUCTOS ==========

@api_view(['GET'])
def listar_productos(request):
    """Listar todos los productos (públicos)"""
    categoria = request.query_params.get('categoria')
    disponible = request.query_params.get('disponible')
    
    productos = Producto.objects.all()
    
    if categoria:
        productos = productos.filter(categoria=categoria)
    if disponible is not None:
        productos = productos.filter(disponible=disponible.lower() == 'true')
    
    serializer = ProductoListSerializer(
        productos, 
        many=True, 
        context={'request': request}
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def detalle_producto(request, pk):
    """Detalle de un producto específico"""
    producto = get_object_or_404(Producto, pk=pk)
    serializer = ProductoSerializer(producto, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def crear_producto(request):
    """Crear nuevo producto (solo admin)"""
    serializer = ProductoSerializer(data=request.data, context={'request': request})
    
    if serializer.is_valid():
        serializer.save()
        return Response({
            "mensaje": "Producto creado correctamente",
            "producto": serializer.data
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAdminUser])
def actualizar_producto(request, pk):
    """Actualizar producto existente (solo admin)"""
    producto = get_object_or_404(Producto, pk=pk)
    serializer = ProductoSerializer(
        producto, 
        data=request.data, 
        partial=True,
        context={'request': request}
    )
    
    if serializer.is_valid():
        serializer.save()
        return Response({
            "mensaje": "Producto actualizado correctamente",
            "producto": serializer.data
        }, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def eliminar_producto(request, pk):
    """Eliminar producto (solo admin)"""
    producto = get_object_or_404(Producto, pk=pk)
    nombre = producto.nombre
    producto.delete()
    
    return Response({
        "mensaje": f"Producto '{nombre}' eliminado correctamente"
    }, status=status.HTTP_200_OK)


# ========== PEDIDOS ==========

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_pedidos_usuario(request):
    """Listar pedidos del usuario autenticado"""
    estado = request.query_params.get('estado')
    
    pedidos = Pedido.objects.filter(usuario=request.user)
    
    if estado:
        pedidos = pedidos.filter(estado=estado)
    
    serializer = PedidoSerializer(
        pedidos, 
        many=True, 
        context={'request': request}
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def listar_todos_pedidos(request):
    """Listar todos los pedidos (solo admin)"""
    estado = request.query_params.get('estado')
    usuario_id = request.query_params.get('usuario_id')
    
    pedidos = Pedido.objects.all()
    
    if estado:
        pedidos = pedidos.filter(estado=estado)
    if usuario_id:
        pedidos = pedidos.filter(usuario_id=usuario_id)
    
    serializer = PedidoSerializer(
        pedidos, 
        many=True, 
        context={'request': request}
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detalle_pedido(request, pk):
    """Detalle de un pedido específico"""
    pedido = get_object_or_404(Pedido, pk=pk)
    
    # Verificar que el usuario sea el dueño o admin
    if pedido.usuario != request.user and not request.user.es_admin:
        return Response({
            "error": "No tienes permiso para ver este pedido"
        }, status=status.HTTP_403_FORBIDDEN)
    
    serializer = PedidoSerializer(pedido, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_pedido(request):
    """Crear nuevo pedido"""
    serializer = PedidoCreateSerializer(data=request.data)
    
    if serializer.is_valid():
        # Verificar si ya existe un pedido con ese producto
        producto = serializer.validated_data['producto']
        pedido_existente = Pedido.objects.filter(
            usuario=request.user,
            producto=producto
        ).first()
        
        if pedido_existente:
            return Response({
                "error": "Ya tienes un pedido de este producto. Puedes actualizarlo en lugar de crear uno nuevo."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        pedido = serializer.save(usuario=request.user)
        response_serializer = PedidoSerializer(pedido, context={'request': request})
        
        return Response({
            "mensaje": "Pedido creado correctamente",
            "pedido": response_serializer.data
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def actualizar_pedido(request, pk):
    """Actualizar pedido existente (solo cantidad y dirección)"""
    pedido = get_object_or_404(Pedido, pk=pk)
    
    # Verificar que el usuario sea el dueño
    if pedido.usuario != request.user:
        return Response({
            "error": "No tienes permiso para modificar este pedido"
        }, status=status.HTTP_403_FORBIDDEN)
    
    # Solo permitir actualizar si está pendiente
    if pedido.estado != 'pendiente':
        return Response({
            "error": "Solo se pueden modificar pedidos en estado pendiente"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Solo permitir actualizar cantidad y dirección
    datos_permitidos = {
        'cantidad': request.data.get('cantidad'),
        'direccion_entrega': request.data.get('direccion_entrega')
    }
    datos_permitidos = {k: v for k, v in datos_permitidos.items() if v is not None}
    
    serializer = PedidoSerializer(
        pedido, 
        data=datos_permitidos, 
        partial=True,
        context={'request': request}
    )
    
    if serializer.is_valid():
        serializer.save()
        return Response({
            "mensaje": "Pedido actualizado correctamente",
            "pedido": serializer.data
        }, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def cambiar_estado_pedido(request, pk):
    """Cambiar estado del pedido (solo admin)"""
    pedido = get_object_or_404(Pedido, pk=pk)
    serializer = PedidoEstadoSerializer(pedido, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        response_serializer = PedidoSerializer(pedido, context={'request': request})
        
        return Response({
            "mensaje": "Estado del pedido actualizado correctamente",
            "pedido": response_serializer.data
        }, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def cancelar_pedido(request, pk):
    """Cancelar pedido (cambiar estado a cancelado)"""
    pedido = get_object_or_404(Pedido, pk=pk)
    
    # Verificar que el usuario sea el dueño
    if pedido.usuario != request.user:
        return Response({
            "error": "No tienes permiso para cancelar este pedido"
        }, status=status.HTTP_403_FORBIDDEN)
    
    # Solo permitir cancelar si está pendiente
    if pedido.estado != 'pendiente':
        return Response({
            "error": "Solo se pueden cancelar pedidos en estado pendiente"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    pedido.estado = 'cancelado'
    pedido.save()
    
    serializer = PedidoSerializer(pedido, context={'request': request})
    return Response({
        "mensaje": "Pedido cancelado correctamente",
        "pedido": serializer.data
    }, status=status.HTTP_200_OK)


# ========== RESEÑAS ==========

@api_view(['GET'])
def listar_resenas_producto(request, producto_id):
    """Listar reseñas de un producto (solo visibles)"""
    producto = get_object_or_404(Producto, pk=producto_id)
    resenas = Resena.objects.filter(producto=producto, visible=True)
    
    serializer = ResenaListSerializer(resenas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_resenas_usuario(request):
    """Listar reseñas del usuario autenticado"""
    resenas = Resena.objects.filter(usuario=request.user)
    serializer = ResenaSerializer(resenas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def listar_todas_resenas(request):
    """Listar todas las reseñas (solo admin)"""
    visible = request.query_params.get('visible')
    
    resenas = Resena.objects.all()
    
    if visible is not None:
        resenas = resenas.filter(visible=visible.lower() == 'true')
    
    serializer = ResenaSerializer(resenas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_resena(request):
    """Crear nueva reseña"""
    serializer = ResenaCreateSerializer(data=request.data)
    
    if serializer.is_valid():
        producto = serializer.validated_data['producto']
        
        # Verificar si ya existe una reseña del usuario para este producto
        resena_existente = Resena.objects.filter(
            usuario=request.user,
            producto=producto
        ).first()
        
        if resena_existente:
            return Response({
                "error": "Ya has dejado una reseña para este producto"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        resena = serializer.save(usuario=request.user)
        response_serializer = ResenaSerializer(resena)
        
        return Response({
            "mensaje": "Reseña creada correctamente",
            "resena": response_serializer.data
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def actualizar_resena(request, pk):
    """Actualizar reseña existente"""
    resena = get_object_or_404(Resena, pk=pk)
    
    # Verificar que el usuario sea el dueño
    if resena.usuario != request.user:
        return Response({
            "error": "No tienes permiso para modificar esta reseña"
        }, status=status.HTTP_403_FORBIDDEN)
    
    serializer = ResenaSerializer(resena, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response({
            "mensaje": "Reseña actualizada correctamente",
            "resena": serializer.data
        }, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_resena(request, pk):
    """Eliminar reseña"""
    resena = get_object_or_404(Resena, pk=pk)
    
    # Verificar que el usuario sea el dueño o admin
    if resena.usuario != request.user and not request.user.es_admin:
        return Response({
            "error": "No tienes permiso para eliminar esta reseña"
        }, status=status.HTTP_403_FORBIDDEN)
    
    resena.delete()
    
    return Response({
        "mensaje": "Reseña eliminada correctamente"
    }, status=status.HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def cambiar_visibilidad_resena(request, pk):
    """Cambiar visibilidad de reseña (solo admin)"""
    resena = get_object_or_404(Resena, pk=pk)
    serializer = ResenaVisibilidadSerializer(resena, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        response_serializer = ResenaSerializer(resena)
        
        return Response({
            "mensaje": "Visibilidad de reseña actualizada correctamente",
            "resena": response_serializer.data
        }, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)