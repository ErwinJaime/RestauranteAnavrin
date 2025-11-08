# usuarios/serializers.py
from rest_framework import serializers
from .models import Usuario, Producto, Pedido, Resena
from django.contrib.auth.password_validation import validate_password

# ========== USUARIO SERIALIZERS ==========

class UsuarioSerializer(serializers.ModelSerializer):
    """Serializer completo para Usuario (lectura)"""
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'correo', 'password', 'es_admin', 
                  'is_active', 'is_staff', 'creadoen']
        read_only_fields = ['id', 'creadoen', 'es_admin', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        usuario = Usuario.objects.create_user(**validated_data)
        usuario.set_password(password)
        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if password:
            instance.set_password(password)
        
        instance.save()
        return instance


class UsuarioRegistroSerializer(serializers.ModelSerializer):
    """Serializer para registro de nuevos usuarios"""
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True, 
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                "password": "Las contraseñas no coinciden"
            })
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        return Usuario.objects.create_user(**validated_data)


class UsuarioPerfilSerializer(serializers.ModelSerializer):
    """Serializer simplificado para perfil público"""
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'correo', 'creadoen']
        read_only_fields = ['id', 'creadoen']


# ========== PRODUCTO SERIALIZERS ==========

class ProductoSerializer(serializers.ModelSerializer):
    """Serializer completo para Producto"""
    promedio_calificacion = serializers.SerializerMethodField()
    total_resenas = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'ingredientes', 'precio', 'imagen', 
                  'categoria', 'disponible', 'creadoen',
                  'promedio_calificacion', 'total_resenas']
        read_only_fields = ['id', 'creadoen']

    def get_promedio_calificacion(self, obj):
        resenas = obj.resenas.filter(visible=True)
        if resenas.exists():
            return round(sum(r.calificacion for r in resenas) / resenas.count(), 1)
        return None

    def get_total_resenas(self, obj):
        return obj.resenas.filter(visible=True).count()
    
    def to_representation(self, instance):
        """Personalizar la representación para incluir URL completa de imagen"""
        representation = super().to_representation(instance)
        
        # Convertir la imagen a URL completa
        if instance.imagen:
            request = self.context.get('request')
            if request:
                representation['imagen'] = request.build_absolute_uri(instance.imagen.url)
            else:
                representation['imagen'] = instance.imagen.url
        
        return representation


class ProductoListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listado de productos"""
    promedio_calificacion = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'ingredientes', 'precio', 'imagen', 'categoria', 
                  'disponible', 'promedio_calificacion']

    def get_promedio_calificacion(self, obj):
        resenas = obj.resenas.filter(visible=True)
        if resenas.exists():
            return round(sum(r.calificacion for r in resenas) / resenas.count(), 1)
        return None
    
    def to_representation(self, instance):
        """Personalizar la representación para incluir URL completa de imagen"""
        representation = super().to_representation(instance)
        
        # Convertir la imagen a URL completa
        if instance.imagen:
            request = self.context.get('request')
            if request:
                representation['imagen'] = request.build_absolute_uri(instance.imagen.url)
            else:
                representation['imagen'] = instance.imagen.url
        
        return representation
# ========== PEDIDO SERIALIZERS ==========

class PedidoSerializer(serializers.ModelSerializer):
    """Serializer completo para Pedido"""
    usuario_nombre = serializers.CharField(source='usuario.nombre', read_only=True)
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    producto_imagen = serializers.SerializerMethodField()
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'usuario_nombre', 'producto', 'producto_nombre',
                  'producto_imagen', 'cantidad', 'precio_unitario', 'subtotal',
                  'fecha_pedido', 'estado', 'estado_display', 'direccion_entrega']
        read_only_fields = ['id', 'fecha_pedido', 'precio_unitario']

    def get_producto_imagen(self, obj):
        if obj.producto.imagen:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.producto.imagen.url)
            return obj.producto.imagen.url
        return None

    def validate(self, attrs):
        # Validar que el producto esté disponible
        producto = attrs.get('producto')
        if producto and not producto.disponible:
            raise serializers.ValidationError({
                "producto": "Este producto no está disponible actualmente"
            })
        return attrs

    def create(self, validated_data):
        # Guardar el precio actual del producto
        producto = validated_data['producto']
        validated_data['precio_unitario'] = producto.precio
        return super().create(validated_data)


class PedidoCreateSerializer(serializers.ModelSerializer):
    """Serializer para crear pedidos"""
    class Meta:
        model = Pedido
        fields = ['producto', 'cantidad', 'direccion_entrega']

    def validate_producto(self, value):
        if not value.disponible:
            raise serializers.ValidationError("Este producto no está disponible")
        return value

    def create(self, validated_data):
        # El usuario se asigna desde la vista
        validated_data['precio_unitario'] = validated_data['producto'].precio
        return super().create(validated_data)


class PedidoListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listado de pedidos"""
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'producto_nombre', 'cantidad', 'subtotal', 
                  'fecha_pedido', 'estado', 'estado_display']


class PedidoEstadoSerializer(serializers.ModelSerializer):
    """Serializer para actualizar solo el estado del pedido"""
    class Meta:
        model = Pedido
        fields = ['estado']


# ========== RESEÑA SERIALIZERS ==========

class ResenaSerializer(serializers.ModelSerializer):
    """Serializer completo para Reseña"""
    usuario_nombre = serializers.CharField(source='usuario.nombre', read_only=True)
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    emoji_display = serializers.CharField(source='get_emoji_display', read_only=True)

    class Meta:
        model = Resena
        fields = ['id', 'usuario', 'usuario_nombre', 'producto', 'producto_nombre',
                  'nombre_usuario', 'emoji', 'emoji_display', 'calificacion', 
                  'comentario', 'fecha', 'visible']
        read_only_fields = ['id', 'fecha', 'nombre_usuario']

    def validate_calificacion(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("La calificación debe estar entre 1 y 5")
        return value

    def create(self, validated_data):
        # El nombre_usuario se asigna automáticamente en el modelo
        return super().create(validated_data)


class ResenaCreateSerializer(serializers.ModelSerializer):
    """Serializer para crear reseñas"""
    class Meta:
        model = Resena
        fields = ['producto', 'emoji', 'calificacion', 'comentario']

    def validate_calificacion(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("La calificación debe estar entre 1 y 5")
        return value


class ResenaListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listado de reseñas"""
    emoji_display = serializers.CharField(source='get_emoji_display', read_only=True)

    class Meta:
        model = Resena
        fields = ['id', 'nombre_usuario', 'emoji', 'emoji_display', 
                  'calificacion', 'comentario', 'fecha']


class ResenaVisibilidadSerializer(serializers.ModelSerializer):
    """Serializer para cambiar visibilidad de reseñas (solo admin)"""
    class Meta:
        model = Resena
        fields = ['visible']