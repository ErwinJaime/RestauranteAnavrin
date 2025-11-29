# usuarios/models.py
import random
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from datetime import timedelta

# ========== USUARIO ==========
class UsuarioManager(BaseUserManager):
    def create_user(self, correo, password=None, **extra_fields):
        """Crear y guardar un usuario"""
        if not correo:
            raise ValueError('El correo es obligatorio')
        
        correo = self.normalize_email(correo)

        # Autodetección de admin
        if correo == 'admin@anavrin.com':
            extra_fields.setdefault('es_admin', True)
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_active', True)  # Admin siempre activo
        else:
            # Para usuarios normales, valores por defecto
            extra_fields.setdefault('es_admin', False)
            extra_fields.setdefault('is_staff', False)
            # NO establecer is_active aquí - respetar lo que venga

        user = self.model(correo=correo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, password=None, **extra_fields):
        """Crear y guardar un superusuario"""
        extra_fields.setdefault('es_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('es_admin') is not True:
            raise ValueError('Superuser debe tener es_admin=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        
        return self.create_user(correo, password, **extra_fields)


class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    correo = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    es_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)  # ✅ CAMBIO: Inactivo por defecto
    is_staff = models.BooleanField(default=False)
    creadoen = models.DateTimeField(auto_now_add=True)

    objects = UsuarioManager()
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre']

    class Meta:
        db_table = "usuarios"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        if self.correo == 'admin@anavrin.com':
            self.es_admin = True
            self.is_staff = True
            self.is_active = True
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} - {self.correo}"

# ========== PRODUCTO ==========

class Producto(models.Model):
    CATEGORIAS = (
        ('platillo', 'Platillo'),
        ('postre', 'Postre'),
        ('bebida', 'Bebida'),
    )

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    ingredientes = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    disponible = models.BooleanField(default=True)
    creadoen = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "productos"
        ordering = ['categoria', 'nombre']

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

# ========== PEDIDO ==========

class Pedido(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('preparando', 'Preparando'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    )

    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='pedidos')
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    direccion_entrega = models.TextField()

    class Meta:
        db_table = "pedidos"
        ordering = ['-fecha_pedido']
        unique_together = ('usuario', 'producto')

    def __str__(self):
        estado_display = dict(self.ESTADOS).get(self.estado, self.estado)
        return f"Pedido #{self.id} - {self.usuario.nombre} - {self.producto.nombre} ({estado_display})"

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario

# ========== RESEÑA ==========

class Resena(models.Model):
    EMOJIS = (
        ('feliz', '😊 Feliz'),
        ('neutral', '😐 Neutral'),
        ('triste', '😢 Triste'),
    )

    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='resenas')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='resenas')
    nombre_usuario = models.CharField(max_length=150)
    emoji = models.CharField(max_length=10, choices=EMOJIS)
    calificacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)

    class Meta:
        db_table = "resenas"
        ordering = ['-fecha']
        unique_together = ('usuario', 'producto')

    def save(self, *args, **kwargs):
        if not self.nombre_usuario:
            self.nombre_usuario = self.usuario.nombre
        super().save(*args, **kwargs)

    def __str__(self):
        emoji_display = dict(self.EMOJIS).get(self.emoji, self.emoji)
        return f"{self.nombre_usuario} - {self.producto.nombre} ({self.calificacion}★) {emoji_display}"

# ========== CÓDIGO DE VERIFICACIÓN ==========

class CodigoVerificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='codigos_verificacion')
    codigo = models.CharField(max_length=6)
    creado_en = models.DateTimeField(auto_now_add=True)
    verificado = models.BooleanField(default=False)
    expira = models.DateTimeField(editable=False)
    
    class Meta:
        db_table = "codigos_verificacion"
        ordering = ['-creado_en']
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.expira = timezone.now() + timedelta(minutes=10)
        super().save(*args, **kwargs)
    
    def es_valido(self):
        """Verificar si el código no ha expirado y no ha sido usado"""
        return not self.verificado and timezone.now() < self.expira
    
    @staticmethod
    def generar_codigo():
        """Generar código de 6 dígitos"""
        return ''.join([str(random.randint(0, 9)) for _ in range(6)])
    
    def __str__(self):
        estado = "✅ Verificado" if self.verificado else ("❌ Expirado" if not self.es_valido() else "⏳ Pendiente")
        return f"Código {self.codigo} - {self.usuario.correo} - {estado}"